# Nasdaq-100 Six-Month Mean Momentum Strategy

This repository builds a rule-based momentum ranking and backtesting system for Nasdaq-100 stocks.

The core idea is simple:

> At the beginning of each month, rank Nasdaq-100 stocks by their average monthly return over the previous six months, buy the top three stocks, and hold them for the following month.


Last updated: **2026-05-30 04:42:31 UTC**

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

## Strategy Logic

At the beginning of each month:

1. Use only historical monthly returns from the previous six months.
2. Calculate the six-month average momentum signal for each Nasdaq-100 stock.
3. Rank all stocks by this six-month average momentum signal.
4. Select the top three stocks.
5. Hold these stocks for the following month.
6. Use the next month's realized return to calculate strategy performance.
7. Rebalance monthly.

The strategy does not use news, analyst reports, valuation metrics, market timing, or discretionary stock picking.

It is a simple rule-based momentum strategy.

---

## Backtest Summary

The following table shows the summary statistics of the monthly mean momentum backtest.

| strategy_name                            | data_start_date   | backtest_start_date   | start_date   | end_date   |   lookback_months |   top_n |   total_return_percent |   annualized_return_percent |   annualized_volatility_percent |   sharpe_ratio_without_risk_free_rate |   max_drawdown_percent |   win_rate_percent |   positive_months |   negative_months |   zero_months |   number_of_months |
|:-----------------------------------------|:------------------|:----------------------|:-------------|:-----------|------------------:|--------:|-----------------------:|----------------------------:|--------------------------------:|--------------------------------------:|-----------------------:|-------------------:|------------------:|------------------:|--------------:|-------------------:|
| Nasdaq-100 Top 3 Six-Month Mean Momentum | 2014-01-01        | 2016-02-01            | 2016-02-01   | 2026-05-29 |                 6 |       3 |                  41342 |                       79.18 |                           47.44 |                               1.66919 |                 -37.26 |               62.1 |                77 |                47 |             0 |                124 |

---

## Backtest Monthly Return Statistics

The following table summarizes the distribution of monthly strategy returns.

| metric                         |   value |
|:-------------------------------|--------:|
| Total months                   |  124    |
| Winning months                 |   77    |
| Losing months                  |   47    |
| Flat months                    |    0    |
| Win rate percent               |   62.1  |
| Average monthly return percent |    5.82 |
| Average winning month percent  |   13.48 |
| Average losing month percent   |   -6.74 |
| Best month percent             |   61.54 |
| Worst month percent            |  -22.21 |
| Monthly volatility percent     |   13.69 |
| Profit loss ratio              |    2    |

---

## Full Monthly Backtest Returns

The following table shows the full monthly strategy return history.

