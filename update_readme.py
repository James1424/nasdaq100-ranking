from datetime import datetime, timezone
import os

import pandas as pd


LATEST_RANK_FILE = "nasdaq100_six_month_momentum_rank.csv"
BACKTEST_SUMMARY_FILE = "nasdaq100_mean_momentum_backtest_summary.csv"
BACKTEST_RETURNS_FILE = "nasdaq100_mean_momentum_backtest_returns.csv"
BACKTEST_HOLDINGS_FILE = "nasdaq100_mean_momentum_backtest_holdings.csv"
README_PATH = "README.md"


def load_table(path):
    if not os.path.exists(path):
        return None
    return pd.read_csv(path)


def format_percent_columns(df):
    df = df.copy()

    for col in df.columns:
        if "percent" in col.lower():
            df[col] = df[col].round(2)

    for col in df.columns:
        if "return" in col.lower() and "percent" not in col.lower():
            if pd.api.types.is_numeric_dtype(df[col]):
                df[col] = df[col].round(4)

    for col in df.columns:
        if "price" in col.lower():
            if pd.api.types.is_numeric_dtype(df[col]):
                df[col] = df[col].round(2)

    return df


def generate_readme(top_n=20):
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    latest_rank = load_table(LATEST_RANK_FILE)
    backtest_summary = load_table(BACKTEST_SUMMARY_FILE)
    backtest_returns = load_table(BACKTEST_RETURNS_FILE)
    backtest_holdings = load_table(BACKTEST_HOLDINGS_FILE)

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
        latest_returns_table = format_percent_columns(backtest_returns.tail(12))
        latest_returns_markdown = latest_returns_table.to_markdown(index=False)
    else:
        latest_returns_markdown = "Backtest returns file not found."

    if backtest_holdings is not None:
        latest_holdings_table = backtest_holdings.tail(12)
        latest_holdings_markdown = latest_holdings_table.to_markdown(index=False)
    else:
        latest_holdings_markdown = "Backtest holdings file not found."

    readme_parts = [
        "# Nasdaq-100 Six-Month Mean Momentum Strategy",
        "",
        "This repository builds a rule-based momentum ranking and backtesting system for Nasdaq-100 stocks.",
        "",
        "The core idea is simple:",
        "",
        "> Every month, rank Nasdaq-100 stocks by their average monthly return over the past six months, buy the top three, and rebalance next month.",
        "",
        "In Chinese, I call this signal:",
        "",
        "**六月均值动量**",
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
        "## Backtest Summary",
        "",
        "The following table shows the summary statistics of the monthly mean momentum backtest.",
        "",
        summary_markdown,
        "",
        "---",
        "",
        "## Recent Monthly Backtest Returns",
        "",
        "The following table shows the most recent monthly strategy returns.",
        "",
        latest_returns_markdown,
        "",
        "The full monthly return history is saved in:",
        "",
        "```text",
        BACKTEST_RETURNS_FILE,
        "```",
        "",
        "---",
        "",
        "## Recent Monthly Holdings",
        "",
        "The following table shows the most recent monthly holdings selected by the strategy.",
        "",
        latest_holdings_markdown,
        "",
        "The full holding history is saved in:",
        "",
        "```text",
        BACKTEST_HOLDINGS_FILE,
        "```",
        "",
        "---",
        "",
        "## Strategy Logic",
        "",
        "For each stock in the Nasdaq-100 universe:",
        "",
        "1. Download adjusted historical price data.",
        "2. Resample prices to monthly frequency.",
        "3. Compute monthly returns.",
        "4. Calculate the average return over the past six months.",
        "5. Rank all stocks by this six-month mean momentum signal.",
        "6. Select the top three stocks.",
        "7. Rebalance monthly.",
        "",
        "The strategy does not use news, analyst reports, valuation metrics, or discretionary stock picking.",
        "",
        "It is a simple rule-based momentum strategy.",
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
