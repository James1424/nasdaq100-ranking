from datetime import datetime, timezone
import os

import pandas as pd


LATEST_RANK_FILE = "nasdaq100_six_month_momentum_rank.csv"

BACKTEST_SUMMARY_FILE = "nasdaq100_mean_momentum_backtest_summary.csv"
BACKTEST_RETURNS_FILE = "nasdaq100_mean_momentum_backtest_returns.csv"
BACKTEST_HOLDINGS_FILE = "nasdaq100_mean_momentum_backtest_holdings.csv"

REGIME_SUMMARY_FILE = "nasdaq100_mean_momentum_regime_backtest_summary.csv"
REGIME_RETURNS_FILE = "nasdaq100_mean_momentum_regime_backtest_returns.csv"

README_PATH = "README.md"


def load_table(path):
    if not os.path.exists(path):
        return None
    return pd.read_csv(path)


def format_percent_columns(df):
    df = df.copy()

    for col in df.columns:
        if "percent" in col.lower():
            if pd.api.types.is_numeric_dtype(df[col]):
                df[col] = df[col].round(2)

    for col in df.columns:
        if "return" in col.lower() and "percent" not in col.lower():
            if pd.api.types.is_numeric_dtype(df[col]):
                df[col] = df[col].round(4)

    for col in df.columns:
        if "price" in col.lower():
            if pd.api.types.is_numeric_dtype(df[col]):
                df[col] = df[col].round(2)

    for col in df.columns:
        if col.lower().endswith("_ma"):
            if pd.api.types.is_numeric_dtype(df[col]):
                df[col] = df[col].round(2)

    return df


def summarize_monthly_return_statistics(backtest_returns):
    if backtest_returns is None or len(backtest_returns) == 0:
        return "Backtest return statistics file not found."

    if "portfolio_return" not in backtest_returns.columns:
        return "Column `portfolio_return` not found in backtest returns file."

    returns = backtest_returns["portfolio_return"].dropna()

    if len(returns) == 0:
        return "No valid monthly returns found."

    winning_months = returns[returns > 0]
    losing_months = returns[returns < 0]
    flat_months = returns[returns == 0]

    stats = pd.DataFrame(
        [
            {
                "metric": "Total months",
                "value": len(returns),
            },
            {
                "metric": "Winning months",
                "value": len(winning_months),
            },
            {
                "metric": "Losing months",
                "value": len(losing_months),
            },
            {
                "metric": "Flat months",
                "value": len(flat_months),
            },
            {
                "metric": "Win rate percent",
                "value": round(len(winning_months) / len(returns) * 100, 2),
            },
            {
                "metric": "Average monthly return percent",
                "value": round(returns.mean() * 100, 2),
            },
            {
                "metric": "Average winning month percent",
                "value": round(winning_months.mean() * 100, 2)
                if len(winning_months) > 0
                else None,
            },
            {
                "metric": "Average losing month percent",
                "value": round(losing_months.mean() * 100, 2)
                if len(losing_months) > 0
                else None,
            },
            {
                "metric": "Best month percent",
                "value": round(returns.max() * 100, 2),
            },
            {
                "metric": "Worst month percent",
                "value": round(returns.min() * 100, 2),
            },
            {
                "metric": "Monthly volatility percent",
                "value": round(returns.std() * 100, 2),
            },
            {
                "metric": "Profit loss ratio",
                "value": round(winning_months.mean() / abs(losing_months.mean()), 2)
                if len(winning_months) > 0 and len(losing_months) > 0
                else None,
            },
        ]
    )

    return stats.to_markdown(index=False)


