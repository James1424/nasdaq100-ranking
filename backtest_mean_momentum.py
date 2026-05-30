import pandas as pd
import yfinance as yf

from stock_database import get_nasdaq100_tickers


# ============================================================
# Configuration
# ============================================================

# 用更早的数据做 warm-up，用来计算 6 个月动量和 10 个月市场均线
DATA_START_DATE = "2014-01-01"

# 真正开始计算收益的日期
# 2016-02-01 是美股交易日，因此第一期可以严格从 2016-02-01 开始
BACKTEST_START_DATE = "2016-02-01"

END_DATE = "2026-12-31"

LOOKBACK_MONTHS = 6
TOP_N = 3

MARKET_INDEX_TICKER = "QQQ"
MARKET_TREND_MONTHS = 10

RETURNS_OUTPUT = "nasdaq100_mean_momentum_backtest_returns.csv"
HOLDINGS_OUTPUT = "nasdaq100_mean_momentum_backtest_holdings.csv"
SUMMARY_OUTPUT = "nasdaq100_mean_momentum_backtest_summary.csv"

REGIME_RETURNS_OUTPUT = "nasdaq100_mean_momentum_regime_backtest_returns.csv"
REGIME_SUMMARY_OUTPUT = "nasdaq100_mean_momentum_regime_backtest_summary.csv"


# ============================================================
# Data Download
# ============================================================

def download_adjusted_close(tickers, start_date, end_date):
    data = yf.download(
        tickers=tickers,
        start=start_date,
        end=end_date,
        auto_adjust=True,
        group_by="ticker",
        progress=False,
        threads=True,
    )

    prices = {}

    for ticker in tickers:
        try:
            if isinstance(data.columns, pd.MultiIndex):
                if ticker in data.columns.get_level_values(0):
                    if "Close" in data[ticker].columns:
                        prices[ticker] = data[ticker]["Close"]
            else:
                if "Close" in data.columns:
                    prices[ticker] = data["Close"]
        except Exception:
            continue

    price_df = pd.DataFrame(prices)
    price_df = price_df.dropna(axis=1, how="all")
    price_df = price_df.ffill()

    return price_df


def download_market_index(ticker, start_date, end_date):
    data = yf.download(
        tickers=ticker,
        start=start_date,
        end=end_date,
        auto_adjust=True,
        progress=False,
    )

    if data.empty:
        raise ValueError(f"No market index data downloaded for {ticker}.")

    if isinstance(data.columns, pd.MultiIndex):
        if "Close" in data.columns.get_level_values(0):
            close = data["Close"]

            if isinstance(close, pd.DataFrame):
                close = close.iloc[:, 0]

        elif ticker in data.columns.get_level_values(0):
            close = data[ticker]["Close"]

        else:
            raise KeyError(
                f"Could not find Close price for {ticker}. Columns: {data.columns}"
            )

    else:
        if "Close" not in data.columns:
            raise KeyError(
                f"Close column not found for {ticker}. Columns: {data.columns}"
            )

        close = data["Close"]

    close = close.dropna()
    close.name = ticker

    return close


# ============================================================
# Signals
# ============================================================

def calculate_six_month_mean_momentum(monthly_prices):
    monthly_returns = monthly_prices.pct_change()

    six_month_mean_momentum = (
        monthly_returns
        .rolling(window=LOOKBACK_MONTHS)
        .mean()
    )

    return six_month_mean_momentum


def calculate_market_regime(market_index_prices):
    monthly_index = market_index_prices.resample("ME").last()

    market_ma = monthly_index.rolling(window=MARKET_TREND_MONTHS).mean()

    regime = pd.DataFrame(
        {
            "market_index_price": monthly_index,
            "market_index_ma": market_ma,
        }
    )

    regime["is_bull_market"] = (
        regime["market_index_price"] > regime["market_index_ma"]
    )

    regime["market_regime"] = regime["is_bull_market"].map(
        {
            True: "Bull Market",
            False: "Bear Market",
        }
    )

    return regime


# ============================================================
# Common Holding Periods
# ============================================================

