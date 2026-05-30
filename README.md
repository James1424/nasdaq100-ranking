# Nasdaq-100 Six-Month Mean Momentum Strategy

This repository builds a rule-based momentum ranking and backtesting system for Nasdaq-100 stocks.

The core idea is simple:

> At the beginning of each month, rank Nasdaq-100 stocks by their average monthly return over the previous six months, buy the top three stocks, and hold them for the following month.


Last updated: **2026-05-30 04:27:43 UTC**

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
| Nasdaq-100 Top 3 Six-Month Mean Momentum | 2014-01-01        | 2016-02-01            | 2016-03-01   | 2026-05-29 |                 6 |       3 |                20117.3 |                      107.98 |                           50.61 |                               2.13367 |                 -48.12 |              63.22 |                55 |                32 |             0 |                 87 |

---

## Backtest Monthly Return Statistics

The following table summarizes the distribution of monthly strategy returns.

| metric                         |   value |
|:-------------------------------|--------:|
| Total months                   |   87    |
| Winning months                 |   55    |
| Losing months                  |   32    |
| Flat months                    |    0    |
| Win rate percent               |   63.22 |
| Average monthly return percent |    7.22 |
| Average winning month percent  |   15.04 |
| Average losing month percent   |   -6.22 |
| Best month percent             |   61.54 |
| Worst month percent            |  -18.9  |
| Monthly volatility percent     |   14.61 |
| Profit loss ratio              |    2.42 |

---

## Full Monthly Backtest Returns

The following table shows the full monthly strategy return history.

