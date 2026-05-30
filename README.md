# Nasdaq-100 Six-Month Mean Momentum Strategy

This repository builds a rule-based momentum ranking and backtesting system for Nasdaq-100 stocks.

The core idea is simple:

> Every month, rank Nasdaq-100 stocks by their average monthly return over the past six months, buy the top three, and rebalance next month.

In Chinese, I call this signal:

**六月均值动量**

Last updated: **2026-05-30 01:59:50 UTC**

---

## Latest Nasdaq-100 Six-Month Momentum Ranking

The following table shows the latest Nasdaq-100 momentum ranking up to the most recent available trading date.

Top 20 stocks are shown below.

|   rank | Ticker   | start_date   | end_date   |   start_price |   end_price |   six_month_momentum |   six_month_momentum_percent |   trading_days |
|-------:|:---------|:-------------|:-----------|--------------:|------------:|---------------------:|-----------------------------:|---------------:|
|      1 | SNDK     | 2025-12-01   | 2026-05-29 |        210.17 |     1694.98 |             7.0648   |                       706.48 |            124 |
|      2 | MU       | 2025-12-01   | 2026-05-29 |        240.26 |      971    |             3.04142  |                       304.14 |            124 |
|      3 | STX      | 2025-12-01   | 2026-05-29 |        268.92 |      879.8  |             2.27155  |                       227.16 |            124 |
|      4 | WDC      | 2025-12-01   | 2026-05-29 |        163.33 |      531.21 |             2.25236  |                       225.24 |            124 |
|      5 | INTC     | 2025-12-01   | 2026-05-29 |         40.01 |      114.68 |             1.86628  |                       186.63 |            124 |
|      6 | LITE     | 2025-12-01   | 2026-05-29 |        317.93 |      854.96 |             1.68915  |                       168.91 |            124 |
|      7 | ARM      | 2025-12-01   | 2026-05-29 |        135.01 |      353.29 |             1.61677  |                       161.68 |            124 |
|      8 | AMD      | 2025-12-01   | 2026-05-29 |        219.76 |      516.1  |             1.34847  |                       134.85 |            124 |
|      9 | MRVL     | 2025-12-01   | 2026-05-29 |         90.99 |      205    |             1.25302  |                       125.3  |            124 |
|     10 | LRCX     | 2025-12-01   | 2026-05-29 |        154.35 |      318.18 |             1.06141  |                       106.14 |            124 |
|     11 | TXN      | 2025-12-01   | 2026-05-29 |        166.22 |      305.68 |             0.838954 |                        83.9  |            124 |
|     12 | MCHP     | 2025-12-01   | 2026-05-29 |         52.85 |       94.65 |             0.790851 |                        79.09 |            124 |
|     13 | AMAT     | 2025-12-01   | 2026-05-29 |        254.12 |      450.06 |             0.771076 |                        77.11 |            124 |
|     14 | MPWR     | 2025-12-01   | 2026-05-29 |        924.93 |     1566.21 |             0.693322 |                        69.33 |            124 |
|     15 | FTNT     | 2025-12-01   | 2026-05-29 |         81.82 |      137.97 |             0.686263 |                        68.63 |            124 |
|     16 | KLAC     | 2025-12-01   | 2026-05-29 |       1154.21 |     1921.71 |             0.664964 |                        66.5  |            124 |
|     17 | NXPI     | 2025-12-01   | 2026-05-29 |        197.58 |      321.35 |             0.626449 |                        62.64 |            124 |
|     18 | ODFL     | 2025-12-01   | 2026-05-29 |        139.2  |      225.15 |             0.617467 |                        61.75 |            124 |
|     19 | CSCO     | 2025-12-01   | 2026-05-29 |         75.23 |      120.42 |             0.600741 |                        60.07 |            124 |
|     20 | DDOG     | 2025-12-01   | 2026-05-29 |        157.9  |      247.35 |             0.566498 |                        56.65 |            124 |

The full ranking is saved in:

```text
nasdaq100_six_month_momentum_rank.csv
```

---

## Backtest Summary

The following table shows the summary statistics of the monthly mean momentum backtest.

| strategy_name                            | start_date   | end_date   |   lookback_months |   top_n |   total_return_percent |   annualized_return_percent |   annualized_volatility_percent |   sharpe_ratio_without_risk_free_rate |   max_drawdown_percent |   win_rate_percent |   number_of_months |
|:-----------------------------------------|:-------------|:-----------|------------------:|--------:|-----------------------:|----------------------------:|--------------------------------:|--------------------------------------:|-----------------------:|-------------------:|-------------------:|
| Nasdaq-100 Top 3 Six-Month Mean Momentum | 2016-07-31   | 2026-05-31 |                 6 |       3 |                75610.2 |                       96.24 |                           50.37 |                               1.91089 |                 -29.15 |              61.86 |                118 |

---

## Recent Monthly Backtest Returns

The following table shows the most recent monthly strategy returns.