def build_common_holding_periods(price_df):
    """
    Build one shared monthly holding-period table.

    Both the normal backtest and the market-regime backtest must use this
    exact same table. This guarantees identical holding_start and holding_end.

    Example first period:
        holding_start = 2016-02-01
        holding_end   = 2016-02-29
        ranking_date  = 2016-01-29

    ranking_date means:
        Use information available at the previous month-end to decide
        the portfolio for the next month.
    """

    backtest_start = pd.Timestamp(BACKTEST_START_DATE)

    monthly_periods = pd.period_range(
        start=backtest_start,
        end=price_df.index.max(),
        freq="M"
    )

    holding_periods = []

    for period in monthly_periods:
        calendar_start = period.start_time.normalize()
        calendar_end = period.end_time.normalize()

        month_trading_dates = price_df.index[
            (price_df.index >= calendar_start) &
            (price_df.index <= calendar_end)
        ]

        if len(month_trading_dates) == 0:
            continue

        holding_start = month_trading_dates[0]
        holding_end = month_trading_dates[-1]

        previous_month_end = calendar_start - pd.offsets.MonthEnd(1)

        ranking_candidates = price_df.index[
            price_df.index <= previous_month_end
        ]

        if len(ranking_candidates) == 0:
            continue

        ranking_date = ranking_candidates[-1]

        holding_periods.append(
            {
                "ranking_date": ranking_date,
                "holding_start": holding_start,
                "holding_end": holding_end,
            }
        )

    if len(holding_periods) == 0:
        raise ValueError("No valid holding periods were built.")

    return holding_periods


# ============================================================
# Backtest Without Market Regime Filter
# ============================================================

def run_backtest(price_df, holding_periods):
    monthly_prices = price_df.resample("ME").last()
    momentum_score = calculate_six_month_mean_momentum(monthly_prices)

    portfolio_records = []
    holdings_records = []

    for period in holding_periods:
        ranking_date = period["ranking_date"]
        holding_start = period["holding_start"]
        holding_end = period["holding_end"]

        if ranking_date not in momentum_score.index:
            continue

        scores = momentum_score.loc[ranking_date].dropna()
        selected = scores.sort_values(ascending=False).head(TOP_N).index.tolist()

        if len(selected) == 0:
            continue

        start_prices = price_df.loc[holding_start, selected]
        end_prices = price_df.loc[holding_end, selected]

        stock_returns = end_prices / start_prices - 1
        stock_returns = stock_returns.dropna()

        if len(stock_returns) == 0:
            continue

        portfolio_return = stock_returns.mean()
        actual_selected = stock_returns.index.tolist()

        portfolio_records.append(
            {
                "ranking_date": ranking_date.strftime("%Y-%m-%d"),
                "selected_stocks": ",".join(actual_selected),
                "holding_start": holding_start.strftime("%Y-%m-%d"),
                "holding_end": holding_end.strftime("%Y-%m-%d"),
                "portfolio_return": portfolio_return,
                "portfolio_return_percent": portfolio_return * 100,
            }
        )

        holdings_records.append(
            {
                "ranking_date": ranking_date.strftime("%Y-%m-%d"),
                "holding_start": holding_start.strftime("%Y-%m-%d"),
                "holding_end": holding_end.strftime("%Y-%m-%d"),
                "selected_stocks": ",".join(actual_selected),
            }
        )

    returns_df = pd.DataFrame(portfolio_records)
    holdings_df = pd.DataFrame(holdings_records)

    if len(returns_df) > 0:
        returns_df["cumulative_return"] = (
            1 + returns_df["portfolio_return"]
        ).cumprod() - 1

        returns_df["cumulative_return_percent"] = (
            returns_df["cumulative_return"] * 100
        )

    return returns_df, holdings_df


# ============================================================
# Backtest With Market Regime Filter
# ============================================================

def run_market_regime_backtest(price_df, market_index_prices, holding_periods):
    monthly_prices = price_df.resample("ME").last()
    momentum_score = calculate_six_month_mean_momentum(monthly_prices)
    market_regime = calculate_market_regime(market_index_prices)

    portfolio_records = []

    for period in holding_periods:
        ranking_date = period["ranking_date"]
        holding_start = period["holding_start"]
        holding_end = period["holding_end"]

        if ranking_date not in momentum_score.index:
            continue

        if ranking_date not in market_regime.index:
            raise ValueError(
                f"Missing market regime data for ranking date {ranking_date}."
            )

        regime_row = market_regime.loc[ranking_date]

        if pd.isna(regime_row["market_index_ma"]):
            raise ValueError(
                f"Market regime moving average is missing for {ranking_date}. "
                f"Use an earlier DATA_START_DATE."
            )

        is_bull_market = bool(regime_row["is_bull_market"])
        market_regime_label = regime_row["market_regime"]

        scores = momentum_score.loc[ranking_date].dropna()
        selected = scores.sort_values(ascending=False).head(TOP_N).index.tolist()

        if len(selected) == 0:
            continue

        if is_bull_market:
            start_prices = price_df.loc[holding_start, selected]
            end_prices = price_df.loc[holding_end, selected]

            stock_returns = end_prices / start_prices - 1
            stock_returns = stock_returns.dropna()

            if len(stock_returns) == 0:
                continue

            portfolio_return = stock_returns.mean()
            selected_stocks = ",".join(stock_returns.index.tolist())

        else:
            portfolio_return = 0.0
            selected_stocks = "CASH"

        portfolio_records.append(
            {
                "ranking_date": ranking_date.strftime("%Y-%m-%d"),
                "market_regime": market_regime_label,
                "is_bull_market": is_bull_market,
                "market_index_price": regime_row["market_index_price"],
                "market_index_ma": regime_row["market_index_ma"],
                "selected_stocks": selected_stocks,
                "holding_start": holding_start.strftime("%Y-%m-%d"),
                "holding_end": holding_end.strftime("%Y-%m-%d"),
                "portfolio_return": portfolio_return,
                "portfolio_return_percent": portfolio_return * 100,
            }
        )

    returns_df = pd.DataFrame(portfolio_records)

    if len(returns_df) > 0:
        returns_df["cumulative_return"] = (
            1 + returns_df["portfolio_return"]
        ).cumprod() - 1

        returns_df["cumulative_return_percent"] = (
            returns_df["cumulative_return"] * 100
        )

    return returns_df