def build_strategy_comparison_table(original_summary, regime_summary):
    if original_summary is None or regime_summary is None:
        return "Strategy comparison cannot be generated because one of the summary files is missing."

    if len(original_summary) == 0 or len(regime_summary) == 0:
        return "Strategy comparison cannot be generated because one of the summary files is empty."

    original = original_summary.iloc[0]
    regime = regime_summary.iloc[0]

    metrics = [
        "total_return_percent",
        "annualized_return_percent",
        "annualized_volatility_percent",
        "sharpe_ratio_without_risk_free_rate",
        "max_drawdown_percent",
        "win_rate_percent",
        "number_of_months",
    ]

    rows = []

    for metric in metrics:
        if metric in original_summary.columns and metric in regime_summary.columns:
            original_value = original[metric]
            regime_value = regime[metric]

            if pd.api.types.is_number(original_value) and pd.api.types.is_number(regime_value):
                difference = regime_value - original_value
            else:
                difference = None

            rows.append(
                {
                    "metric": metric,
                    "original_strategy": original_value,
                    "with_market_regime_filter": regime_value,
                    "difference": difference,
                }
            )

    comparison = pd.DataFrame(rows)
    comparison = format_percent_columns(comparison)

    return comparison.to_markdown(index=False)


def generate_readme(top_n=20):
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    latest_rank = load_table(LATEST_RANK_FILE)

    backtest_summary = load_table(BACKTEST_SUMMARY_FILE)
    backtest_returns = load_table(BACKTEST_RETURNS_FILE)

    regime_summary = load_table(REGIME_SUMMARY_FILE)
    regime_returns = load_table(REGIME_RETURNS_FILE)

    if latest_rank is not None:
        latest_rank_table = format_percent_columns(latest_rank.head(top_n))
        latest_rank_markdown = latest_rank_table.to_markdown(index=False)
    else:
        latest_rank_markdown = "Latest ranking file not found."

    if backtest_summary is not None:
        summary_table = format_percent_columns(backtest_summary)
        summary_markdown = summary_table.to_markdown(index=False)
    else:
        summary_markdown = "Backtest summary file not found."

    if backtest_returns is not None:
        backtest_returns_table = format_percent_columns(backtest_returns)
        backtest_returns_markdown = backtest_returns_table.to_markdown(index=False)
        monthly_statistics_markdown = summarize_monthly_return_statistics(
            backtest_returns
        )
    else:
        backtest_returns_markdown = "Backtest returns file not found."
        monthly_statistics_markdown = "Backtest return statistics file not found."

    if regime_summary is not None:
        regime_summary_table = format_percent_columns(regime_summary)
        regime_summary_markdown = regime_summary_table.to_markdown(index=False)
    else:
        regime_summary_markdown = "Market regime summary file not found."

    if regime_returns is not None:
        regime_returns_table = format_percent_columns(regime_returns)
        regime_returns_markdown = regime_returns_table.to_markdown(index=False)
        regime_statistics_markdown = summarize_monthly_return_statistics(
            regime_returns
        )
    else:
        regime_returns_markdown = "Market regime returns file not found."
        regime_statistics_markdown = "Market regime return statistics file not found."

    strategy_comparison_markdown = build_strategy_comparison_table(
        backtest_summary,
        regime_summary,
    )

    readme_parts = [
        "# Nasdaq-100 Six-Month Mean Momentum Strategy",
        "",
        "This repository builds a rule-based momentum ranking and backtesting system for Nasdaq-100 stocks.",
        "",
        "The core idea is simple:",
        "",
        "> At the beginning of each month, rank Nasdaq-100 stocks by their average monthly return over the previous six months, buy the top three stocks, and hold them for the following month.",
        "",
        "",
        f"Last updated: **{now}**",
        "",
        "---",
        "",
        "## Latest Nasdaq-100 Six-Month Momentum Ranking",
        "",
        "The following table shows the latest Nasdaq-100 momentum ranking up to the most recent available trading date.",
        "",
        f"Top {top_n} stocks are shown below.",
        "",
        latest_rank_markdown,
        "",
        "The full ranking is saved in:",
        "",
        "```text",
        LATEST_RANK_FILE,
        "```",
        "",
        "---",
        "",
        "## Strategy Logic",
        "",
        "At the beginning of each month:",
        "",
        "1. Use only historical monthly returns from the previous six months.",
        "2. Calculate the six-month average momentum signal for each Nasdaq-100 stock.",
        "3. Rank all stocks by this six-month average momentum signal.",
        "4. Select the top three stocks.",
        "5. Hold these stocks for the following month.",
        "6. Use the next month's realized return to calculate strategy performance.",
        "7. Rebalance monthly.",
        "",
        "The strategy does not use news, analyst reports, valuation metrics, market timing, or discretionary stock picking.",
        "",
        "It is a simple rule-based momentum strategy.",
        "",
        "---",
        "",
        "## Backtest Summary",
        "",
        "The following table shows the summary statistics of the monthly mean momentum backtest.",
        "",
        summary_markdown,
        "",
        "---",
        "",
        "## Backtest Monthly Return Statistics",
        "",
        "The following table summarizes the distribution of monthly strategy returns.",
        "",
        monthly_statistics_markdown,
        "",
        "---",
        "",
        "## Full Monthly Backtest Returns",
        "",
        "The following table shows the full monthly strategy return history.",
        "",
        backtest_returns_markdown,
        "",
        "The full monthly return history is saved in:",
        "",
        "```text",
        BACKTEST_RETURNS_FILE,
        "```",
        "",
        "---",
        "",
        "## Market Regime Filter Analysis",
        "",
        "This additional section studies how the strategy changes when a Nasdaq market regime filter is added.",
        "",
        "The original backtest above is kept unchanged. In the regime-filtered version, the same six-month mean momentum signal is still used to select the top three stocks, but trades are executed only when the Nasdaq market index is classified as being in a bull market.",
        "",
        "When the Nasdaq market is classified as a bear market, the strategy stays in cash for the following month and records a 0% return.",
        "",
        "The market regime is determined using only information available up to each ranking date, so the regime filter does not use future returns.",
        "",
        "---",
        "",
        "## Market Regime Filter Logic",
        "",
        "At each ranking date:",
        "",
        "1. Calculate the Nasdaq market index trend using historical index data.",
        "2. Classify the month as a bull market if the index price is above its historical moving average.",
        "3. If the month is a bull market, hold the selected top-three momentum stocks for the following month.",
        "4. If the month is a bear market, stay in cash for the following month.",
        "5. Compare the filtered strategy with the original strategy to evaluate whether the regime filter improves risk-adjusted performance.",
        "",
        "---",
        "",
        "## Strategy Comparison: Original vs Market Regime Filter",
        "",
        "The following table compares the original strategy with the market-regime-filtered version.",
        "",
        strategy_comparison_markdown,
        "",
        "---",
        "",
        "## Market Regime Backtest Summary",
        "",
        "The following table shows the summary statistics of the strategy after adding the Nasdaq market regime filter.",
        "",
        regime_summary_markdown,
        "",
        "---",
        "",
        "## Market Regime Monthly Return Statistics",
        "",
        "The following table summarizes the distribution of monthly strategy returns after applying the market regime filter.",
        "",
        regime_statistics_markdown,
        "",
        "---",
        "",
        "## Full Market Regime Backtest Returns",
        "",
        "The following table shows the full monthly strategy return history with the market regime filter.",
        "",
        regime_returns_markdown,
        "",
        "The full market regime return history is saved in:",
        "",
        "```text",
        REGIME_RETURNS_FILE,
        "```",
        "",
        "---",
        "",
        "## Files",
        "",
        "| File | Description |",
        "|---|---|",
        f"| `{LATEST_RANK_FILE}` | Latest Nasdaq-100 six-month mean momentum ranking |",
        f"| `{BACKTEST_SUMMARY_FILE}` | Backtest summary statistics |",
        f"| `{BACKTEST_RETURNS_FILE}` | Monthly backtest return history |",
        f"| `{BACKTEST_HOLDINGS_FILE}` | Monthly strategy holdings |",
        f"| `{REGIME_SUMMARY_FILE}` | Market regime filtered backtest summary statistics |",
        f"| `{REGIME_RETURNS_FILE}` | Market regime filtered monthly return history |",
        f"| `{README_PATH}` | Auto-generated project README |",
        "",
        "---",
        "",
        "## Disclaimer",
        "",
        "This project is for educational and research purposes only.",
        "",
        "It is not financial advice.",
        "",
        "Momentum strategies can suffer from drawdowns, turnover costs, tax effects, slippage, survivorship bias, and regime changes.",
        "",
        "Past performance does not guarantee future results.",
        "",
    ]

    readme = "\n".join(readme_parts)

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(readme)


if __name__ == "__main__":
    generate_readme()
