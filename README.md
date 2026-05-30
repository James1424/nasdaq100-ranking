# Nasdaq-100 Six-Month Mean Momentum Strategy

This repository builds a simple rule-based momentum ranking and backtesting system for Nasdaq-100 stocks.

The core idea is simple:

> Every month, rank Nasdaq-100 stocks by their average monthly return over the past six months, buy the top three, and rebalance next month.

In Chinese, I call this signal:

**六月均值动量**

---

## Core Idea

This strategy does not rely on:

- financial statement analysis
- news interpretation
- industry forecasting
- K-line pattern reading
- target prices
- manual stop-loss rules
- manual take-profit rules

Instead, it follows one predefined ranking rule.

For each Nasdaq-100 stock, calculate its monthly returns over the past six months:

```text
r1, r2, r3, r4, r5, r6
```

Then calculate the average:

```text
six_month_mean_momentum = (r1 + r2 + r3 + r4 + r5 + r6) / 6
```

Stocks are ranked from highest to lowest based on this value.

The top three stocks enter the portfolio.

If a stock remains in the top three next month, it stays.

If it drops out of the top three, it is replaced.

---

## Strategy Rule

The strategy follows this monthly process:

```text
1. At the end of each month, collect monthly adjusted closing prices.
2. Calculate each stock's monthly returns over the past six months.
3. Compute the average of those six monthly returns.
4. Rank all Nasdaq-100 stocks by six-month mean momentum.
5. Select the top three stocks.
6. Hold the selected stocks with equal weights for one month.
7. Repeat the process next month.
```

The rule can be summarized as:

```text
Rank decides everything.
```

---

## Backtest Setting

The backtest is designed as follows:

```text
Universe: Nasdaq-100 stocks
Signal: six-month mean momentum
Lookback window: 6 months
Selection: top 3 stocks
Weighting: equal weight
Rebalancing frequency: monthly
Holding period: 1 month
Backtest period: 2016-2026
```

The first six months are used to calculate the initial momentum signal, so the first investable portfolio starts only after enough monthly return history is available.

---

## Output Files

The project generates the following CSV files:

```text
nasdaq100_six_month_momentum_rank.csv
nasdaq100_mean_momentum_backtest_returns.csv
nasdaq100_mean_momentum_backtest_holdings.csv
nasdaq100_mean_momentum_backtest_summary.csv
```

---

## Latest Ranking File

```text
nasdaq100_six_month_momentum_rank.csv
```

This file contains the latest Nasdaq-100 momentum ranking.

Typical columns include:

| Column | Meaning |
|---|---|
| rank | Ranking position |
| Ticker | Stock ticker |
| start_date | Start date of the ranking window |
| end_date | End date of the ranking window |
| start_price | Adjusted closing price at the start date |
| end_price | Adjusted closing price at the end date |
| six_month_momentum | Six-month momentum value |
| six_month_momentum_percent | Six-month momentum in percentage form |
| trading_days | Number of trading days used |

---

## Backtest Returns File

```text
nasdaq100_mean_momentum_backtest_returns.csv
```

This file records the monthly portfolio return and cumulative return.

Typical columns include:

| Column | Meaning |
|---|---|
| ranking_date | Date when the ranking is calculated |
| holding_start | Start date of the holding period |
| holding_end | End date of the holding period |
| portfolio_return | Monthly portfolio return |
| portfolio_return_percent | Monthly portfolio return in percentage form |
| number_of_stocks | Number of stocks actually held |
| cumulative_return | Cumulative return |
| cumulative_return_percent | Cumulative return in percentage form |

---

## Backtest Holdings File

```text
nasdaq100_mean_momentum_backtest_holdings.csv
```

This file records the selected stocks at each monthly rebalance.

Typical columns include:

| Column | Meaning |
|---|---|
| ranking_date | Date when the ranking is calculated |
| holding_start | Start date of the holding period |
| holding_end | End date of the holding period |
| selected_stocks | Stocks selected by the strategy |

---

## Backtest Summary File

```text
nasdaq100_mean_momentum_backtest_summary.csv
```

This file summarizes the strategy performance.

Typical columns include:

| Column | Meaning |
|---|---|
| strategy_name | Name of the strategy |
| start_date | First holding period start date |
| end_date | Last holding period end date |
| lookback_months | Number of months used for momentum calculation |
| top_n | Number of selected stocks |
| total_return_percent | Total return over the full backtest |
| annualized_return_percent | Annualized return |
| annualized_volatility_percent | Annualized volatility |
| sharpe_ratio_without_risk_free_rate | Sharpe ratio without risk-free rate adjustment |
| max_drawdown_percent | Maximum drawdown |
| win_rate_percent | Percentage of positive-return months |
| number_of_months | Number of monthly holding periods |

---

## How to Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the latest ranking script:

```bash
python calculate_momentum_rank.py
```

Run the six-month mean momentum backtest:

```bash
python backtest_mean_momentum.py
```

After running the scripts, the CSV result files will be saved in the project root directory.

---

## Online Update with GitHub Actions

This repository can be updated online using GitHub Actions.

To run the workflow manually:

```text
Actions → Run Nasdaq100 Momentum Ranking → Run workflow
```

After the workflow finishes successfully, the ranking and backtest CSV files will be updated in the repository.

---

## Project Structure

```text
nasdaq100-ranking/
├── calculate_momentum_rank.py
├── backtest_mean_momentum.py
├── stock_database.py
├── update_readme.py
├── requirements.txt
├── README.md
├── nasdaq100_six_month_momentum_rank.csv
├── nasdaq100_mean_momentum_backtest_returns.csv
├── nasdaq100_mean_momentum_backtest_holdings.csv
├── nasdaq100_mean_momentum_backtest_summary.csv
└── .github/
    └── workflows/
        └── run-ranking.yml
```

---

## Data Source

Stock price data is downloaded using `yfinance`.

The strategy uses adjusted closing prices, which account for stock splits and dividends when available.

---

## Important Limitation

This backtest currently uses the available Nasdaq-100 stock universe from the data source.

This may introduce **survivorship bias**.

Survivorship bias means that the backtest may use today's successful Nasdaq-100 companies to test historical periods, while ignoring companies that were previously in the index but later removed.

As a result, the historical performance may look better than what a real investor could have achieved at the time.

A more rigorous version should use historical Nasdaq-100 constituent data for each month.

---

## Future Improvements

Possible future improvements include:

- adding historical Nasdaq-100 constituent data
- comparing the strategy with QQQ
- adding transaction costs
- adding slippage assumptions
- adding turnover statistics
- adding risk-free-rate-adjusted Sharpe ratio
- adding maximum drawdown charts
- adding cumulative return charts
- extending the framework to multiple asset pools

---

## Disclaimer

This project is for research and educational purposes only.

It is not financial advice.

The strategy result does not guarantee future performance.

Use the code and results at your own risk.
