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

    readme = f"""# Nasdaq-100 Six-Month Mean Momentum Strategy

This repository builds a rule-based momentum ranking and backtesting system for Nasdaq-100 stocks.

The core idea is simple:

> Every month, rank Nasdaq-100 stocks by their average monthly return over the past six months, buy the top three, and rebalance next month.

In Chinese, I call this signal:

**六月均值动量**

Last updated: **{now}**

---

## Latest Nasdaq-100 Six-Month Momentum Ranking

The following table shows the latest Nasdaq-100 momentum ranking up to the most recent available trading date.

Top {top_n} stocks are shown below.

{latest_rank_markdown}

The full ranking is saved in:

```text
{LATEST_RANK_FILE}