| ranking_date   | selected_stocks   | holding_start   | holding_end   |   portfolio_return |   portfolio_return_percent |   cumulative_return |   cumulative_return_percent |
|:---------------|:------------------|:----------------|:--------------|-------------------:|---------------------------:|--------------------:|----------------------------:|
| 2016-02-29     | NVDA,KLAC,LITE    | 2016-03-01      | 2016-03-31    |             0.0832 |                       8.32 |              0.0832 |                        8.32 |
| 2016-03-31     | AMD,LITE,KLAC     | 2016-04-01      | 2016-04-29    |             0.0546 |                       5.46 |              0.1423 |                       14.23 |
| 2016-05-31     | AMD,NVDA,AMAT     | 2016-06-01      | 2016-06-30    |             0.0492 |                       4.92 |              0.1986 |                       19.86 |
| 2016-06-30     | AMD,AXON,NVDA     | 2016-07-01      | 2016-07-29    |             0.2468 |                      24.68 |              0.4944 |                       49.44 |
| 2016-08-31     | AMD,NVDA,SHOP     | 2016-09-01      | 2016-09-30    |             0.0268 |                       2.68 |              0.5345 |                       53.45 |
| 2016-09-30     | AMD,NVDA,MU       | 2016-10-03      | 2016-10-31    |             0.0159 |                       1.59 |              0.5589 |                       55.89 |
| 2016-10-31     | AMD,NVDA,STX      | 2016-11-01      | 2016-11-30    |             0.2612 |                      26.12 |              0.966  |                       96.6  |
| 2016-11-30     | AMD,NVDA,STX      | 2016-12-01      | 2016-12-30    |             0.1958 |                      19.58 |              1.351  |                      135.1  |
| 2017-01-31     | NVDA,MU,WDC       | 2017-02-01      | 2017-02-28    |            -0.0633 |                      -6.33 |              1.2021 |                      120.21 |
| 2017-02-28     | AMD,CSX,WDC       | 2017-03-01      | 2017-03-31    |            -0.007  |                      -0.7  |              1.1866 |                      118.66 |
| 2017-03-31     | AMD,MU,NVDA       | 2017-04-03      | 2017-04-28    |            -0.0543 |                      -5.43 |              1.0678 |                      106.78 |
| 2017-05-31     | SHOP,TSLA,MELI    | 2017-06-01      | 2017-06-30    |            -0.0374 |                      -3.74 |              0.9903 |                       99.03 |
| 2017-06-30     | ALNY,SHOP,VRTX    | 2017-07-03      | 2017-07-31    |             0.0903 |                       9.03 |              1.17   |                      117    |
| 2017-07-31     | ALNY,SHOP,VRTX    | 2017-08-01      | 2017-08-31    |             0.0567 |                       5.67 |              1.293  |                      129.3  |
| 2017-08-31     | SHOP,VRTX,TTWO    | 2017-09-01      | 2017-09-29    |             0.018  |                       1.8  |              1.3344 |                      133.44 |
| 2017-10-31     | INSM,ALNY,NVDA    | 2017-11-01      | 2017-11-30    |             0.0756 |                       7.56 |              1.5108 |                      151.08 |
| 2017-11-30     | INSM,ALNY,TTWO    | 2017-12-01      | 2017-12-29    |            -0.0257 |                      -2.57 |              1.4462 |                      144.62 |
| 2018-01-31     | INSM,STX,ALNY     | 2018-02-01      | 2018-02-28    |            -0.0575 |                      -5.75 |              1.3055 |                      130.55 |
| 2018-02-28     | INSM,STX,NFLX     | 2018-03-01      | 2018-03-29    |             0.0238 |                       2.38 |              1.3603 |                      136.03 |
| 2018-04-30     | AXON,DXCM,NFLX    | 2018-05-01      | 2018-05-31    |             0.2851 |                      28.51 |              2.0332 |                      203.32 |
| 2018-05-31     | AXON,NFLX,DXCM    | 2018-06-01      | 2018-06-29    |             0.0284 |                       2.84 |              2.1193 |                      211.93 |
| 2018-07-31     | AXON,DXCM,AMD     | 2018-08-01      | 2018-08-31    |             0.2908 |                      29.08 |              3.0265 |                      302.65 |
| 2018-08-31     | DXCM,AMD,AXON     | 2018-09-04      | 2018-09-28    |             0.0198 |                       1.98 |              3.1062 |                      310.62 |
| 2018-10-31     | AMD,DXCM,AXON     | 2018-11-01      | 2018-11-30    |            -0.0953 |                      -9.53 |              2.715  |                      271.5  |
| 2018-11-30     | AMD,DXCM,ZS       | 2018-12-03      | 2018-12-31    |            -0.114  |                     -11.4  |              2.2914 |                      229.14 |
| 2018-12-31     | AMD,DXCM,WDAY     | 2019-01-02      | 2019-01-31    |             0.2191 |                      21.91 |              3.0125 |                      301.25 |
| 2019-01-31     | AMD,DXCM,PDD      | 2019-02-01      | 2019-02-28    |            -0.0078 |                      -0.78 |              2.9811 |                      298.11 |
| 2019-02-28     | INSM,PDD,MELI     | 2019-03-01      | 2019-03-29    |            -0.0366 |                      -3.66 |              2.8353 |                      283.53 |
| 2019-04-30     | INSM,ZS,SHOP      | 2019-05-01      | 2019-05-31    |            -0.0037 |                      -0.37 |              2.8212 |                      282.12 |
| 2019-05-31     | ZS,SHOP,INSM      | 2019-06-03      | 2019-06-28    |             0.1264 |                      12.64 |              3.3044 |                      330.44 |
| 2019-07-31     | SHOP,ZS,MELI      | 2019-08-01      | 2019-08-30    |            -0.0386 |                      -3.86 |              3.1383 |                      313.83 |
| 2019-09-30     | SHOP,QCOM,PDD     | 2019-10-01      | 2019-10-31    |             0.1051 |                      10.51 |              3.5732 |                      357.32 |
| 2019-10-31     | PDD,TSLA,KLAC     | 2019-11-01      | 2019-11-29    |            -0.0418 |                      -4.18 |              3.3819 |                      338.19 |
| 2019-12-31     | PDD,TSLA,ALNY     | 2020-01-02      | 2020-01-31    |             0.1197 |                      11.97 |              3.9064 |                      390.64 |
| 2020-01-31     | TSLA,PDD,DXCM     | 2020-02-03      | 2020-02-28    |             0.0067 |                       0.67 |              3.9395 |                      393.95 |
| 2020-03-31     | TSLA,DXCM,REGN    | 2020-04-01      | 2020-04-30    |             0.3327 |                      33.27 |              5.5826 |                      558.26 |
| 2020-04-30     | TSLA,DXCM,SHOP    | 2020-05-01      | 2020-05-29    |             0.1778 |                      17.78 |              6.7527 |                      675.27 |
| 2020-06-30     | TSLA,DDOG,SHOP    | 2020-07-01      | 2020-07-31    |             0.1117 |                      11.17 |              7.6191 |                      761.91 |
| 2020-07-31     | PDD,TSLA,ZS       | 2020-08-03      | 2020-08-31    |             0.2284 |                      22.84 |              9.5876 |                      958.76 |
| 2020-08-31     | TSLA,ZS,PDD       | 2020-09-01      | 2020-09-30    |            -0.1341 |                     -13.41 |              8.1673 |                      816.73 |
| 2020-09-30     | TSLA,DDOG,SHOP    | 2020-10-01      | 2020-10-30    |            -0.1266 |                     -12.66 |              7.0068 |                      700.68 |
| 2020-11-30     | TSLA,MSTR,PDD     | 2020-12-01      | 2020-12-31    |             0.2357 |                      23.57 |              8.8944 |                      889.44 |
| 2020-12-31     | MSTR,TSLA,PDD     | 2021-01-04      | 2021-01-29    |             0.1776 |                      17.76 |             10.6513 |                     1065.13 |
| 2021-03-31     | MSTR,PLTR,FANG    | 2021-04-01      | 2021-04-30    |            -0.0203 |                      -2.03 |             10.4145 |                     1041.45 |
| 2021-04-30     | MSTR,PLTR,FANG    | 2021-05-03      | 2021-05-28    |            -0.0908 |                      -9.08 |              9.3777 |                      937.77 |
| 2021-06-30     | MSTR,FANG,AMAT    | 2021-07-01      | 2021-07-30    |            -0.0831 |                      -8.31 |              8.5149 |                      851.49 |
| 2021-08-31     | FTNT,NVDA,REGN    | 2021-09-01      | 2021-09-30    |            -0.0805 |                      -8.05 |              7.7492 |                      774.92 |
| 2021-09-30     | DDOG,FTNT,NVDA    | 2021-10-01      | 2021-10-29    |             0.1719 |                      17.19 |              9.2535 |                      925.35 |
| 2021-11-30     | NVDA,AMD,DDOG     | 2021-12-01      | 2021-12-31    |            -0.0056 |                      -0.56 |              9.1961 |                      919.61 |
| 2021-12-31     | DDOG,TSLA,AMD     | 2022-01-03      | 2022-01-31    |            -0.189  |                     -18.9  |              7.2692 |                      726.92 |
| 2022-01-31     | FANG,TSLA,DDOG    | 2022-02-01      | 2022-02-28    |             0.0285 |                       2.85 |              7.5048 |                      750.48 |
| 2022-02-28     | FANG,BKR,PANW     | 2022-03-01      | 2022-03-31    |             0.1234 |                      12.34 |              8.5547 |                      855.47 |
| 2022-03-31     | TSLA,BKR,FANG     | 2022-04-01      | 2022-04-29    |            -0.1445 |                     -14.45 |              7.1736 |                      717.36 |
| 2022-05-31     | BKR,FANG,VRTX     | 2022-06-01      | 2022-06-30    |            -0.13   |                     -13    |              6.1113 |                      611.13 |
| 2022-06-30     | BKR,VRTX,FANG     | 2022-07-01      | 2022-07-29    |            -0.0282 |                      -2.82 |              5.9104 |                      591.04 |
| 2022-08-31     | CEG,PDD,ALNY      | 2022-09-01      | 2022-09-30    |            -0.0561 |                      -5.61 |              5.5231 |                      552.31 |
| 2022-09-30     | PDD,CEG,ALNY      | 2022-10-03      | 2022-10-31    |             0.0067 |                       0.67 |              5.567  |                      556.7  |
| 2022-10-31     | ALNY,CEG,NFLX     | 2022-11-01      | 2022-11-30    |             0.0361 |                       3.61 |              5.8042 |                      580.42 |
| 2022-11-30     | PDD,AXON,ALNY     | 2022-12-01      | 2022-12-30    |            -0.0176 |                      -1.76 |              5.6842 |                      568.42 |
| 2023-01-31     | PDD,AXON,ALNY     | 2023-02-01      | 2023-02-28    |            -0.0957 |                      -9.57 |              5.0444 |                      504.44 |
| 2023-02-28     | AXON,NVDA,MSTR    | 2023-03-01      | 2023-03-31    |             0.1248 |                      12.48 |              5.799  |                      579.9  |
| 2023-03-31     | NVDA,AXON,SHOP    | 2023-04-03      | 2023-04-28    |            -0.0216 |                      -2.16 |              5.6518 |                      565.18 |
| 2023-05-31     | PLTR,NVDA,META    | 2023-06-01      | 2023-06-30    |             0.0569 |                       5.69 |              6.0306 |                      603.06 |
| 2023-06-30     | NVDA,PLTR,MSTR    | 2023-07-03      | 2023-07-31    |             0.1797 |                      17.97 |              7.2938 |                      729.38 |
| 2023-07-31     | PLTR,APP,NVDA     | 2023-08-01      | 2023-08-31    |             0.0619 |                       6.19 |              7.8072 |                      780.72 |
| 2023-08-31     | APP,PLTR,NVDA     | 2023-09-01      | 2023-09-29    |            -0.0413 |                      -4.13 |              7.4433 |                      744.33 |
| 2023-10-31     | PLTR,APP,ZS       | 2023-11-01      | 2023-11-30    |             0.2087 |                      20.87 |              9.2053 |                      920.53 |
| 2023-11-30     | PDD,MSTR,APP      | 2023-12-01      | 2023-12-29    |             0.082  |                       8.2  |             10.042  |                     1004.2  |
| 2024-01-31     | CRWD,PDD,AMD      | 2024-02-01      | 2024-02-29    |             0.0653 |                       6.53 |             10.7631 |                     1076.31 |
| 2024-02-29     | MSTR,CRWD,PLTR    | 2024-03-01      | 2024-03-28    |             0.1737 |                      17.37 |             12.8068 |                     1280.68 |
| 2024-04-30     | MSTR,ARM,NVDA     | 2024-05-01      | 2024-05-31    |             0.3559 |                      35.59 |             17.72   |                     1772    |
| 2024-05-31     | MSTR,INSM,ARM     | 2024-06-03      | 2024-06-28    |             0.1104 |                      11.04 |             19.7872 |                     1978.72 |
| 2024-07-31     | MSTR,INSM,ARM     | 2024-08-01      | 2024-08-30    |            -0.0051 |                      -0.51 |             19.6805 |                     1968.05 |
| 2024-09-30     | INSM,ALNY,APP     | 2024-10-01      | 2024-10-31    |             0.0618 |                       6.18 |             20.9584 |                     2095.84 |
| 2024-10-31     | INSM,MSTR,APP     | 2024-11-01      | 2024-11-29    |             0.6154 |                      61.54 |             34.4712 |                     3447.12 |
| 2024-12-31     | APP,PLTR,MSTR     | 2025-01-02      | 2025-01-31    |             0.0981 |                       9.81 |             37.952  |                     3795.2  |
| 2025-01-31     | APP,PLTR,MSTR     | 2025-02-03      | 2025-02-28    |            -0.1195 |                     -11.95 |             33.2956 |                     3329.56 |
| 2025-02-28     | APP,PLTR,MSTR     | 2025-03-03      | 2025-03-31    |            -0.018  |                      -1.8  |             32.679  |                     3267.9  |
| 2025-03-31     | APP,PLTR,MSTR     | 2025-04-01      | 2025-04-30    |             0.1978 |                      19.78 |             39.341  |                     3934.1  |
| 2025-04-30     | PLTR,APP,MSTR     | 2025-05-01      | 2025-05-30    |             0.1691 |                      16.91 |             46.1633 |                     4616.33 |
| 2025-06-30     | PLTR,STX,ZS       | 2025-07-01      | 2025-07-31    |             0.0745 |                       7.45 |             49.6764 |                     4967.64 |
| 2025-07-31     | PLTR,STX,WDC      | 2025-08-01      | 2025-08-29    |             0.0489 |                       4.89 |             52.1536 |                     5215.36 |
| 2025-09-30     | SNDK,WDC,APP      | 2025-10-01      | 2025-10-31    |             0.2337 |                      23.37 |             64.5765 |                     6457.65 |
| 2025-10-31     | SNDK,WDC,LITE     | 2025-11-03      | 2025-11-28    |             0.2471 |                      24.71 |             80.7831 |                     8078.31 |
| 2025-12-31     | SNDK,LITE,WDC     | 2026-01-02      | 2026-01-30    |             0.4805 |                      48.05 |            120.083  |                    12008.3  |
| 2026-03-31     | SNDK,LITE,WDC     | 2026-04-01      | 2026-04-30    |             0.4075 |                      40.75 |            169.419  |                    16941.9  |
| 2026-04-30     | SNDK,LITE,WDC     | 2026-05-01      | 2026-05-29    |             0.1863 |                      18.63 |            201.173  |                    20117.3  |

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
| total_return_percent                |         20117.3     |                  7948.99    | -12168.3      |
| annualized_return_percent           |           107.984   |                    83.1728  |    -24.8117   |
| annualized_volatility_percent       |            50.6098  |                    45.5663  |     -5.04354  |
| sharpe_ratio_without_risk_free_rate |             2.13367 |                     1.82531 |     -0.308351 |
| max_drawdown_percent                |           -48.1227  |                   -35.8217  |     12.301    |
| win_rate_percent                    |            63.2184  |                    50.5747  |    -12.6437   |
| number_of_months                    |            87       |                    87       |      0        |