| signal_date   | ranking_date   | selected_stocks   | holding_start   | holding_end   |   portfolio_return |   portfolio_return_percent |   cumulative_return |   cumulative_return_percent |
|:--------------|:---------------|:------------------|:----------------|:--------------|-------------------:|---------------------------:|--------------------:|----------------------------:|
| 2016-01-31    | 2016-01-29     | NVDA,KLAC,MPWR    | 2016-02-01      | 2016-02-29    |             0.0132 |                       1.32 |              0.0132 |                        1.32 |
| 2016-02-29    | 2016-02-29     | NVDA,KLAC,LITE    | 2016-03-01      | 2016-03-31    |             0.0832 |                       8.32 |              0.0976 |                        9.76 |
| 2016-03-31    | 2016-03-31     | AMD,LITE,KLAC     | 2016-04-01      | 2016-04-29    |             0.0546 |                       5.46 |              0.1574 |                       15.74 |
| 2016-04-30    | 2016-04-29     | LITE,AMD,MELI     | 2016-05-02      | 2016-05-31    |             0.0984 |                       9.84 |              0.2713 |                       27.13 |
| 2016-05-31    | 2016-05-31     | AMD,NVDA,AMAT     | 2016-06-01      | 2016-06-30    |             0.0492 |                       4.92 |              0.3339 |                       33.39 |
| 2016-06-30    | 2016-06-30     | AMD,AXON,NVDA     | 2016-07-01      | 2016-07-29    |             0.2468 |                      24.68 |              0.6631 |                       66.31 |
| 2016-07-31    | 2016-07-29     | AMD,NVDA,AXON     | 2016-08-01      | 2016-08-31    |             0.0421 |                       4.21 |              0.7332 |                       73.32 |
| 2016-08-31    | 2016-08-31     | AMD,NVDA,SHOP     | 2016-09-01      | 2016-09-30    |             0.0268 |                       2.68 |              0.7797 |                       77.97 |
| 2016-09-30    | 2016-09-30     | AMD,NVDA,MU       | 2016-10-03      | 2016-10-31    |             0.0159 |                       1.59 |              0.808  |                       80.8  |
| 2016-10-31    | 2016-10-31     | AMD,NVDA,STX      | 2016-11-01      | 2016-11-30    |             0.2612 |                      26.12 |              1.2802 |                      128.02 |
| 2016-11-30    | 2016-11-30     | AMD,NVDA,STX      | 2016-12-01      | 2016-12-30    |             0.1958 |                      19.58 |              1.7267 |                      172.67 |
| 2016-12-31    | 2016-12-30     | NVDA,AMD,LITE     | 2017-01-03      | 2017-01-31    |            -0.0017 |                      -0.17 |              1.7221 |                      172.21 |
| 2017-01-31    | 2017-01-31     | NVDA,MU,WDC       | 2017-02-01      | 2017-02-28    |            -0.0633 |                      -6.33 |              1.5497 |                      154.97 |
| 2017-02-28    | 2017-02-28     | AMD,CSX,WDC       | 2017-03-01      | 2017-03-31    |            -0.007  |                      -0.7  |              1.5318 |                      153.18 |
| 2017-03-31    | 2017-03-31     | AMD,MU,NVDA       | 2017-04-03      | 2017-04-28    |            -0.0543 |                      -5.43 |              1.3942 |                      139.42 |
| 2017-04-30    | 2017-04-28     | AMD,SHOP,CSX      | 2017-05-01      | 2017-05-31    |             0.022  |                       2.2  |              1.4468 |                      144.68 |
| 2017-05-31    | 2017-05-31     | SHOP,TSLA,MELI    | 2017-06-01      | 2017-06-30    |            -0.0374 |                      -3.74 |              1.3551 |                      135.51 |
| 2017-06-30    | 2017-06-30     | ALNY,SHOP,VRTX    | 2017-07-03      | 2017-07-31    |             0.0903 |                       9.03 |              1.5677 |                      156.77 |
| 2017-07-31    | 2017-07-31     | ALNY,SHOP,VRTX    | 2017-08-01      | 2017-08-31    |             0.0567 |                       5.67 |              1.7133 |                      171.33 |
| 2017-08-31    | 2017-08-31     | SHOP,VRTX,TTWO    | 2017-09-01      | 2017-09-29    |             0.018  |                       1.8  |              1.7622 |                      176.22 |
| 2017-09-30    | 2017-09-29     | INSM,ALNY,TTWO    | 2017-10-02      | 2017-10-31    |            -0.0169 |                      -1.69 |              1.7154 |                      171.54 |
| 2017-10-31    | 2017-10-31     | INSM,ALNY,NVDA    | 2017-11-01      | 2017-11-30    |             0.0756 |                       7.56 |              1.9206 |                      192.06 |
| 2017-11-30    | 2017-11-30     | INSM,ALNY,TTWO    | 2017-12-01      | 2017-12-29    |            -0.0257 |                      -2.57 |              1.8455 |                      184.55 |
| 2017-12-31    | 2017-12-29     | INSM,ALNY,TTWO    | 2018-01-02      | 2018-01-31    |            -0.0361 |                      -3.61 |              1.7428 |                      174.28 |
| 2018-01-31    | 2018-01-31     | INSM,STX,ALNY     | 2018-02-01      | 2018-02-28    |            -0.0575 |                      -5.75 |              1.585  |                      158.5  |
| 2018-02-28    | 2018-02-28     | INSM,STX,NFLX     | 2018-03-01      | 2018-03-29    |             0.0238 |                       2.38 |              1.6465 |                      164.65 |
| 2018-03-31    | 2018-03-29     | STX,AXON,NFLX     | 2018-04-02      | 2018-04-30    |             0.0602 |                       6.02 |              1.8057 |                      180.57 |
| 2018-04-30    | 2018-04-30     | AXON,DXCM,NFLX    | 2018-05-01      | 2018-05-31    |             0.2851 |                      28.51 |              2.6056 |                      260.56 |
| 2018-05-31    | 2018-05-31     | AXON,NFLX,DXCM    | 2018-06-01      | 2018-06-29    |             0.0284 |                       2.84 |              2.708  |                      270.8  |
| 2018-06-30    | 2018-06-29     | AXON,NFLX,DXCM    | 2018-07-02      | 2018-07-31    |            -0.044  |                      -4.4  |              2.5449 |                      254.49 |
| 2018-07-31    | 2018-07-31     | AXON,DXCM,AMD     | 2018-08-01      | 2018-08-31    |             0.2908 |                      29.08 |              3.5759 |                      357.59 |
| 2018-08-31    | 2018-08-31     | DXCM,AMD,AXON     | 2018-09-04      | 2018-09-28    |             0.0198 |                       1.98 |              3.6665 |                      366.65 |
| 2018-09-30    | 2018-09-28     | AMD,DXCM,AXON     | 2018-10-01      | 2018-10-31    |            -0.1682 |                     -16.82 |              2.8817 |                      288.17 |
| 2018-10-31    | 2018-10-31     | AMD,DXCM,AXON     | 2018-11-01      | 2018-11-30    |            -0.0953 |                      -9.53 |              2.5119 |                      251.19 |
| 2018-11-30    | 2018-11-30     | AMD,DXCM,ZS       | 2018-12-03      | 2018-12-31    |            -0.114  |                     -11.4  |              2.1115 |                      211.15 |
| 2018-12-31    | 2018-12-31     | AMD,DXCM,WDAY     | 2019-01-02      | 2019-01-31    |             0.2191 |                      21.91 |              2.7931 |                      279.31 |
| 2019-01-31    | 2019-01-31     | AMD,DXCM,PDD      | 2019-02-01      | 2019-02-28    |            -0.0078 |                      -0.78 |              2.7635 |                      276.35 |
| 2019-02-28    | 2019-02-28     | INSM,PDD,MELI     | 2019-03-01      | 2019-03-29    |            -0.0366 |                      -3.66 |              2.6256 |                      262.56 |
| 2019-03-31    | 2019-03-29     | INSM,ZS,MELI      | 2019-04-01      | 2019-04-30    |            -0.0178 |                      -1.78 |              2.5609 |                      256.09 |
| 2019-04-30    | 2019-04-30     | INSM,ZS,SHOP      | 2019-05-01      | 2019-05-31    |            -0.0037 |                      -0.37 |              2.5479 |                      254.79 |
| 2019-05-31    | 2019-05-31     | ZS,SHOP,INSM      | 2019-06-03      | 2019-06-28    |             0.1264 |                      12.64 |              2.9965 |                      299.65 |
| 2019-06-30    | 2019-06-28     | INSM,SHOP,MELI    | 2019-07-01      | 2019-07-31    |            -0.0339 |                      -3.39 |              2.8608 |                      286.08 |
| 2019-07-31    | 2019-07-31     | SHOP,ZS,MELI      | 2019-08-01      | 2019-08-30    |            -0.0386 |                      -3.86 |              2.7119 |                      271.19 |
| 2019-08-31    | 2019-08-30     | SHOP,QCOM,TTWO    | 2019-09-03      | 2019-09-30    |            -0.0709 |                      -7.09 |              2.4487 |                      244.87 |
| 2019-09-30    | 2019-09-30     | SHOP,QCOM,PDD     | 2019-10-01      | 2019-10-31    |             0.1051 |                      10.51 |              2.8111 |                      281.11 |
| 2019-10-31    | 2019-10-31     | PDD,TSLA,KLAC     | 2019-11-01      | 2019-11-29    |            -0.0418 |                      -4.18 |              2.6517 |                      265.17 |
| 2019-11-30    | 2019-11-29     | DXCM,PDD,LITE     | 2019-12-02      | 2019-12-31    |             0.0323 |                       3.23 |              2.7698 |                      276.98 |
| 2019-12-31    | 2019-12-31     | PDD,TSLA,ALNY     | 2020-01-02      | 2020-01-31    |             0.1197 |                      11.97 |              3.221  |                      322.1  |
| 2020-01-31    | 2020-01-31     | TSLA,PDD,DXCM     | 2020-02-03      | 2020-02-28    |             0.0067 |                       0.67 |              3.2495 |                      324.95 |
| 2020-02-29    | 2020-02-28     | TSLA,DXCM,NVDA    | 2020-03-02      | 2020-03-31    |            -0.1331 |                     -13.31 |              2.6838 |                      268.38 |
| 2020-03-31    | 2020-03-31     | TSLA,DXCM,REGN    | 2020-04-01      | 2020-04-30    |             0.3327 |                      33.27 |              3.9092 |                      390.92 |
| 2020-04-30    | 2020-04-30     | TSLA,DXCM,SHOP    | 2020-05-01      | 2020-05-29    |             0.1778 |                      17.78 |              4.7819 |                      478.19 |
| 2020-05-31    | 2020-05-29     | TSLA,SHOP,ZS      | 2020-06-01      | 2020-06-30    |             0.1501 |                      15.01 |              5.6495 |                      564.95 |
| 2020-06-30    | 2020-06-30     | TSLA,DDOG,SHOP    | 2020-07-01      | 2020-07-31    |             0.1117 |                      11.17 |              6.3926 |                      639.26 |
| 2020-07-31    | 2020-07-31     | PDD,TSLA,ZS       | 2020-08-03      | 2020-08-31    |             0.2284 |                      22.84 |              8.081  |                      808.1  |
| 2020-08-31    | 2020-08-31     | TSLA,ZS,PDD       | 2020-09-01      | 2020-09-30    |            -0.1341 |                     -13.41 |              6.8628 |                      686.28 |
| 2020-09-30    | 2020-09-30     | TSLA,DDOG,SHOP    | 2020-10-01      | 2020-10-30    |            -0.1266 |                     -12.66 |              5.8675 |                      586.75 |
| 2020-10-31    | 2020-10-30     | TSLA,DDOG,MELI    | 2020-11-02      | 2020-11-30    |             0.2715 |                      27.15 |              7.7323 |                      773.23 |
| 2020-11-30    | 2020-11-30     | TSLA,MSTR,PDD     | 2020-12-01      | 2020-12-31    |             0.2357 |                      23.57 |              9.7909 |                      979.09 |
| 2020-12-31    | 2020-12-31     | MSTR,TSLA,PDD     | 2021-01-04      | 2021-01-29    |             0.1776 |                      17.76 |             11.707  |                     1170.7  |
| 2021-01-31    | 2021-01-29     | MSTR,TSLA,WBD     | 2021-02-01      | 2021-02-26    |             0.082  |                       8.2  |             12.7487 |                     1274.87 |
| 2021-02-28    | 2021-02-26     | MSTR,WBD,PDD      | 2021-03-01      | 2021-03-31    |            -0.2221 |                     -22.21 |              9.6953 |                      969.53 |
| 2021-03-31    | 2021-03-31     | MSTR,PLTR,FANG    | 2021-04-01      | 2021-04-30    |            -0.0203 |                      -2.03 |              9.4779 |                      947.79 |
| 2021-04-30    | 2021-04-30     | MSTR,PLTR,FANG    | 2021-05-03      | 2021-05-28    |            -0.0908 |                      -9.08 |              8.5262 |                      852.62 |
| 2021-05-31    | 2021-05-28     | FANG,FTNT,WDC     | 2021-06-01      | 2021-06-30    |             0.0447 |                       4.47 |              8.9517 |                      895.17 |
| 2021-06-30    | 2021-06-30     | MSTR,FANG,AMAT    | 2021-07-01      | 2021-07-30    |            -0.0831 |                      -8.31 |              8.1243 |                      812.43 |
| 2021-07-31    | 2021-07-30     | FTNT,NVDA,GOOG    | 2021-08-02      | 2021-08-31    |             0.1035 |                      10.35 |              9.0687 |                      906.87 |
| 2021-08-31    | 2021-08-31     | FTNT,NVDA,REGN    | 2021-09-01      | 2021-09-30    |            -0.0805 |                      -8.05 |              8.2584 |                      825.84 |
| 2021-09-30    | 2021-09-30     | DDOG,FTNT,NVDA    | 2021-10-01      | 2021-10-29    |             0.1719 |                      17.19 |              9.8503 |                      985.03 |
| 2021-10-31    | 2021-10-29     | DDOG,APP,NVDA     | 2021-11-01      | 2021-11-30    |             0.0867 |                       8.67 |             10.7914 |                     1079.14 |
| 2021-11-30    | 2021-11-30     | NVDA,AMD,DDOG     | 2021-12-01      | 2021-12-31    |            -0.0056 |                      -0.56 |             10.7254 |                     1072.54 |
| 2021-12-31    | 2021-12-31     | DDOG,TSLA,AMD     | 2022-01-03      | 2022-01-31    |            -0.189  |                     -18.9  |              8.5094 |                      850.94 |
| 2022-01-31    | 2022-01-31     | FANG,TSLA,DDOG    | 2022-02-01      | 2022-02-28    |             0.0285 |                       2.85 |              8.7804 |                      878.04 |
| 2022-02-28    | 2022-02-28     | FANG,BKR,PANW     | 2022-03-01      | 2022-03-31    |             0.1234 |                      12.34 |              9.9878 |                      998.78 |
| 2022-03-31    | 2022-03-31     | TSLA,BKR,FANG     | 2022-04-01      | 2022-04-29    |            -0.1445 |                     -14.45 |              8.3996 |                      839.96 |
| 2022-04-30    | 2022-04-29     | VRTX,BKR,EXC      | 2022-05-02      | 2022-05-31    |             0.0855 |                       8.55 |              9.2028 |                      920.28 |
| 2022-05-31    | 2022-05-31     | BKR,FANG,VRTX     | 2022-06-01      | 2022-06-30    |            -0.13   |                     -13    |              7.8767 |                      787.67 |
| 2022-06-30    | 2022-06-30     | BKR,VRTX,FANG     | 2022-07-01      | 2022-07-29    |            -0.0282 |                      -2.82 |              7.6259 |                      762.59 |
| 2022-07-31    | 2022-07-29     | CEG,TMUS,CDNS     | 2022-08-01      | 2022-08-31    |             0.064  |                       6.4  |              8.1779 |                      817.79 |
| 2022-08-31    | 2022-08-31     | CEG,PDD,ALNY      | 2022-09-01      | 2022-09-30    |            -0.0561 |                      -5.61 |              7.6635 |                      766.35 |
| 2022-09-30    | 2022-09-30     | PDD,CEG,ALNY      | 2022-10-03      | 2022-10-31    |             0.0067 |                       0.67 |              7.7218 |                      772.18 |
| 2022-10-31    | 2022-10-31     | ALNY,CEG,NFLX     | 2022-11-01      | 2022-11-30    |             0.0361 |                       3.61 |              8.0369 |                      803.69 |
| 2022-11-30    | 2022-11-30     | PDD,AXON,ALNY     | 2022-12-01      | 2022-12-30    |            -0.0176 |                      -1.76 |              7.8776 |                      787.76 |
| 2022-12-31    | 2022-12-30     | AXON,NFLX,ALNY    | 2023-01-03      | 2023-01-31    |             0.1102 |                      11.02 |              8.8559 |                      885.59 |
| 2023-01-31    | 2023-01-31     | PDD,AXON,ALNY     | 2023-02-01      | 2023-02-28    |            -0.0957 |                      -9.57 |              7.9125 |                      791.25 |
| 2023-02-28    | 2023-02-28     | AXON,NVDA,MSTR    | 2023-03-01      | 2023-03-31    |             0.1248 |                      12.48 |              9.0251 |                      902.51 |
| 2023-03-31    | 2023-03-31     | NVDA,AXON,SHOP    | 2023-04-03      | 2023-04-28    |            -0.0216 |                      -2.16 |              8.8082 |                      880.82 |
| 2023-04-30    | 2023-04-28     | META,NVDA,MSTR    | 2023-05-01      | 2023-05-31    |             0.1261 |                      12.61 |             10.0448 |                     1004.48 |
| 2023-05-31    | 2023-05-31     | PLTR,NVDA,META    | 2023-06-01      | 2023-06-30    |             0.0569 |                       5.69 |             10.6737 |                     1067.37 |
| 2023-06-30    | 2023-06-30     | NVDA,PLTR,MSTR    | 2023-07-03      | 2023-07-31    |             0.1797 |                      17.97 |             12.7712 |                     1277.12 |
| 2023-07-31    | 2023-07-31     | PLTR,APP,NVDA     | 2023-08-01      | 2023-08-31    |             0.0619 |                       6.19 |             13.6238 |                     1362.38 |
| 2023-08-31    | 2023-08-31     | APP,PLTR,NVDA     | 2023-09-01      | 2023-09-29    |            -0.0413 |                      -4.13 |             13.0195 |                     1301.95 |
| 2023-09-30    | 2023-09-29     | APP,PLTR,NVDA     | 2023-10-02      | 2023-10-31    |            -0.0882 |                      -8.82 |             11.7826 |                     1178.26 |
| 2023-10-31    | 2023-10-31     | PLTR,APP,ZS       | 2023-11-01      | 2023-11-30    |             0.2087 |                      20.87 |             14.4501 |                     1445.01 |
| 2023-11-30    | 2023-11-30     | PDD,MSTR,APP      | 2023-12-01      | 2023-12-29    |             0.082  |                       8.2  |             15.7168 |                     1571.68 |
| 2023-12-31    | 2023-12-29     | PDD,MSTR,CRWD     | 2024-01-02      | 2024-01-31    |            -0.0709 |                      -7.09 |             14.5321 |                     1453.21 |
| 2024-01-31    | 2024-01-31     | CRWD,PDD,AMD      | 2024-02-01      | 2024-02-29    |             0.0653 |                       6.53 |             15.5465 |                     1554.65 |
| 2024-02-29    | 2024-02-29     | MSTR,CRWD,PLTR    | 2024-03-01      | 2024-03-28    |             0.1737 |                      17.37 |             18.4212 |                     1842.12 |
| 2024-03-31    | 2024-03-28     | MSTR,ARM,NVDA     | 2024-04-01      | 2024-04-30    |            -0.1985 |                     -19.85 |             14.5652 |                     1456.52 |
| 2024-04-30    | 2024-04-30     | MSTR,ARM,NVDA     | 2024-05-01      | 2024-05-31    |             0.3559 |                      35.59 |             20.1042 |                     2010.42 |
| 2024-05-31    | 2024-05-31     | MSTR,INSM,ARM     | 2024-06-03      | 2024-06-28    |             0.1104 |                      11.04 |             22.4346 |                     2243.46 |
| 2024-06-30    | 2024-06-28     | MSTR,INSM,ARM     | 2024-07-01      | 2024-07-31    |             0.0621 |                       6.21 |             23.8893 |                     2388.93 |
| 2024-07-31    | 2024-07-31     | MSTR,INSM,ARM     | 2024-08-01      | 2024-08-30    |            -0.0051 |                      -0.51 |             23.7616 |                     2376.16 |
| 2024-08-31    | 2024-08-30     | INSM,ALNY,MSTR    | 2024-09-03      | 2024-09-30    |             0.1526 |                      15.26 |             27.5407 |                     2754.07 |
| 2024-09-30    | 2024-09-30     | INSM,ALNY,APP     | 2024-10-01      | 2024-10-31    |             0.0618 |                       6.18 |             29.3043 |                     2930.43 |
| 2024-10-31    | 2024-10-31     | INSM,MSTR,APP     | 2024-11-01      | 2024-11-29    |             0.6154 |                      61.54 |             47.953  |                     4795.3  |
| 2024-11-30    | 2024-11-29     | APP,PLTR,MSTR     | 2024-12-02      | 2024-12-31    |            -0.0495 |                      -4.95 |             45.5303 |                     4553.03 |
| 2024-12-31    | 2024-12-31     | APP,PLTR,MSTR     | 2025-01-02      | 2025-01-31    |             0.0981 |                       9.81 |             50.0962 |                     5009.62 |
| 2025-01-31    | 2025-01-31     | APP,PLTR,MSTR     | 2025-02-03      | 2025-02-28    |            -0.1195 |                     -11.95 |             43.988  |                     4398.8  |
| 2025-02-28    | 2025-02-28     | APP,PLTR,MSTR     | 2025-03-03      | 2025-03-31    |            -0.018  |                      -1.8  |             43.1793 |                     4317.93 |
| 2025-03-31    | 2025-03-31     | APP,PLTR,MSTR     | 2025-04-01      | 2025-04-30    |             0.1978 |                      19.78 |             51.9183 |                     5191.83 |
| 2025-04-30    | 2025-04-30     | PLTR,APP,MSTR     | 2025-05-01      | 2025-05-30    |             0.1691 |                      16.91 |             60.8676 |                     6086.76 |
| 2025-05-31    | 2025-05-30     | PLTR,AVGO,CRWD    | 2025-06-02      | 2025-06-30    |             0.0687 |                       6.87 |             65.1209 |                     6512.09 |
| 2025-06-30    | 2025-06-30     | PLTR,STX,ZS       | 2025-07-01      | 2025-07-31    |             0.0745 |                       7.45 |             70.046  |                     7004.6  |
| 2025-07-31    | 2025-07-31     | PLTR,STX,WDC      | 2025-08-01      | 2025-08-29    |             0.0489 |                       4.89 |             73.519  |                     7351.9  |
| 2025-08-31    | 2025-08-29     | LITE,PLTR,ALNY    | 2025-09-02      | 2025-09-30    |             0.1363 |                      13.63 |             83.6752 |                     8367.52 |
| 2025-09-30    | 2025-09-30     | SNDK,WDC,APP      | 2025-10-01      | 2025-10-31    |             0.2337 |                      23.37 |            103.465  |                    10346.5  |
| 2025-10-31    | 2025-10-31     | SNDK,WDC,LITE     | 2025-11-03      | 2025-11-28    |             0.2471 |                      24.71 |            129.283  |                    12928.3  |
| 2025-11-30    | 2025-11-28     | SNDK,LITE,WDC     | 2025-12-01      | 2025-12-31    |             0.1143 |                      11.43 |            144.18   |                    14418    |
| 2025-12-31    | 2025-12-31     | SNDK,LITE,WDC     | 2026-01-02      | 2026-01-30    |             0.4805 |                      48.05 |            213.944  |                    21394.4  |
| 2026-01-31    | 2026-01-30     | SNDK,MU,LITE      | 2026-02-02      | 2026-02-27    |             0.1841 |                      18.41 |            253.519  |                    25351.9  |
| 2026-02-28    | 2026-02-27     | SNDK,LITE,WDC     | 2026-03-02      | 2026-03-31    |            -0.0248 |                      -2.48 |            247.198  |                    24719.8  |
| 2026-03-31    | 2026-03-31     | SNDK,LITE,WDC     | 2026-04-01      | 2026-04-30    |             0.4075 |                      40.75 |            348.328  |                    34832.8  |
| 2026-04-30    | 2026-04-30     | SNDK,LITE,WDC     | 2026-05-01      | 2026-05-29    |             0.1863 |                      18.63 |            413.42   |                    41342    |