# ============================================================
# Summary
# ============================================================

def summarize_backtest(returns_df):
    if len(returns_df) == 0:
        return pd.DataFrame()

    monthly_returns = returns_df["portfolio_return"]

    total_return = (1 + monthly_returns).prod() - 1
    annualized_return = (1 + total_return) ** (12 / len(monthly_returns)) - 1
    annualized_volatility = monthly_returns.std() * (12 ** 0.5)

    if annualized_volatility == 0 or pd.isna(annualized_volatility):
        sharpe_ratio = None
    else:
        sharpe_ratio = annualized_return / annualized_volatility

    cumulative = (1 + monthly_returns).cumprod()
    running_max = cumulative.cummax()
    drawdown = cumulative / running_max - 1
    max_drawdown = drawdown.min()

    win_rate = (monthly_returns > 0).mean()

    positive_months = int((monthly_returns > 0).sum())
    negative_months = int((monthly_returns < 0).sum())
    zero_months = int((monthly_returns == 0).sum())

    summary = pd.DataFrame(
        [
            {
                "strategy_name": "Nasdaq-100 Top 3 Six-Month Mean Momentum",
                "data_start_date": DATA_START_DATE,
                "backtest_start_date": BACKTEST_START_DATE,
                "start_date": returns_df["holding_start"].iloc[0],
                "end_date": returns_df["holding_end"].iloc[-1],
                "lookback_months": LOOKBACK_MONTHS,
                "top_n": TOP_N,
                "total_return_percent": total_return * 100,
                "annualized_return_percent": annualized_return * 100,
                "annualized_volatility_percent": annualized_volatility * 100,
                "sharpe_ratio_without_risk_free_rate": sharpe_ratio,
                "max_drawdown_percent": max_drawdown * 100,
                "win_rate_percent": win_rate * 100,
                "positive_months": positive_months,
                "negative_months": negative_months,
                "zero_months": zero_months,
                "number_of_months": len(monthly_returns),
            }
        ]
    )

    return summary


def summarize_market_regime_backtest(returns_df):
    if len(returns_df) == 0:
        return pd.DataFrame()

    monthly_returns = returns_df["portfolio_return"]

    total_return = (1 + monthly_returns).prod() - 1
    annualized_return = (1 + total_return) ** (12 / len(monthly_returns)) - 1
    annualized_volatility = monthly_returns.std() * (12 ** 0.5)

    if annualized_volatility == 0 or pd.isna(annualized_volatility):
        sharpe_ratio = None
    else:
        sharpe_ratio = annualized_return / annualized_volatility

    cumulative = (1 + monthly_returns).cumprod()
    running_max = cumulative.cummax()
    drawdown = cumulative / running_max - 1
    max_drawdown = drawdown.min()

    win_rate = (monthly_returns > 0).mean()

    bull_months = int(returns_df["is_bull_market"].sum())
    bear_months = len(returns_df) - bull_months

    trading_months = bull_months
    cash_months = bear_months

    positive_months = int((monthly_returns > 0).sum())
    negative_months = int((monthly_returns < 0).sum())
    zero_months = int((monthly_returns == 0).sum())

    bull_returns = returns_df.loc[
        returns_df["is_bull_market"],
        "portfolio_return"
    ]

    bear_returns = returns_df.loc[
        ~returns_df["is_bull_market"],
        "portfolio_return"
    ]

    summary = pd.DataFrame(
        [
            {
                "strategy_name": "Nasdaq-100 Top 3 Six-Month Mean Momentum With Market Regime Filter",
                "data_start_date": DATA_START_DATE,
                "backtest_start_date": BACKTEST_START_DATE,
                "market_index_ticker": MARKET_INDEX_TICKER,
                "market_trend_months": MARKET_TREND_MONTHS,
                "start_date": returns_df["holding_start"].iloc[0],
                "end_date": returns_df["holding_end"].iloc[-1],
                "lookback_months": LOOKBACK_MONTHS,
                "top_n": TOP_N,
                "bull_market_months": bull_months,
                "bear_market_months": bear_months,
                "trading_months": trading_months,
                "cash_months": cash_months,
                "bull_market_average_monthly_return_percent": bull_returns.mean() * 100,
                "bear_market_average_monthly_return_percent": bear_returns.mean() * 100,
                "total_return_percent": total_return * 100,
                "annualized_return_percent": annualized_return * 100,
                "annualized_volatility_percent": annualized_volatility * 100,
                "sharpe_ratio_without_risk_free_rate": sharpe_ratio,
                "max_drawdown_percent": max_drawdown * 100,
                "win_rate_percent": win_rate * 100,
                "positive_months": positive_months,
                "negative_months": negative_months,
                "zero_months": zero_months,
                "number_of_months": len(monthly_returns),
            }
        ]
    )

    return summary