| ranking_date   | holding_start   | holding_end   |   portfolio_return |   portfolio_return_percent |   number_of_stocks |   cumulative_return |   cumulative_return_percent |
|:---------------|:----------------|:--------------|-------------------:|---------------------------:|-------------------:|--------------------:|----------------------------:|
| 2025-05-31     | 2025-05-31      | 2025-06-30    |             0.0854 |                       8.54 |                  3 |             84.0043 |                     8400.43 |
| 2025-06-30     | 2025-06-30      | 2025-07-31    |             0.053  |                       5.3  |                  3 |             88.5112 |                     8851.12 |
| 2025-07-31     | 2025-07-31      | 2025-08-31    |             0.0256 |                       2.56 |                  3 |             90.8023 |                     9080.23 |
| 2025-08-31     | 2025-08-31      | 2025-09-30    |             0.1368 |                      13.68 |                  3 |            103.362  |                    10336.2  |
| 2025-09-30     | 2025-09-30      | 2025-10-31    |             0.3049 |                      30.49 |                  3 |            135.181  |                    13518.1  |
| 2025-10-31     | 2025-10-31      | 2025-11-30    |             0.2736 |                      27.36 |                  3 |            172.436  |                    17243.6  |
| 2025-11-30     | 2025-11-30      | 2025-12-31    |             0.0841 |                       8.41 |                  3 |            187.022  |                    18702.2  |
| 2025-12-31     | 2025-12-31      | 2026-01-31    |             0.6477 |                      64.77 |                  3 |            308.808  |                    30880.8  |
| 2026-01-31     | 2026-01-31      | 2026-02-28    |             0.2951 |                      29.51 |                  3 |            400.232  |                    40023.2  |
| 2026-02-28     | 2026-02-28      | 2026-03-31    |            -0.01   |                      -1    |                  3 |            396.239  |                    39623.9  |
| 2026-03-31     | 2026-03-31      | 2026-04-30    |             0.5387 |                      53.87 |                  3 |            610.251  |                    61025.1  |
| 2026-04-30     | 2026-04-30      | 2026-05-31    |             0.2386 |                      23.86 |                  3 |            756.102  |                    75610.2  |

The full monthly return history is saved in:

```text
nasdaq100_mean_momentum_backtest_returns.csv
```

---

## Recent Monthly Holdings

The following table shows the most recent monthly holdings selected by the strategy.

| ranking_date   | holding_start   | holding_end   | selected_stocks   |
|:---------------|:----------------|:--------------|:------------------|
| 2025-05-31     | 2025-05-31      | 2025-06-30    | PLTR,AVGO,CRWD    |
| 2025-06-30     | 2025-06-30      | 2025-07-31    | PLTR,STX,ZS       |
| 2025-07-31     | 2025-07-31      | 2025-08-31    | PLTR,STX,WDC      |
| 2025-08-31     | 2025-08-31      | 2025-09-30    | LITE,PLTR,ALNY    |
| 2025-09-30     | 2025-09-30      | 2025-10-31    | SNDK,WDC,APP      |
| 2025-10-31     | 2025-10-31      | 2025-11-30    | SNDK,WDC,LITE     |
| 2025-11-30     | 2025-11-30      | 2025-12-31    | SNDK,LITE,WDC     |
| 2025-12-31     | 2025-12-31      | 2026-01-31    | SNDK,LITE,WDC     |
| 2026-01-31     | 2026-01-31      | 2026-02-28    | SNDK,MU,LITE      |
| 2026-02-28     | 2026-02-28      | 2026-03-31    | SNDK,LITE,WDC     |
| 2026-03-31     | 2026-03-31      | 2026-04-30    | SNDK,LITE,WDC     |
| 2026-04-30     | 2026-04-30      | 2026-05-31    | SNDK,LITE,WDC     |

The full holding history is saved in:

```text
nasdaq100_mean_momentum_backtest_holdings.csv
```

---

## Strategy Logic

For each stock in the Nasdaq-100 universe:

1. Download adjusted historical price data.
2. Resample prices to monthly frequency.
3. Compute monthly returns.
4. Calculate the average return over the past six months.
5. Rank all stocks by this six-month mean momentum signal.
6. Select the top three stocks.
7. Rebalance monthly.

The strategy does not use news, analyst reports, valuation metrics, or discretionary stock picking.

It is a simple rule-based momentum strategy.

---

## Files

| File | Description |
|---|---|
| `nasdaq100_six_month_momentum_rank.csv` | Latest Nasdaq-100 six-month mean momentum ranking |
| `nasdaq100_mean_momentum_backtest_summary.csv` | Backtest summary statistics |
| `nasdaq100_mean_momentum_backtest_returns.csv` | Monthly backtest return history |
| `nasdaq100_mean_momentum_backtest_holdings.csv` | Monthly strategy holdings |
| `README.md` | Auto-generated project README |

---

## Disclaimer

This project is for educational and research purposes only.

It is not financial advice.

Momentum strategies can suffer from drawdowns, turnover costs, tax effects, slippage, survivorship bias, and regime changes.

Past performance does not guarantee future results.
