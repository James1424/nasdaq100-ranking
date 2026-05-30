import pandas as pd
import yfinance as yf

from stock_database import get_nasdaq100_tickers


START_DATE = "2016-01-01"
END_DATE = "2026-12-31"

LOOKBACK_MONTHS = 6
TOP_N = 3

RETURNS_OUTPUT = "nasdaq100_mean_momentum_backtest_returns.csv"
HOLDINGS_OUTPUT = "nasdaq100_mean_momentum_backtest_holdings.csv"
SUMMARY_OUTPUT = "nasdaq100_mean_momentum_backtest_summary.csv"


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


def calculate_six_month_mean_momentum(monthly_prices):
    monthly_returns = monthly_prices.pct_change()

    six_month_mean_momentum = (
        monthly_returns
        .rolling(window=LOOKBACK_MONTHS)
        .mean()
    )

    return six_month_mean_momentum


def run_backtest(price_df):
    monthly_prices = price_df.resample("ME").last()
    momentum_score = calculate_six_month_mean_momentum(monthly_prices)

    portfolio_records = []
    holdings_records = []

    for i in range(LOOKBACK_MONTHS, len(monthly_prices) - 1):
        ranking_date = monthly_prices.index[i]
        holding_start = monthly_prices.index[i]
        holding_end = monthly_prices.index[i + 1]

        scores = momentum_score.iloc[i].dropna()
        selected = scores.sort_values(ascending=False).head(TOP_N).index.tolist()

        if len(selected) == 0:
            continue

        start_prices = monthly_prices.loc[holding_start, selected]
        end_prices = monthly_prices.loc[holding_end, selected]

        stock_returns = end_prices / start_prices - 1
        stock_returns = stock_returns.dropna()

        if len(stock_returns) == 0:
            continue

        portfolio_return = stock_returns.mean()

        portfolio_records.append(
            {
                "ranking_date": ranking_date.strftime("%Y-%m-%d"),
                "selected_stocks": ",".join(selected),
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
                "selected_stocks": ",".join(selected),
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

    summary = pd.DataFrame(
        [
            {
                "strategy_name": "Nasdaq-100 Top 3 Six-Month Mean Momentum",
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
                "number_of_months": len(monthly_returns),
            }
        ]
    )

    return summary


if __name__ == "__main__":
    print("Getting Nasdaq-100 tickers...")
    tickers = get_nasdaq100_tickers()
    print(f"Number of tickers: {len(tickers)}")

    print("\nDownloading adjusted close prices...")
    price_df = download_adjusted_close(
        tickers=tickers,
        start_date=START_DATE,
        end_date=END_DATE,
    )

    print("\nRunning six-month mean momentum backtest...")
    returns_df, holdings_df = run_backtest(price_df)

    print("\nSummarizing backtest...")
    summary_df = summarize_backtest(returns_df)

    returns_df.to_csv(RETURNS_OUTPUT, index=False)
    holdings_df.to_csv(HOLDINGS_OUTPUT, index=False)
    summary_df.to_csv(SUMMARY_OUTPUT, index=False)

    print("\nBacktest summary:")
    print(summary_df.to_string(index=False))

    print("\nBacktest files saved:")
    print(RETURNS_OUTPUT)
    print(HOLDINGS_OUTPUT)
    print(SUMMARY_OUTPUT)