# ============================================================
# Validation
# ============================================================

def validate_identical_holding_periods(returns_df, regime_returns_df):
    normal_periods = returns_df[
        ["holding_start", "holding_end"]
    ].reset_index(drop=True)

    regime_periods = regime_returns_df[
        ["holding_start", "holding_end"]
    ].reset_index(drop=True)

    if not normal_periods.equals(regime_periods):
        comparison = pd.concat(
            [
                normal_periods.add_prefix("normal_"),
                regime_periods.add_prefix("regime_"),
            ],
            axis=1
        )

        mismatch = comparison[
            (comparison["normal_holding_start"] != comparison["regime_holding_start"]) |
            (comparison["normal_holding_end"] != comparison["regime_holding_end"])
        ]

        raise ValueError(
            "The normal backtest and regime backtest do not have identical "
            f"holding periods.\nFirst mismatches:\n{mismatch.head(10)}"
        )

    print("\nHolding periods are exactly identical.")
    print("Common start:", returns_df["holding_start"].iloc[0])
    print("Common end:", returns_df["holding_end"].iloc[-1])
    print("Number of months:", len(returns_df))


# ============================================================
# Main
# ============================================================

if __name__ == "__main__":
    print("Getting Nasdaq-100 tickers...")
    tickers = get_nasdaq100_tickers()
    print(f"Number of tickers: {len(tickers)}")

    print("\nDownloading adjusted close prices...")
    price_df = download_adjusted_close(
        tickers=tickers,
        start_date=DATA_START_DATE,
        end_date=END_DATE,
    )

    print("\nDownloading market index prices...")
    market_index_prices = download_market_index(
        ticker=MARKET_INDEX_TICKER,
        start_date=DATA_START_DATE,
        end_date=END_DATE,
    )

    print("\nBuilding common holding periods...")
    holding_periods = build_common_holding_periods(price_df)

    print("\nFirst 5 common holding periods:")
    for period in holding_periods[:5]:
        print(
            period["ranking_date"].strftime("%Y-%m-%d"),
            "->",
            period["holding_start"].strftime("%Y-%m-%d"),
            "to",
            period["holding_end"].strftime("%Y-%m-%d")
        )

    print("\nRunning six-month mean momentum backtest without market regime filter...")
    returns_df, holdings_df = run_backtest(price_df, holding_periods)

    print("\nRunning six-month mean momentum backtest with market regime filter...")
    regime_returns_df = run_market_regime_backtest(
        price_df=price_df,
        market_index_prices=market_index_prices,
        holding_periods=holding_periods,
    )

    validate_identical_holding_periods(returns_df, regime_returns_df)

    print("\nSummarizing original backtest...")
    summary_df = summarize_backtest(returns_df)

    print("\nSummarizing market regime backtest...")
    regime_summary_df = summarize_market_regime_backtest(regime_returns_df)

    returns_df.to_csv(RETURNS_OUTPUT, index=False)
    holdings_df.to_csv(HOLDINGS_OUTPUT, index=False)
    summary_df.to_csv(SUMMARY_OUTPUT, index=False)

    regime_returns_df.to_csv(REGIME_RETURNS_OUTPUT, index=False)
    regime_summary_df.to_csv(REGIME_SUMMARY_OUTPUT, index=False)

    print("\nOriginal backtest first rows:")
    print(returns_df.head().to_string(index=False))

    print("\nMarket regime backtest first rows:")
    print(regime_returns_df.head().to_string(index=False))

    print("\nOriginal backtest summary:")
    print(summary_df.to_string(index=False))

    print("\nMarket regime backtest summary:")
    print(regime_summary_df.to_string(index=False))

    print("\nBacktest files saved:")
    print(RETURNS_OUTPUT)
    print(HOLDINGS_OUTPUT)
    print(SUMMARY_OUTPUT)
    print(REGIME_RETURNS_OUTPUT)
    print(REGIME_SUMMARY_OUTPUT)