The full monthly return history is saved in:

```text
nasdaq100_mean_momentum_backtest_returns.csv
```

---

## Market Regime Filter Analysis

This additional section studies how the strategy changes when a Nasdaq market regime filter is added.

The original backtest above is kept unchanged. In the regime-filtered version, the same six-month mean momentum signal is still used to select the top three stocks, but trades are executed only when the Nasdaq market index is classified as being in a bull market.

When the Nasdaq market is classified as a bear market, the strategy stays in cash for the following month and records a 0% return.

The market regime is determined using only information available up to each ranking date, so the regime filter does not use future returns.

---

## Market Regime Filter Logic

At each ranking date:

1. Calculate the Nasdaq market index trend using historical index data.
2. Classify the month as a bull market if the index price is above its historical moving average.
3. If the month is a bull market, hold the selected top-three momentum stocks for the following month.
4. If the month is a bear market, stay in cash for the following month.
5. Compare the filtered strategy with the original strategy to evaluate whether the regime filter improves risk-adjusted performance.

---

## Strategy Comparison: Original vs Market Regime Filter

The following table compares the original strategy with the market-regime-filtered version.

| metric                              |   original_strategy |   with_market_regime_filter |    difference |
|:------------------------------------|--------------------:|----------------------------:|--------------:|
| total_return_percent                |         41342       |                 11462.3     | -29879.6      |
| annualized_return_percent           |            79.1846  |                    58.3615  |    -20.8231   |
| annualized_volatility_percent       |            47.439   |                    43.4326  |     -4.00637  |
| sharpe_ratio_without_risk_free_rate |             1.66919 |                     1.34372 |     -0.325463 |
| max_drawdown_percent                |           -37.2601  |                   -37.4552  |     -0.1951   |
| win_rate_percent                    |            62.0968  |                    49.1935  |    -12.9032   |
| number_of_months                    |           124       |                   124       |      0        |