---

## Market Regime Backtest Summary

The following table shows the summary statistics of the strategy after adding the Nasdaq market regime filter.

| strategy_name                                                      | data_start_date   | backtest_start_date   | market_index_ticker   |   market_trend_months | start_date   | end_date   |   lookback_months |   top_n |   bull_market_months |   bear_market_months |   trading_months |   cash_months |   bull_market_average_monthly_return_percent |   bear_market_average_monthly_return_percent |   total_return_percent |   annualized_return_percent |   annualized_volatility_percent |   sharpe_ratio_without_risk_free_rate |   max_drawdown_percent |   win_rate_percent |   positive_months |   negative_months |   zero_months |   number_of_months |
|:-------------------------------------------------------------------|:------------------|:----------------------|:----------------------|----------------------:|:-------------|:-----------|------------------:|--------:|---------------------:|---------------------:|-----------------:|--------------:|---------------------------------------------:|---------------------------------------------:|-----------------------:|----------------------------:|--------------------------------:|--------------------------------------:|-----------------------:|-------------------:|------------------:|------------------:|--------------:|-------------------:|
| Nasdaq-100 Top 3 Six-Month Mean Momentum With Market Regime Filter | 2014-01-01        | 2016-02-01            | QQQ                   |                    10 | 2016-03-01   | 2026-05-29 |                 6 |       3 |                   68 |                   19 |               68 |            19 |                                         7.56 |                                            0 |                7948.99 |                       83.17 |                           45.57 |                               1.82531 |                 -35.82 |              50.57 |                44 |                24 |            19 |                 87 |