---

## Market Regime Backtest Summary

The following table shows the summary statistics of the strategy after adding the Nasdaq market regime filter.

| strategy_name                                                      | data_start_date   | backtest_start_date   | market_index_ticker   |   market_trend_months | start_date   | end_date   |   lookback_months |   top_n |   bull_market_months |   bear_market_months |   trading_months |   cash_months |   bull_market_average_monthly_return_percent |   bear_market_average_monthly_return_percent |   total_return_percent |   annualized_return_percent |   annualized_volatility_percent |   sharpe_ratio_without_risk_free_rate |   max_drawdown_percent |   win_rate_percent |   positive_months |   negative_months |   zero_months |   number_of_months |
|:-------------------------------------------------------------------|:------------------|:----------------------|:----------------------|----------------------:|:-------------|:-----------|------------------:|--------:|---------------------:|---------------------:|-----------------:|--------------:|---------------------------------------------:|---------------------------------------------:|-----------------------:|----------------------------:|--------------------------------:|--------------------------------------:|-----------------------:|-------------------:|------------------:|------------------:|--------------:|-------------------:|
| Nasdaq-100 Top 3 Six-Month Mean Momentum With Market Regime Filter | 2014-01-01        | 2016-02-01            | QQQ                   |                    10 | 2016-02-01   | 2026-05-29 |                 6 |       3 |                  100 |                   24 |              100 |            24 |                                          5.7 |                                            0 |                11462.3 |                       58.36 |                           43.43 |                               1.34372 |                 -37.46 |              49.19 |                61 |                39 |            24 |                124 |

---

## Market Regime Monthly Return Statistics

The following table summarizes the distribution of monthly strategy returns after applying the market regime filter.

| metric                         |   value |
|:-------------------------------|--------:|
| Total months                   |  124    |
| Winning months                 |   61    |
| Losing months                  |   39    |
| Flat months                    |   24    |
| Win rate percent               |   49.19 |
| Average monthly return percent |    4.6  |
| Average winning month percent  |   13.57 |
| Average losing month percent   |   -6.6  |
| Best month percent             |   61.54 |
| Worst month percent            |  -22.21 |
| Monthly volatility percent     |   12.54 |
| Profit loss ratio              |    2.06 |

---

## Full Market Regime Backtest Returns

The following table shows the full monthly strategy return history with the market regime filter.