---

## Market Regime Monthly Return Statistics

The following table summarizes the distribution of monthly strategy returns after applying the market regime filter.

| metric                         |   value |
|:-------------------------------|--------:|
| Total months                   |   87    |
| Winning months                 |   44    |
| Losing months                  |   24    |
| Flat months                    |   19    |
| Win rate percent               |   50.57 |
| Average monthly return percent |    5.91 |
| Average winning month percent  |   14.86 |
| Average losing month percent   |   -5.82 |
| Best month percent             |   61.54 |
| Worst month percent            |  -18.9  |
| Monthly volatility percent     |   13.15 |
| Profit loss ratio              |    2.55 |

---

## Full Market Regime Backtest Returns

The following table shows the full monthly strategy return history with the market regime filter.

| ranking_date   | market_regime   | is_bull_market   |   market_index_price |   market_index_ma | selected_stocks   | holding_start   | holding_end   |   portfolio_return |   portfolio_return_percent |   cumulative_return |   cumulative_return_percent |
|:---------------|:----------------|:-----------------|---------------------:|------------------:|:------------------|:----------------|:--------------|-------------------:|---------------------------:|--------------------:|----------------------------:|
| 2016-02-29     | Bear Market     | False            |                95.21 |            100.08 | CASH              | 2016-03-01      | 2016-03-31    |             0      |                       0    |              0      |                        0    |
| 2016-03-31     | Bull Market     | True             |               101.74 |            100.11 | AMD,LITE,KLAC     | 2016-04-01      | 2016-04-29    |             0.0546 |                       5.46 |              0.0546 |                        5.46 |
| 2016-05-31     | Bull Market     | True             |               102.8  |            100    | AMD,NVDA,AMAT     | 2016-06-01      | 2016-06-30    |             0.0492 |                       4.92 |              0.1065 |                       10.65 |
| 2016-06-30     | Bull Market     | True             |               100.46 |            100.41 | AMD,AXON,NVDA     | 2016-07-01      | 2016-07-29    |             0.2468 |                      24.68 |              0.3795 |                       37.95 |
| 2016-08-31     | Bull Market     | True             |               108.77 |            102.14 | AMD,NVDA,SHOP     | 2016-09-01      | 2016-09-30    |             0.0268 |                       2.68 |              0.4166 |                       41.66 |
| 2016-09-30     | Bull Market     | True             |               111.18 |            102.7  | AMD,NVDA,MU       | 2016-10-03      | 2016-10-31    |             0.0159 |                       1.59 |              0.4391 |                       43.91 |
| 2016-10-31     | Bull Market     | True             |               109.56 |            103.26 | AMD,NVDA,STX      | 2016-11-01      | 2016-11-30    |             0.2612 |                      26.12 |              0.815  |                       81.5  |
| 2016-11-30     | Bull Market     | True             |               110.04 |            104.59 | AMD,NVDA,STX      | 2016-12-01      | 2016-12-30    |             0.1958 |                      19.58 |              1.1704 |                      117.04 |
| 2017-01-31     | Bull Market     | True             |               117.01 |            107.72 | NVDA,MU,WDC       | 2017-02-01      | 2017-02-28    |            -0.0633 |                      -6.33 |              1.0329 |                      103.29 |
| 2017-02-28     | Bull Market     | True             |               122.12 |            110.09 | AMD,CSX,WDC       | 2017-03-01      | 2017-03-31    |            -0.007  |                      -0.7  |              1.0186 |                      101.86 |
| 2017-03-31     | Bull Market     | True             |               124.6  |            112.27 | AMD,MU,NVDA       | 2017-04-03      | 2017-04-28    |            -0.0543 |                      -5.43 |              0.9089 |                       90.89 |
| 2017-05-31     | Bull Market     | True             |               132.99 |            117.56 | SHOP,TSLA,MELI    | 2017-06-01      | 2017-06-30    |            -0.0374 |                      -3.74 |              0.8374 |                       83.74 |
| 2017-06-30     | Bull Market     | True             |               129.9  |            119.67 | ALNY,SHOP,VRTX    | 2017-07-03      | 2017-07-31    |             0.0903 |                       9.03 |              1.0032 |                      100.32 |
| 2017-07-31     | Bull Market     | True             |               135.18 |            122.07 | ALNY,SHOP,VRTX    | 2017-08-01      | 2017-08-31    |             0.0567 |                       5.67 |              1.1168 |                      111.68 |
| 2017-08-31     | Bull Market     | True             |               137.98 |            124.91 | SHOP,VRTX,TTWO    | 2017-09-01      | 2017-09-29    |             0.018  |                       1.8  |              1.155  |                      115.5  |
| 2017-10-31     | Bull Market     | True             |               143.91 |            130.93 | INSM,ALNY,NVDA    | 2017-11-01      | 2017-11-30    |             0.0756 |                       7.56 |              1.3178 |                      131.78 |
| 2017-11-30     | Bull Market     | True             |               146.75 |            133.9  | INSM,ALNY,TTWO    | 2017-12-01      | 2017-12-29    |            -0.0257 |                      -2.57 |              1.2583 |                      125.83 |
| 2018-01-31     | Bull Market     | True             |               160.56 |            140.05 | INSM,STX,ALNY     | 2018-02-01      | 2018-02-28    |            -0.0575 |                      -5.75 |              1.1283 |                      112.83 |
| 2018-02-28     | Bull Market     | True             |               158.49 |            143.1  | INSM,STX,NFLX     | 2018-03-01      | 2018-03-29    |             0.0238 |                       2.38 |              1.1789 |                      117.89 |
| 2018-04-30     | Bull Market     | True             |               152.79 |            147.29 | AXON,DXCM,NFLX    | 2018-05-01      | 2018-05-31    |             0.2851 |                      28.51 |              1.8001 |                      180.01 |
| 2018-05-31     | Bull Market     | True             |               161.46 |            149.92 | AXON,NFLX,DXCM    | 2018-06-01      | 2018-06-29    |             0.0284 |                       2.84 |              1.8796 |                      187.96 |
| 2018-07-31     | Bull Market     | True             |               167.88 |            155.48 | AXON,DXCM,AMD     | 2018-08-01      | 2018-08-31    |             0.2908 |                      29.08 |              2.7171 |                      271.71 |
| 2018-08-31     | Bull Market     | True             |               177.58 |            158.85 | DXCM,AMD,AXON     | 2018-09-04      | 2018-09-28    |             0.0198 |                       1.98 |              2.7907 |                      279.07 |
| 2018-10-31     | Bear Market     | False            |               161.86 |            163.3  | CASH              | 2018-11-01      | 2018-11-30    |             0      |                       0    |              2.7907 |                      279.07 |
| 2018-11-30     | Bear Market     | False            |               161.43 |            163.39 | CASH              | 2018-12-03      | 2018-12-31    |             0      |                       0    |              2.7907 |                      279.07 |
| 2018-12-31     | Bear Market     | False            |               147.45 |            162.29 | CASH              | 2019-01-02      | 2019-01-31    |             0      |                       0    |              2.7907 |                      279.07 |
| 2019-01-31     | Bear Market     | False            |               160.73 |            163.16 | CASH              | 2019-02-01      | 2019-02-28    |             0      |                       0    |              2.7907 |                      279.07 |
| 2019-02-28     | Bull Market     | True             |               165.54 |            164.43 | INSM,PDD,MELI     | 2019-03-01      | 2019-03-29    |            -0.0366 |                      -3.66 |              2.6518 |                      265.18 |
| 2019-04-30     | Bull Market     | True             |               181.5  |            167.31 | INSM,ZS,SHOP      | 2019-05-01      | 2019-05-31    |            -0.0037 |                      -0.37 |              2.6385 |                      263.85 |
| 2019-05-31     | Bear Market     | False            |               166.57 |            167.18 | CASH              | 2019-06-03      | 2019-06-28    |             0      |                       0    |              2.6385 |                      263.85 |
| 2019-07-31     | Bull Market     | True             |               183.4  |            167.97 | SHOP,ZS,MELI      | 2019-08-01      | 2019-08-30    |            -0.0386 |                      -3.86 |              2.4981 |                      249.81 |
| 2019-09-30     | Bull Market     | True             |               181.57 |            171.79 | SHOP,QCOM,PDD     | 2019-10-01      | 2019-10-31    |             0.1051 |                      10.51 |              2.8657 |                      286.57 |
| 2019-10-31     | Bull Market     | True             |               189.52 |            176    | PDD,TSLA,KLAC     | 2019-11-01      | 2019-11-29    |            -0.0418 |                      -4.18 |              2.704  |                      270.4  |
| 2019-12-31     | Bull Market     | True             |               204.9  |            183.59 | PDD,TSLA,ALNY     | 2020-01-02      | 2020-01-31    |             0.1197 |                      11.97 |              3.1473 |                      314.73 |
| 2020-01-31     | Bull Market     | True             |               211.12 |            187.49 | TSLA,PDD,DXCM     | 2020-02-03      | 2020-02-28    |             0.0067 |                       0.67 |              3.1753 |                      317.53 |
| 2020-03-31     | Bear Market     | False            |               183.88 |            190.91 | CASH              | 2020-04-01      | 2020-04-30    |             0      |                       0    |              3.1753 |                      317.53 |
| 2020-04-30     | Bull Market     | True             |               211.42 |            194.13 | TSLA,DXCM,SHOP    | 2020-05-01      | 2020-05-29    |             0.1778 |                      17.78 |              3.9175 |                      391.75 |
| 2020-06-30     | Bull Market     | True             |               239.54 |            204.29 | TSLA,DDOG,SHOP    | 2020-07-01      | 2020-07-31    |             0.1117 |                      11.17 |              4.467  |                      446.7  |
| 2020-07-31     | Bull Market     | True             |               257.14 |            211.85 | PDD,TSLA,ZS       | 2020-08-03      | 2020-08-31    |             0.2284 |                      22.84 |              5.7156 |                      571.56 |
| 2020-08-31     | Bull Market     | True             |               285.28 |            221.42 | TSLA,ZS,PDD       | 2020-09-01      | 2020-09-30    |            -0.1341 |                     -13.41 |              4.8147 |                      481.47 |
| 2020-09-30     | Bull Market     | True             |               268.8  |            228.58 | TSLA,DDOG,SHOP    | 2020-10-01      | 2020-10-30    |            -0.1266 |                     -12.66 |              4.0786 |                      407.86 |
| 2020-11-30     | Bull Market     | True             |               289.87 |            242.02 | TSLA,MSTR,PDD     | 2020-12-01      | 2020-12-31    |             0.2357 |                      23.57 |              5.2759 |                      527.59 |
| 2020-12-31     | Bull Market     | True             |               304.08 |            252.6  | MSTR,TSLA,PDD     | 2021-01-04      | 2021-01-29    |             0.1776 |                      17.76 |              6.3903 |                      639.03 |
| 2021-03-31     | Bull Market     | True             |               309.69 |            282.44 | MSTR,PLTR,FANG    | 2021-04-01      | 2021-04-30    |            -0.0203 |                      -2.03 |              6.2401 |                      624.01 |
| 2021-04-30     | Bull Market     | True             |               328    |            291.28 | MSTR,PLTR,FANG    | 2021-05-03      | 2021-05-28    |            -0.0908 |                      -9.08 |              5.5824 |                      558.24 |
| 2021-06-30     | Bull Market     | True             |               344.35 |            303.88 | MSTR,FANG,AMAT    | 2021-07-01      | 2021-07-30    |            -0.0831 |                      -8.31 |              5.0352 |                      503.52 |
| 2021-08-31     | Bull Market     | True             |               369.14 |            323.27 | FTNT,NVDA,REGN    | 2021-09-01      | 2021-09-30    |            -0.0805 |                      -8.05 |              4.5495 |                      454.95 |
| 2021-09-30     | Bull Market     | True             |               348.16 |            329.1  | DDOG,FTNT,NVDA    | 2021-10-01      | 2021-10-29    |             0.1719 |                      17.19 |              5.5037 |                      550.37 |
| 2021-11-30     | Bull Market     | True             |               383.04 |            344.07 | NVDA,AMD,DDOG     | 2021-12-01      | 2021-12-31    |            -0.0056 |                      -0.56 |              5.4673 |                      546.73 |
| 2021-12-31     | Bull Market     | True             |               387.46 |            352.36 | DDOG,TSLA,AMD     | 2022-01-03      | 2022-01-31    |            -0.189  |                     -18.9  |              4.245  |                      424.5  |
| 2022-01-31     | Bear Market     | False            |               353.57 |            356.75 | CASH              | 2022-02-01      | 2022-02-28    |             0      |                       0    |              4.245  |                      424.5  |
| 2022-02-28     | Bear Market     | False            |               337.74 |            357.73 | CASH              | 2022-03-01      | 2022-03-31    |             0      |                       0    |              4.245  |                      424.5  |
| 2022-03-31     | Bear Market     | False            |               353.51 |            360.67 | CASH              | 2022-04-01      | 2022-04-29    |             0      |                       0    |              4.245  |                      424.5  |
| 2022-05-31     | Bear Market     | False            |               300.6  |            351.42 | CASH              | 2022-06-01      | 2022-06-30    |             0      |                       0    |              4.245  |                      424.5  |
| 2022-06-30     | Bear Market     | False            |               273.82 |            341.89 | CASH              | 2022-07-01      | 2022-07-29    |             0      |                       0    |              4.245  |                      424.5  |
| 2022-08-31     | Bear Market     | False            |               292.37 |            329.57 | CASH              | 2022-09-01      | 2022-09-30    |             0      |                       0    |              4.245  |                      424.5  |
| 2022-09-30     | Bear Market     | False            |               261.57 |            317.43 | CASH              | 2022-10-03      | 2022-10-31    |             0      |                       0    |              4.245  |                      424.5  |
| 2022-10-31     | Bear Market     | False            |               272.03 |            305.88 | CASH              | 2022-11-01      | 2022-11-30    |             0      |                       0    |              4.245  |                      424.5  |
| 2022-11-30     | Bear Market     | False            |               287.11 |            299.24 | CASH              | 2022-12-01      | 2022-12-30    |             0      |                       0    |              4.245  |                      424.5  |
| 2023-01-31     | Bull Market     | True             |               289.04 |            285.14 | PDD,AXON,ALNY     | 2023-02-01      | 2023-02-28    |            -0.0957 |                      -9.57 |              3.7429 |                      374.29 |
| 2023-02-28     | Bull Market     | True             |               288    |            283.4  | AXON,NVDA,MSTR    | 2023-03-01      | 2023-03-31    |             0.1248 |                      12.48 |              4.3351 |                      433.51 |
| 2023-03-31     | Bull Market     | True             |               315.34 |            284.87 | NVDA,AXON,SHOP    | 2023-04-03      | 2023-04-28    |            -0.0216 |                      -2.16 |              4.2196 |                      421.96 |
| 2023-05-31     | Bull Market     | True             |               341.92 |            292.56 | PLTR,NVDA,META    | 2023-06-01      | 2023-06-30    |             0.0569 |                       5.69 |              4.5168 |                      451.68 |
| 2023-06-30     | Bull Market     | True             |               363.48 |            299.67 | NVDA,PLTR,MSTR    | 2023-07-03      | 2023-07-31    |             0.1797 |                      17.97 |              5.508  |                      550.8  |
| 2023-07-31     | Bull Market     | True             |               377.51 |            311.26 | PLTR,APP,NVDA     | 2023-08-01      | 2023-08-31    |             0.0619 |                       6.19 |              5.911  |                      591.1  |
| 2023-08-31     | Bull Market     | True             |               371.91 |            321.25 | APP,PLTR,NVDA     | 2023-09-01      | 2023-09-29    |            -0.0413 |                      -4.13 |              5.6254 |                      562.54 |
| 2023-10-31     | Bull Market     | True             |               345.73 |            336.29 | PLTR,APP,ZS       | 2023-11-01      | 2023-11-30    |             0.2087 |                      20.87 |              7.008  |                      700.8  |
| 2023-11-30     | Bull Market     | True             |               383.13 |            345.7  | PDD,MSTR,APP      | 2023-12-01      | 2023-12-29    |             0.082  |                       8.2  |              7.6645 |                      766.45 |
| 2024-01-31     | Bull Market     | True             |               411.9  |            367.01 | CRWD,PDD,AMD      | 2024-02-01      | 2024-02-29    |             0.0653 |                       6.53 |              8.2304 |                      823.04 |
| 2024-02-29     | Bull Market     | True             |               433.66 |            378.68 | MSTR,CRWD,PLTR    | 2024-03-01      | 2024-03-28    |             0.1737 |                      17.37 |              9.834  |                      983.4  |
| 2024-04-30     | Bull Market     | True             |               419.98 |            394.06 | MSTR,ARM,NVDA     | 2024-05-01      | 2024-05-31    |             0.3559 |                      35.59 |             13.6894 |                     1368.94 |
| 2024-05-31     | Bull Market     | True             |               445.81 |            400.89 | MSTR,INSM,ARM     | 2024-06-03      | 2024-06-28    |             0.1104 |                      11.04 |             15.3115 |                     1531.15 |
| 2024-07-31     | Bull Market     | True             |               466.69 |            422.53 | MSTR,INSM,ARM     | 2024-08-01      | 2024-08-30    |            -0.0051 |                      -0.51 |             15.2278 |                     1522.78 |
| 2024-09-30     | Bull Market     | True             |               484.21 |            445.25 | INSM,ALNY,APP     | 2024-10-01      | 2024-10-31    |             0.0618 |                       6.18 |             16.2305 |                     1623.05 |
| 2024-10-31     | Bull Market     | True             |               480.03 |            452.8  | INSM,MSTR,APP     | 2024-11-01      | 2024-11-29    |             0.6154 |                      61.54 |             26.8339 |                     2683.39 |
| 2024-12-31     | Bull Market     | True             |               508.01 |            469.61 | APP,PLTR,MSTR     | 2025-01-02      | 2025-01-31    |             0.0981 |                       9.81 |             29.5652 |                     2956.52 |
| 2025-01-31     | Bull Market     | True             |               519    |            477.6  | APP,PLTR,MSTR     | 2025-02-03      | 2025-02-28    |            -0.1195 |                     -11.95 |             25.9114 |                     2591.14 |
| 2025-02-28     | Bull Market     | True             |               504.97 |            486.09 | APP,PLTR,MSTR     | 2025-03-03      | 2025-03-31    |            -0.018  |                      -1.8  |             25.4276 |                     2542.76 |
| 2025-03-31     | Bear Market     | False            |               466.66 |            488.18 | CASH              | 2025-04-01      | 2025-04-30    |             0      |                       0    |             25.4276 |                     2542.76 |
| 2025-04-30     | Bear Market     | False            |               473.18 |            488.03 | CASH              | 2025-05-01      | 2025-05-30    |             0      |                       0    |             25.4276 |                     2542.76 |
| 2025-06-30     | Bull Market     | True             |               549.6  |            500.8  | PLTR,STX,ZS       | 2025-07-01      | 2025-07-31    |             0.0745 |                       7.45 |             27.3961 |                     2739.61 |
| 2025-07-31     | Bull Market     | True             |               562.92 |            508.67 | PLTR,STX,WDC      | 2025-08-01      | 2025-08-29    |             0.0489 |                       4.89 |             28.7842 |                     2878.42 |
| 2025-09-30     | Bull Market     | True             |               598.84 |            526.81 | SNDK,WDC,APP      | 2025-10-01      | 2025-10-31    |             0.2337 |                      23.37 |             35.7453 |                     3574.53 |
| 2025-10-31     | Bull Market     | True             |               627.47 |            538.75 | SNDK,WDC,LITE     | 2025-11-03      | 2025-11-28    |             0.2471 |                      24.71 |             44.8265 |                     4482.65 |
| 2025-12-31     | Bull Market     | True             |               613.54 |            559.48 | SNDK,LITE,WDC     | 2026-01-02      | 2026-01-30    |             0.4805 |                      48.05 |             66.8477 |                     6684.77 |
| 2026-03-31     | Bear Market     | False            |               577.18 |            594.31 | CASH              | 2026-04-01      | 2026-04-30    |             0      |                       0    |             66.8477 |                     6684.77 |
| 2026-04-30     | Bull Market     | True             |               667.74 |            606.13 | SNDK,LITE,WDC     | 2026-05-01      | 2026-05-29    |             0.1863 |                      18.63 |             79.4899 |                     7948.99 |

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