| signal_date   | ranking_date   | market_regime   | is_bull_market   |   market_index_price |   market_index_ma | selected_stocks   | holding_start   | holding_end   |   portfolio_return |   portfolio_return_percent |   cumulative_return |   cumulative_return_percent |
|:--------------|:---------------|:----------------|:-----------------|---------------------:|------------------:|:------------------|:----------------|:--------------|-------------------:|---------------------------:|--------------------:|----------------------------:|
| 2016-01-31    | 2016-01-29     | Bear Market     | False            |                96.73 |            100.48 | CASH              | 2016-02-01      | 2016-02-29    |             0      |                       0    |              0      |                        0    |
| 2016-02-29    | 2016-02-29     | Bear Market     | False            |                95.21 |            100.08 | CASH              | 2016-03-01      | 2016-03-31    |             0      |                       0    |              0      |                        0    |
| 2016-03-31    | 2016-03-31     | Bull Market     | True             |               101.74 |            100.11 | AMD,LITE,KLAC     | 2016-04-01      | 2016-04-29    |             0.0546 |                       5.46 |              0.0546 |                        5.46 |
| 2016-04-30    | 2016-04-29     | Bear Market     | False            |                98.5  |            100.07 | CASH              | 2016-05-02      | 2016-05-31    |             0      |                       0    |              0.0546 |                        5.46 |
| 2016-05-31    | 2016-05-31     | Bull Market     | True             |               102.8  |            100    | AMD,NVDA,AMAT     | 2016-06-01      | 2016-06-30    |             0.0492 |                       4.92 |              0.1065 |                       10.65 |
| 2016-06-30    | 2016-06-30     | Bull Market     | True             |               100.46 |            100.41 | AMD,AXON,NVDA     | 2016-07-01      | 2016-07-29    |             0.2468 |                      24.68 |              0.3795 |                       37.95 |
| 2016-07-31    | 2016-07-29     | Bull Market     | True             |               107.64 |            101.75 | AMD,NVDA,AXON     | 2016-08-01      | 2016-08-31    |             0.0421 |                       4.21 |              0.4377 |                       43.77 |
| 2016-08-31    | 2016-08-31     | Bull Market     | True             |               108.77 |            102.14 | AMD,NVDA,SHOP     | 2016-09-01      | 2016-09-30    |             0.0268 |                       2.68 |              0.4762 |                       47.62 |
| 2016-09-30    | 2016-09-30     | Bull Market     | True             |               111.18 |            102.7  | AMD,NVDA,MU       | 2016-10-03      | 2016-10-31    |             0.0159 |                       1.59 |              0.4997 |                       49.97 |
| 2016-10-31    | 2016-10-31     | Bull Market     | True             |               109.56 |            103.26 | AMD,NVDA,STX      | 2016-11-01      | 2016-11-30    |             0.2612 |                      26.12 |              0.8914 |                       89.14 |
| 2016-11-30    | 2016-11-30     | Bull Market     | True             |               110.04 |            104.59 | AMD,NVDA,STX      | 2016-12-01      | 2016-12-30    |             0.1958 |                      19.58 |              1.2618 |                      126.18 |
| 2016-12-31    | 2016-12-30     | Bull Market     | True             |               111.28 |            106.2  | NVDA,AMD,LITE     | 2017-01-03      | 2017-01-31    |            -0.0017 |                      -0.17 |              1.258  |                      125.8  |
| 2017-01-31    | 2017-01-31     | Bull Market     | True             |               117.01 |            107.72 | NVDA,MU,WDC       | 2017-02-01      | 2017-02-28    |            -0.0633 |                      -6.33 |              1.115  |                      111.5  |
| 2017-02-28    | 2017-02-28     | Bull Market     | True             |               122.12 |            110.09 | AMD,CSX,WDC       | 2017-03-01      | 2017-03-31    |            -0.007  |                      -0.7  |              1.1001 |                      110.01 |
| 2017-03-31    | 2017-03-31     | Bull Market     | True             |               124.6  |            112.27 | AMD,MU,NVDA       | 2017-04-03      | 2017-04-28    |            -0.0543 |                      -5.43 |              0.986  |                       98.6  |
| 2017-04-30    | 2017-04-28     | Bull Market     | True             |               128    |            115.02 | AMD,SHOP,CSX      | 2017-05-01      | 2017-05-31    |             0.022  |                       2.2  |              1.0296 |                      102.96 |
| 2017-05-31    | 2017-05-31     | Bull Market     | True             |               132.99 |            117.56 | SHOP,TSLA,MELI    | 2017-06-01      | 2017-06-30    |            -0.0374 |                      -3.74 |              0.9536 |                       95.36 |
| 2017-06-30    | 2017-06-30     | Bull Market     | True             |               129.9  |            119.67 | ALNY,SHOP,VRTX    | 2017-07-03      | 2017-07-31    |             0.0903 |                       9.03 |              1.1299 |                      112.99 |
| 2017-07-31    | 2017-07-31     | Bull Market     | True             |               135.18 |            122.07 | ALNY,SHOP,VRTX    | 2017-08-01      | 2017-08-31    |             0.0567 |                       5.67 |              1.2507 |                      125.07 |
| 2017-08-31    | 2017-08-31     | Bull Market     | True             |               137.98 |            124.91 | SHOP,VRTX,TTWO    | 2017-09-01      | 2017-09-29    |             0.018  |                       1.8  |              1.2913 |                      129.13 |
| 2017-09-30    | 2017-09-29     | Bull Market     | True             |               137.57 |            127.66 | INSM,ALNY,TTWO    | 2017-10-02      | 2017-10-31    |            -0.0169 |                      -1.69 |              1.2525 |                      125.25 |
| 2017-10-31    | 2017-10-31     | Bull Market     | True             |               143.91 |            130.93 | INSM,ALNY,NVDA    | 2017-11-01      | 2017-11-30    |             0.0756 |                       7.56 |              1.4227 |                      142.27 |
| 2017-11-30    | 2017-11-30     | Bull Market     | True             |               146.75 |            133.9  | INSM,ALNY,TTWO    | 2017-12-01      | 2017-12-29    |            -0.0257 |                      -2.57 |              1.3604 |                      136.04 |
| 2017-12-31    | 2017-12-29     | Bull Market     | True             |               147.63 |            136.45 | INSM,ALNY,TTWO    | 2018-01-02      | 2018-01-31    |            -0.0361 |                      -3.61 |              1.2752 |                      127.52 |
| 2018-01-31    | 2018-01-31     | Bull Market     | True             |               160.56 |            140.05 | INSM,STX,ALNY     | 2018-02-01      | 2018-02-28    |            -0.0575 |                      -5.75 |              1.1443 |                      114.43 |
| 2018-02-28    | 2018-02-28     | Bull Market     | True             |               158.49 |            143.1  | INSM,STX,NFLX     | 2018-03-01      | 2018-03-29    |             0.0238 |                       2.38 |              1.1952 |                      119.52 |
| 2018-03-31    | 2018-03-29     | Bull Market     | True             |               152.02 |            145    | STX,AXON,NFLX     | 2018-04-02      | 2018-04-30    |             0.0602 |                       6.02 |              1.3273 |                      132.73 |
| 2018-04-30    | 2018-04-30     | Bull Market     | True             |               152.79 |            147.29 | AXON,DXCM,NFLX    | 2018-05-01      | 2018-05-31    |             0.2851 |                      28.51 |              1.9908 |                      199.08 |
| 2018-05-31    | 2018-05-31     | Bull Market     | True             |               161.46 |            149.92 | AXON,NFLX,DXCM    | 2018-06-01      | 2018-06-29    |             0.0284 |                       2.84 |              2.0758 |                      207.58 |
| 2018-06-30    | 2018-06-29     | Bull Market     | True             |               163.31 |            152.45 | AXON,NFLX,DXCM    | 2018-07-02      | 2018-07-31    |            -0.044  |                      -4.4  |              1.9405 |                      194.05 |
| 2018-07-31    | 2018-07-31     | Bull Market     | True             |               167.88 |            155.48 | AXON,DXCM,AMD     | 2018-08-01      | 2018-08-31    |             0.2908 |                      29.08 |              2.7957 |                      279.57 |
| 2018-08-31    | 2018-08-31     | Bull Market     | True             |               177.58 |            158.85 | DXCM,AMD,AXON     | 2018-09-04      | 2018-09-28    |             0.0198 |                       1.98 |              2.8709 |                      287.09 |
| 2018-09-30    | 2018-09-28     | Bull Market     | True             |               177.08 |            161.88 | AMD,DXCM,AXON     | 2018-10-01      | 2018-10-31    |            -0.1682 |                     -16.82 |              2.2199 |                      221.99 |
| 2018-10-31    | 2018-10-31     | Bear Market     | False            |               161.86 |            163.3  | CASH              | 2018-11-01      | 2018-11-30    |             0      |                       0    |              2.2199 |                      221.99 |
| 2018-11-30    | 2018-11-30     | Bear Market     | False            |               161.43 |            163.39 | CASH              | 2018-12-03      | 2018-12-31    |             0      |                       0    |              2.2199 |                      221.99 |
| 2018-12-31    | 2018-12-31     | Bear Market     | False            |               147.45 |            162.29 | CASH              | 2019-01-02      | 2019-01-31    |             0      |                       0    |              2.2199 |                      221.99 |
| 2019-01-31    | 2019-01-31     | Bear Market     | False            |               160.73 |            163.16 | CASH              | 2019-02-01      | 2019-02-28    |             0      |                       0    |              2.2199 |                      221.99 |
| 2019-02-28    | 2019-02-28     | Bull Market     | True             |               165.54 |            164.43 | INSM,PDD,MELI     | 2019-03-01      | 2019-03-29    |            -0.0366 |                      -3.66 |              2.102  |                      210.2  |
| 2019-03-31    | 2019-03-29     | Bull Market     | True             |               172.04 |            165.49 | INSM,ZS,MELI      | 2019-04-01      | 2019-04-30    |            -0.0178 |                      -1.78 |              2.0466 |                      204.66 |
| 2019-04-30    | 2019-04-30     | Bull Market     | True             |               181.5  |            167.31 | INSM,ZS,SHOP      | 2019-05-01      | 2019-05-31    |            -0.0037 |                      -0.37 |              2.0355 |                      203.55 |
| 2019-05-31    | 2019-05-31     | Bear Market     | False            |               166.57 |            167.18 | CASH              | 2019-06-03      | 2019-06-28    |             0      |                       0    |              2.0355 |                      203.55 |
| 2019-06-30    | 2019-06-28     | Bull Market     | True             |               179.21 |            167.34 | INSM,SHOP,MELI    | 2019-07-01      | 2019-07-31    |            -0.0339 |                      -3.39 |              1.9324 |                      193.24 |
| 2019-07-31    | 2019-07-31     | Bull Market     | True             |               183.4  |            167.97 | SHOP,ZS,MELI      | 2019-08-01      | 2019-08-30    |            -0.0386 |                      -3.86 |              1.8193 |                      181.93 |
| 2019-08-31    | 2019-08-30     | Bull Market     | True             |               179.91 |            169.78 | SHOP,QCOM,TTWO    | 2019-09-03      | 2019-09-30    |            -0.0709 |                      -7.09 |              1.6194 |                      161.94 |
| 2019-09-30    | 2019-09-30     | Bull Market     | True             |               181.57 |            171.79 | SHOP,QCOM,PDD     | 2019-10-01      | 2019-10-31    |             0.1051 |                      10.51 |              1.8947 |                      189.47 |
| 2019-10-31    | 2019-10-31     | Bull Market     | True             |               189.52 |            176    | PDD,TSLA,KLAC     | 2019-11-01      | 2019-11-29    |            -0.0418 |                      -4.18 |              1.7736 |                      177.36 |
| 2019-11-30    | 2019-11-29     | Bull Market     | True             |               197.23 |            179.65 | DXCM,PDD,LITE     | 2019-12-02      | 2019-12-31    |             0.0323 |                       3.23 |              1.8633 |                      186.33 |
| 2019-12-31    | 2019-12-31     | Bull Market     | True             |               204.9  |            183.59 | PDD,TSLA,ALNY     | 2020-01-02      | 2020-01-31    |             0.1197 |                      11.97 |              2.206  |                      220.6  |
| 2020-01-31    | 2020-01-31     | Bull Market     | True             |               211.12 |            187.49 | TSLA,PDD,DXCM     | 2020-02-03      | 2020-02-28    |             0.0067 |                       0.67 |              2.2276 |                      222.76 |
| 2020-02-29    | 2020-02-28     | Bull Market     | True             |               198.33 |            189.18 | TSLA,DXCM,NVDA    | 2020-03-02      | 2020-03-31    |            -0.1331 |                     -13.31 |              1.798  |                      179.8  |
| 2020-03-31    | 2020-03-31     | Bear Market     | False            |               183.88 |            190.91 | CASH              | 2020-04-01      | 2020-04-30    |             0      |                       0    |              1.798  |                      179.8  |
| 2020-04-30    | 2020-04-30     | Bull Market     | True             |               211.42 |            194.13 | TSLA,DXCM,SHOP    | 2020-05-01      | 2020-05-29    |             0.1778 |                      17.78 |              2.2953 |                      229.53 |
| 2020-05-31    | 2020-05-29     | Bull Market     | True             |               225.37 |            198.33 | TSLA,SHOP,ZS      | 2020-06-01      | 2020-06-30    |             0.1501 |                      15.01 |              2.7898 |                      278.98 |
| 2020-06-30    | 2020-06-30     | Bull Market     | True             |               239.54 |            204.29 | TSLA,DDOG,SHOP    | 2020-07-01      | 2020-07-31    |             0.1117 |                      11.17 |              3.2133 |                      321.33 |
| 2020-07-31    | 2020-07-31     | Bull Market     | True             |               257.14 |            211.85 | PDD,TSLA,ZS       | 2020-08-03      | 2020-08-31    |             0.2284 |                      22.84 |              4.1756 |                      417.56 |
| 2020-08-31    | 2020-08-31     | Bull Market     | True             |               285.28 |            221.42 | TSLA,ZS,PDD       | 2020-09-01      | 2020-09-30    |            -0.1341 |                     -13.41 |              3.4813 |                      348.13 |
| 2020-09-30    | 2020-09-30     | Bull Market     | True             |               268.8  |            228.58 | TSLA,DDOG,SHOP    | 2020-10-01      | 2020-10-30    |            -0.1266 |                     -12.66 |              2.914  |                      291.4  |
| 2020-10-31    | 2020-10-30     | Bull Market     | True             |               260.61 |            234.15 | TSLA,DDOG,MELI    | 2020-11-02      | 2020-11-30    |             0.2715 |                      27.15 |              3.9769 |                      397.69 |
| 2020-11-30    | 2020-11-30     | Bull Market     | True             |               289.87 |            242.02 | TSLA,MSTR,PDD     | 2020-12-01      | 2020-12-31    |             0.2357 |                      23.57 |              5.1502 |                      515.02 |
| 2020-12-31    | 2020-12-31     | Bull Market     | True             |               304.08 |            252.6  | MSTR,TSLA,PDD     | 2021-01-04      | 2021-01-29    |             0.1776 |                      17.76 |              6.2422 |                      624.22 |
| 2021-01-31    | 2021-01-29     | Bull Market     | True             |               304.87 |            264.7  | MSTR,TSLA,WBD     | 2021-02-01      | 2021-02-26    |             0.082  |                       8.2  |              6.8359 |                      683.59 |
| 2021-02-28    | 2021-02-26     | Bull Market     | True             |               304.47 |            274    | MSTR,WBD,PDD      | 2021-03-01      | 2021-03-31    |            -0.2221 |                     -22.21 |              5.0957 |                      509.57 |
| 2021-03-31    | 2021-03-31     | Bull Market     | True             |               309.69 |            282.44 | MSTR,PLTR,FANG    | 2021-04-01      | 2021-04-30    |            -0.0203 |                      -2.03 |              4.9718 |                      497.18 |
| 2021-04-30    | 2021-04-30     | Bull Market     | True             |               328    |            291.28 | MSTR,PLTR,FANG    | 2021-05-03      | 2021-05-28    |            -0.0908 |                      -9.08 |              4.4294 |                      442.94 |
| 2021-05-31    | 2021-05-28     | Bull Market     | True             |               324.06 |            297.97 | FANG,FTNT,WDC     | 2021-06-01      | 2021-06-30    |             0.0447 |                       4.47 |              4.6719 |                      467.19 |
| 2021-06-30    | 2021-06-30     | Bull Market     | True             |               344.35 |            303.88 | MSTR,FANG,AMAT    | 2021-07-01      | 2021-07-30    |            -0.0831 |                      -8.31 |              4.2003 |                      420.03 |
| 2021-07-31    | 2021-07-30     | Bull Market     | True             |               354.2  |            312.42 | FTNT,NVDA,GOOG    | 2021-08-02      | 2021-08-31    |             0.1035 |                      10.35 |              4.7385 |                      473.85 |
| 2021-08-31    | 2021-08-31     | Bull Market     | True             |               369.14 |            323.27 | FTNT,NVDA,REGN    | 2021-09-01      | 2021-09-30    |            -0.0805 |                      -8.05 |              4.2767 |                      427.67 |
| 2021-09-30    | 2021-09-30     | Bull Market     | True             |               348.16 |            329.1  | DDOG,FTNT,NVDA    | 2021-10-01      | 2021-10-29    |             0.1719 |                      17.19 |              5.184  |                      518.4  |
| 2021-10-31    | 2021-10-29     | Bull Market     | True             |               375.54 |            336.25 | DDOG,APP,NVDA     | 2021-11-01      | 2021-11-30    |             0.0867 |                       8.67 |              5.7204 |                      572.04 |
| 2021-11-30    | 2021-11-30     | Bull Market     | True             |               383.04 |            344.07 | NVDA,AMD,DDOG     | 2021-12-01      | 2021-12-31    |            -0.0056 |                      -0.56 |              5.6828 |                      568.28 |
| 2021-12-31    | 2021-12-31     | Bull Market     | True             |               387.46 |            352.36 | DDOG,TSLA,AMD     | 2022-01-03      | 2022-01-31    |            -0.189  |                     -18.9  |              4.4198 |                      441.98 |
| 2022-01-31    | 2022-01-31     | Bear Market     | False            |               353.57 |            356.75 | CASH              | 2022-02-01      | 2022-02-28    |             0      |                       0    |              4.4198 |                      441.98 |
| 2022-02-28    | 2022-02-28     | Bear Market     | False            |               337.74 |            357.73 | CASH              | 2022-03-01      | 2022-03-31    |             0      |                       0    |              4.4198 |                      441.98 |
| 2022-03-31    | 2022-03-31     | Bear Market     | False            |               353.51 |            360.67 | CASH              | 2022-04-01      | 2022-04-29    |             0      |                       0    |              4.4198 |                      441.98 |
| 2022-04-30    | 2022-04-29     | Bear Market     | False            |               305.44 |            356.78 | CASH              | 2022-05-02      | 2022-05-31    |             0      |                       0    |              4.4198 |                      441.98 |
| 2022-05-31    | 2022-05-31     | Bear Market     | False            |               300.6  |            351.42 | CASH              | 2022-06-01      | 2022-06-30    |             0      |                       0    |              4.4198 |                      441.98 |
| 2022-06-30    | 2022-06-30     | Bear Market     | False            |               273.82 |            341.89 | CASH              | 2022-07-01      | 2022-07-29    |             0      |                       0    |              4.4198 |                      441.98 |
| 2022-07-31    | 2022-07-29     | Bear Market     | False            |               308.19 |            337.89 | CASH              | 2022-08-01      | 2022-08-31    |             0      |                       0    |              4.4198 |                      441.98 |
| 2022-08-31    | 2022-08-31     | Bear Market     | False            |               292.37 |            329.57 | CASH              | 2022-09-01      | 2022-09-30    |             0      |                       0    |              4.4198 |                      441.98 |
| 2022-09-30    | 2022-09-30     | Bear Market     | False            |               261.57 |            317.43 | CASH              | 2022-10-03      | 2022-10-31    |             0      |                       0    |              4.4198 |                      441.98 |
| 2022-10-31    | 2022-10-31     | Bear Market     | False            |               272.03 |            305.88 | CASH              | 2022-11-01      | 2022-11-30    |             0      |                       0    |              4.4198 |                      441.98 |
| 2022-11-30    | 2022-11-30     | Bear Market     | False            |               287.11 |            299.24 | CASH              | 2022-12-01      | 2022-12-30    |             0      |                       0    |              4.4198 |                      441.98 |
| 2022-12-31    | 2022-12-30     | Bear Market     | False            |               261.23 |            291.59 | CASH              | 2023-01-03      | 2023-01-31    |             0      |                       0    |              4.4198 |                      441.98 |
| 2023-01-31    | 2023-01-31     | Bull Market     | True             |               289.04 |            285.14 | PDD,AXON,ALNY     | 2023-02-01      | 2023-02-28    |            -0.0957 |                      -9.57 |              3.901  |                      390.1  |
| 2023-02-28    | 2023-02-28     | Bull Market     | True             |               288    |            283.4  | AXON,NVDA,MSTR    | 2023-03-01      | 2023-03-31    |             0.1248 |                      12.48 |              4.5128 |                      451.28 |
| 2023-03-31    | 2023-03-31     | Bull Market     | True             |               315.34 |            284.87 | NVDA,AXON,SHOP    | 2023-04-03      | 2023-04-28    |            -0.0216 |                      -2.16 |              4.3935 |                      439.35 |
| 2023-04-30    | 2023-04-28     | Bull Market     | True             |               316.94 |            289.18 | META,NVDA,MSTR    | 2023-05-01      | 2023-05-31    |             0.1261 |                      12.61 |              5.0736 |                      507.36 |
| 2023-05-31    | 2023-05-31     | Bull Market     | True             |               341.92 |            292.56 | PLTR,NVDA,META    | 2023-06-01      | 2023-06-30    |             0.0569 |                       5.69 |              5.4194 |                      541.94 |
| 2023-06-30    | 2023-06-30     | Bull Market     | True             |               363.48 |            299.67 | NVDA,PLTR,MSTR    | 2023-07-03      | 2023-07-31    |             0.1797 |                      17.97 |              6.5728 |                      657.28 |
| 2023-07-31    | 2023-07-31     | Bull Market     | True             |               377.51 |            311.26 | PLTR,APP,NVDA     | 2023-08-01      | 2023-08-31    |             0.0619 |                       6.19 |              7.0416 |                      704.16 |
| 2023-08-31    | 2023-08-31     | Bull Market     | True             |               371.91 |            321.25 | APP,PLTR,NVDA     | 2023-09-01      | 2023-09-29    |            -0.0413 |                      -4.13 |              6.7093 |                      670.93 |
| 2023-09-30    | 2023-09-29     | Bull Market     | True             |               353.02 |            327.84 | APP,PLTR,NVDA     | 2023-10-02      | 2023-10-31    |            -0.0882 |                      -8.82 |              6.0292 |                      602.92 |
| 2023-10-31    | 2023-10-31     | Bull Market     | True             |               345.73 |            336.29 | PLTR,APP,ZS       | 2023-11-01      | 2023-11-30    |             0.2087 |                      20.87 |              7.496  |                      749.6  |
| 2023-11-30    | 2023-11-30     | Bull Market     | True             |               383.13 |            345.7  | PDD,MSTR,APP      | 2023-12-01      | 2023-12-29    |             0.082  |                       8.2  |              8.1926 |                      819.26 |
| 2023-12-31    | 2023-12-29     | Bull Market     | True             |               404.54 |            357.35 | PDD,MSTR,CRWD     | 2024-01-02      | 2024-01-31    |            -0.0709 |                      -7.09 |              7.5411 |                      754.11 |
| 2024-01-31    | 2024-01-31     | Bull Market     | True             |               411.9  |            367.01 | CRWD,PDD,AMD      | 2024-02-01      | 2024-02-29    |             0.0653 |                       6.53 |              8.0989 |                      809.89 |
| 2024-02-29    | 2024-02-29     | Bull Market     | True             |               433.66 |            378.68 | MSTR,CRWD,PLTR    | 2024-03-01      | 2024-03-28    |             0.1737 |                      17.37 |              9.6797 |                      967.97 |
| 2024-03-31    | 2024-03-28     | Bull Market     | True             |               439.19 |            388.41 | MSTR,ARM,NVDA     | 2024-04-01      | 2024-04-30    |            -0.1985 |                     -19.85 |              7.5593 |                      755.93 |
| 2024-04-30    | 2024-04-30     | Bull Market     | True             |               419.98 |            394.06 | MSTR,ARM,NVDA     | 2024-05-01      | 2024-05-31    |             0.3559 |                      35.59 |             10.6052 |                     1060.52 |
| 2024-05-31    | 2024-05-31     | Bull Market     | True             |               445.81 |            400.89 | MSTR,INSM,ARM     | 2024-06-03      | 2024-06-28    |             0.1104 |                      11.04 |             11.8867 |                     1188.67 |
| 2024-06-30    | 2024-06-28     | Bull Market     | True             |               474.66 |            411.16 | MSTR,INSM,ARM     | 2024-07-01      | 2024-07-31    |             0.0621 |                       6.21 |             12.6866 |                     1268.66 |
| 2024-07-31    | 2024-07-31     | Bull Market     | True             |               466.69 |            422.53 | MSTR,INSM,ARM     | 2024-08-01      | 2024-08-30    |            -0.0051 |                      -0.51 |             12.6164 |                     1261.64 |
| 2024-08-31    | 2024-08-30     | Bull Market     | True             |               471.85 |            435.14 | INSM,ALNY,MSTR    | 2024-09-03      | 2024-09-30    |             0.1526 |                      15.26 |             14.6946 |                     1469.46 |
| 2024-09-30    | 2024-09-30     | Bull Market     | True             |               484.21 |            445.25 | INSM,ALNY,APP     | 2024-10-01      | 2024-10-31    |             0.0618 |                       6.18 |             15.6644 |                     1566.44 |
| 2024-10-31    | 2024-10-31     | Bull Market     | True             |               480.03 |            452.8  | INSM,MSTR,APP     | 2024-11-01      | 2024-11-29    |             0.6154 |                      61.54 |             25.9193 |                     2591.93 |
| 2024-11-30    | 2024-11-29     | Bull Market     | True             |               505.71 |            462.18 | APP,PLTR,MSTR     | 2024-12-02      | 2024-12-31    |            -0.0495 |                      -4.95 |             24.587  |                     2458.7  |
| 2024-12-31    | 2024-12-31     | Bull Market     | True             |               508.01 |            469.61 | APP,PLTR,MSTR     | 2025-01-02      | 2025-01-31    |             0.0981 |                       9.81 |             27.0979 |                     2709.79 |
| 2025-01-31    | 2025-01-31     | Bull Market     | True             |               519    |            477.6  | APP,PLTR,MSTR     | 2025-02-03      | 2025-02-28    |            -0.1195 |                     -11.95 |             23.739  |                     2373.9  |
| 2025-02-28    | 2025-02-28     | Bull Market     | True             |               504.97 |            486.09 | APP,PLTR,MSTR     | 2025-03-03      | 2025-03-31    |            -0.018  |                      -1.8  |             23.2943 |                     2329.43 |
| 2025-03-31    | 2025-03-31     | Bear Market     | False            |               466.66 |            488.18 | CASH              | 2025-04-01      | 2025-04-30    |             0      |                       0    |             23.2943 |                     2329.43 |
| 2025-04-30    | 2025-04-30     | Bear Market     | False            |               473.18 |            488.03 | CASH              | 2025-05-01      | 2025-05-30    |             0      |                       0    |             23.2943 |                     2329.43 |
| 2025-05-31    | 2025-05-30     | Bull Market     | True             |               516.61 |            493.02 | PLTR,AVGO,CRWD    | 2025-06-02      | 2025-06-30    |             0.0687 |                       6.87 |             24.9644 |                     2496.44 |
| 2025-06-30    | 2025-06-30     | Bull Market     | True             |               549.6  |            500.8  | PLTR,STX,ZS       | 2025-07-01      | 2025-07-31    |             0.0745 |                       7.45 |             26.8984 |                     2689.84 |
| 2025-07-31    | 2025-07-31     | Bull Market     | True             |               562.92 |            508.67 | PLTR,STX,WDC      | 2025-08-01      | 2025-08-29    |             0.0489 |                       4.89 |             28.2622 |                     2826.22 |
| 2025-08-31    | 2025-08-29     | Bull Market     | True             |               568.29 |            517.5  | LITE,PLTR,ALNY    | 2025-09-02      | 2025-09-30    |             0.1363 |                      13.63 |             32.2504 |                     3225.04 |
| 2025-09-30    | 2025-09-30     | Bull Market     | True             |               598.84 |            526.81 | SNDK,WDC,APP      | 2025-10-01      | 2025-10-31    |             0.2337 |                      23.37 |             40.0215 |                     4002.15 |
| 2025-10-31    | 2025-10-31     | Bull Market     | True             |               627.47 |            538.75 | SNDK,WDC,LITE     | 2025-11-03      | 2025-11-28    |             0.2471 |                      24.71 |             50.1596 |                     5015.96 |
| 2025-11-30    | 2025-11-28     | Bull Market     | True             |               617.67 |            548.62 | SNDK,LITE,WDC     | 2025-12-01      | 2025-12-31    |             0.1143 |                      11.43 |             56.0095 |                     5600.95 |
| 2025-12-31    | 2025-12-31     | Bull Market     | True             |               613.54 |            559.48 | SNDK,LITE,WDC     | 2026-01-02      | 2026-01-30    |             0.4805 |                      48.05 |             83.4045 |                     8340.45 |
| 2026-01-31    | 2026-01-30     | Bull Market     | True             |               621.09 |            574.92 | SNDK,MU,LITE      | 2026-02-02      | 2026-02-27    |             0.1841 |                      18.41 |             98.9448 |                     9894.48 |
| 2026-02-28    | 2026-02-27     | Bull Market     | True             |               606.53 |            588.26 | SNDK,LITE,WDC     | 2026-03-02      | 2026-03-31    |            -0.0248 |                      -2.48 |             96.4628 |                     9646.28 |
| 2026-03-31    | 2026-03-31     | Bear Market     | False            |               577.18 |            594.31 | CASH              | 2026-04-01      | 2026-04-30    |             0      |                       0    |             96.4628 |                     9646.28 |
| 2026-04-30    | 2026-04-30     | Bull Market     | True             |               667.74 |            606.13 | SNDK,LITE,WDC     | 2026-05-01      | 2026-05-29    |             0.1863 |                      18.63 |            114.623  |                    11462.3  |

The full market regime return history is saved in:

```text
nasdaq100_mean_momentum_regime_backtest_returns.csv
```

---

## Files

| File | Description |
|---|---|
| `nasdaq100_six_month_momentum_rank.csv` | Latest Nasdaq-100 six-month mean momentum ranking |
| `nasdaq100_mean_momentum_backtest_summary.csv` | Backtest summary statistics |
| `nasdaq100_mean_momentum_backtest_returns.csv` | Monthly backtest return history |
| `nasdaq100_mean_momentum_backtest_holdings.csv` | Monthly strategy holdings |
| `nasdaq100_mean_momentum_regime_backtest_summary.csv` | Market regime filtered backtest summary statistics |
| `nasdaq100_mean_momentum_regime_backtest_returns.csv` | Market regime filtered monthly return history |
| `README.md` | Auto-generated project README |

---

## Disclaimer

This project is for educational and research purposes only.

It is not financial advice.

Momentum strategies can suffer from drawdowns, turnover costs, tax effects, slippage, survivorship bias, and regime changes.

Past performance does not guarantee future results.
