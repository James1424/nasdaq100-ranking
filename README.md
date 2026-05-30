# Nasdaq-100 Six-Month Mean Momentum Strategy

This repository builds a rule-based momentum ranking and backtesting system for Nasdaq-100 stocks.

The core idea is simple:

> At the beginning of each month, rank Nasdaq-100 stocks by their average monthly return over the previous six months, buy the top three stocks, and hold them for the following month.


Last updated: **2026-05-30 03:31:11 UTC**

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
5. If the Nasdaq market index is in a bull market, hold these stocks for the following month; otherwise stay in cash.
6. Use the next month's realized return to calculate strategy performance. Bear-market cash months are recorded as 0% return.
7. Rebalance monthly.

The strategy does not use news, analyst reports, valuation metrics, or discretionary stock picking.

It is a simple rule-based momentum strategy.

---

## Backtest Summary

The following table shows the summary statistics of the monthly mean momentum backtest.

| strategy_name                            | start_date   | end_date   |   lookback_months |   top_n | market_index_ticker   |   market_trend_months |   bull_market_months |   bear_market_months |   trading_months |   cash_months |   total_return_percent |   annualized_return_percent |   annualized_volatility_percent |   sharpe_ratio_without_risk_free_rate |   max_drawdown_percent |   win_rate_percent |   number_of_months |
|:-----------------------------------------|:-------------|:-----------|------------------:|--------:|:----------------------|----------------------:|---------------------:|---------------------:|-----------------:|--------------:|-----------------------:|----------------------------:|--------------------------------:|--------------------------------------:|-----------------------:|-------------------:|-------------------:|
| Nasdaq-100 Top 3 Six-Month Mean Momentum | 2016-10-31   | 2026-05-31 |                 6 |       3 | QQQ                   |                    10 |                   94 |                   21 |               94 |            21 |                19588.7 |                       73.54 |                           46.65 |                               1.57638 |                 -32.68 |              49.57 |                115 |

---

## Backtest Monthly Return Statistics

The following table summarizes the distribution of monthly strategy returns.

| metric                         |   value |
|:-------------------------------|--------:|
| Total months                   |  115    |
| Winning months                 |   57    |
| Losing months                  |   37    |
| Flat months                    |   21    |
| Win rate percent               |   49.57 |
| Average monthly return percent |    5.48 |
| Average winning month percent  |   15.22 |
| Average losing month percent   |   -6.4  |
| Best month percent             |   64.77 |
| Worst month percent            |  -20.31 |
| Monthly volatility percent     |   13.47 |
| Profit loss ratio              |    2.38 |

---

## Full Monthly Backtest Returns

The following table shows the full monthly strategy return history.

| ranking_date   | market_regime   | is_bull_market   | trade_executed   |   market_index_price |   market_index_ma | selected_stocks   | holding_start   | holding_end   |   portfolio_return |   portfolio_return_percent |   cumulative_return |   cumulative_return_percent |
|:---------------|:----------------|:-----------------|:-----------------|---------------------:|------------------:|:------------------|:----------------|:--------------|-------------------:|---------------------------:|--------------------:|----------------------------:|
| 2016-10-31     | Bull Market     | True             | True             |               109.56 |           103.26  | AMD,NVDA,STX      | 2016-10-31      | 2016-11-30    |             0.2329 |                      23.29 |              0.2329 |                       23.29 |
| 2016-11-30     | Bull Market     | True             | True             |               110.04 |           104.591 | AMD,NVDA,STX      | 2016-11-30      | 2016-12-31    |             0.1326 |                      13.26 |              0.3964 |                       39.64 |
| 2016-12-31     | Bull Market     | True             | True             |               111.28 |           106.198 | NVDA,AMD,LITE     | 2016-12-31      | 2017-01-31    |            -0.0269 |                      -2.69 |              0.3588 |                       35.88 |
| 2017-01-31     | Bull Market     | True             | True             |               117.01 |           107.725 | NVDA,MU,WDC       | 2017-01-31      | 2017-02-28    |            -0.0443 |                      -4.43 |              0.2986 |                       29.86 |
| 2017-02-28     | Bull Market     | True             | True             |               122.12 |           110.087 | AMD,CSX,WDC       | 2017-02-28      | 2017-03-31    |             0.015  |                       1.5  |              0.3181 |                       31.81 |
| 2017-03-31     | Bull Market     | True             | True             |               124.6  |           112.267 | AMD,MU,NVDA       | 2017-03-31      | 2017-04-30    |            -0.057  |                      -5.7  |              0.243  |                       24.3  |
| 2017-04-30     | Bull Market     | True             | True             |               128    |           115.021 | AMD,SHOP,CSX      | 2017-04-30      | 2017-05-31    |             0.0401 |                       4.01 |              0.2929 |                       29.29 |
| 2017-05-31     | Bull Market     | True             | True             |               132.99 |           117.555 | SHOP,TSLA,MELI    | 2017-05-31      | 2017-06-30    |            -0.027  |                      -2.7  |              0.2579 |                       25.79 |
| 2017-06-30     | Bull Market     | True             | True             |               129.9  |           119.668 | ALNY,SHOP,VRTX    | 2017-06-30      | 2017-07-31    |             0.0928 |                       9.28 |              0.3746 |                       37.46 |
| 2017-07-31     | Bull Market     | True             | True             |               135.18 |           122.068 | ALNY,SHOP,VRTX    | 2017-07-31      | 2017-08-31    |             0.0981 |                       9.81 |              0.5095 |                       50.95 |
| 2017-08-31     | Bull Market     | True             | True             |               137.98 |           124.91  | SHOP,VRTX,TTWO    | 2017-08-31      | 2017-09-30    |             0.0142 |                       1.42 |              0.531  |                       53.1  |
| 2017-09-30     | Bull Market     | True             | True             |               137.57 |           127.664 | INSM,ALNY,TTWO    | 2017-09-30      | 2017-10-31    |            -0.0051 |                      -0.51 |              0.5232 |                       52.32 |
| 2017-10-31     | Bull Market     | True             | True             |               143.91 |           130.926 | INSM,ALNY,NVDA    | 2017-10-31      | 2017-11-30    |             0.0767 |                       7.67 |              0.6401 |                       64.01 |
| 2017-11-30     | Bull Market     | True             | True             |               146.75 |           133.901 | INSM,ALNY,TTWO    | 2017-11-30      | 2017-12-31    |            -0.024  |                      -2.4  |              0.6008 |                       60.08 |
| 2017-12-31     | Bull Market     | True             | True             |               147.63 |           136.452 | INSM,ALNY,TTWO    | 2017-12-31      | 2018-01-31    |            -0.0024 |                      -0.24 |              0.597  |                       59.7  |
| 2018-01-31     | Bull Market     | True             | True             |               160.56 |           140.048 | INSM,STX,ALNY     | 2018-01-31      | 2018-02-28    |            -0.0522 |                      -5.22 |              0.5137 |                       51.37 |
| 2018-02-28     | Bull Market     | True             | True             |               158.49 |           143.097 | INSM,STX,NFLX     | 2018-02-28      | 2018-03-31    |             0.0171 |                       1.71 |              0.5395 |                       53.95 |
| 2018-03-31     | Bull Market     | True             | True             |               152.02 |           145.001 | STX,AXON,NFLX     | 2018-03-31      | 2018-04-30    |             0.0384 |                       3.84 |              0.5986 |                       59.86 |
| 2018-04-30     | Bull Market     | True             | True             |               152.79 |           147.29  | AXON,DXCM,NFLX    | 2018-04-30      | 2018-05-31    |             0.2815 |                      28.15 |              1.0486 |                      104.86 |
| 2018-05-31     | Bull Market     | True             | True             |               161.46 |           149.918 | AXON,NFLX,DXCM    | 2018-05-31      | 2018-06-30    |             0.0616 |                       6.16 |              1.1749 |                      117.49 |
| 2018-06-30     | Bull Market     | True             | True             |               163.31 |           152.45  | AXON,NFLX,DXCM    | 2018-06-30      | 2018-07-31    |            -0.0204 |                      -2.04 |              1.1305 |                      113.05 |
| 2018-07-31     | Bull Market     | True             | True             |               167.88 |           155.48  | AXON,DXCM,AMD     | 2018-07-31      | 2018-08-31    |             0.2986 |                      29.86 |              1.7667 |                      176.67 |
| 2018-08-31     | Bull Market     | True             | True             |               177.58 |           158.847 | DXCM,AMD,AXON     | 2018-08-31      | 2018-09-30    |             0.0735 |                       7.35 |              1.97   |                      197    |
| 2018-09-30     | Bull Market     | True             | True             |               177.08 |           161.88  | AMD,DXCM,AXON     | 2018-09-30      | 2018-10-31    |            -0.1934 |                     -19.34 |              1.3955 |                      139.55 |
| 2018-10-31     | Bear Market     | False            | False            |               161.86 |           163.302 | CASH              | 2018-10-31      | 2018-11-30    |             0      |                       0    |              1.3955 |                      139.55 |
| 2018-11-30     | Bear Market     | False            | False            |               161.43 |           163.389 | CASH              | 2018-11-30      | 2018-12-31    |             0      |                       0    |              1.3955 |                      139.55 |
| 2018-12-31     | Bear Market     | False            | False            |               147.45 |           162.285 | CASH              | 2018-12-31      | 2019-01-31    |             0      |                       0    |              1.3955 |                      139.55 |
| 2019-01-31     | Bear Market     | False            | False            |               160.73 |           163.156 | CASH              | 2019-01-31      | 2019-02-28    |             0      |                       0    |              1.3955 |                      139.55 |
| 2019-02-28     | Bull Market     | True             | True             |               165.54 |           164.431 | INSM,PDD,MELI     | 2019-02-28      | 2019-03-31    |            -0.0282 |                      -2.82 |              1.3279 |                      132.79 |
| 2019-03-31     | Bull Market     | True             | True             |               172.04 |           165.489 | INSM,ZS,MELI      | 2019-03-31      | 2019-04-30    |            -0.0121 |                      -1.21 |              1.2998 |                      129.98 |
| 2019-04-30     | Bull Market     | True             | True             |               181.5  |           167.309 | INSM,ZS,SHOP      | 2019-04-30      | 2019-05-31    |            -0.0237 |                      -2.37 |              1.2452 |                      124.52 |
| 2019-05-31     | Bear Market     | False            | False            |               166.57 |           167.178 | CASH              | 2019-05-31      | 2019-06-30    |             0      |                       0    |              1.2452 |                      124.52 |
| 2019-06-30     | Bull Market     | True             | True             |               179.21 |           167.342 | INSM,SHOP,MELI    | 2019-06-30      | 2019-07-31    |            -0.0226 |                      -2.26 |              1.1945 |                      119.45 |
| 2019-07-31     | Bull Market     | True             | True             |               183.4  |           167.974 | SHOP,ZS,MELI      | 2019-07-31      | 2019-08-31    |            -0.005  |                      -0.5  |              1.1835 |                      118.35 |
| 2019-08-31     | Bull Market     | True             | True             |               179.91 |           169.779 | SHOP,QCOM,TTWO    | 2019-08-31      | 2019-09-30    |            -0.0843 |                      -8.43 |              0.9994 |                       99.94 |
| 2019-09-30     | Bull Market     | True             | True             |               181.57 |           171.793 | SHOP,QCOM,PDD     | 2019-09-30      | 2019-10-31    |             0.1098 |                      10.98 |              1.219  |                      121.9  |
| 2019-10-31     | Bull Market     | True             | True             |               189.52 |           176     | PDD,TSLA,KLAC     | 2019-10-31      | 2019-11-30    |            -0.033  |                      -3.3  |              1.1459 |                      114.59 |
| 2019-11-30     | Bull Market     | True             | True             |               197.23 |           179.65  | DXCM,PDD,LITE     | 2019-11-30      | 2019-12-31    |             0.0303 |                       3.03 |              1.2109 |                      121.09 |
| 2019-12-31     | Bull Market     | True             | True             |               204.9  |           183.585 | PDD,TSLA,ALNY     | 2019-12-31      | 2020-01-31    |             0.161  |                      16.1  |              1.5669 |                      156.69 |
| 2020-01-31     | Bull Market     | True             | True             |               211.12 |           187.493 | TSLA,PDD,DXCM     | 2020-01-31      | 2020-02-29    |             0.063  |                       6.3  |              1.7287 |                      172.87 |
| 2020-02-29     | Bull Market     | True             | True             |               198.33 |           189.177 | TSLA,DXCM,NVDA    | 2020-02-29      | 2020-03-31    |            -0.088  |                      -8.8  |              1.4887 |                      148.87 |
| 2020-03-31     | Bear Market     | False            | False            |               183.88 |           190.908 | CASH              | 2020-03-31      | 2020-04-30    |             0      |                       0    |              1.4887 |                      148.87 |
| 2020-04-30     | Bull Market     | True             | True             |               211.42 |           194.128 | TSLA,DXCM,SHOP    | 2020-04-30      | 2020-05-31    |             0.1317 |                      13.17 |              1.8164 |                      181.64 |
| 2020-05-31     | Bull Market     | True             | True             |               225.37 |           198.326 | TSLA,SHOP,ZS      | 2020-05-31      | 2020-06-30    |             0.2207 |                      22.07 |              2.4379 |                      243.79 |
| 2020-06-30     | Bull Market     | True             | True             |               239.54 |           204.288 | TSLA,DDOG,SHOP    | 2020-06-30      | 2020-07-31    |             0.1611 |                      16.11 |              2.9918 |                      299.18 |
| 2020-07-31     | Bull Market     | True             | True             |               257.14 |           211.846 | PDD,TSLA,ZS       | 2020-07-31      | 2020-08-31    |             0.2714 |                      27.14 |              4.0751 |                      407.51 |
| 2020-08-31     | Bull Market     | True             | True             |               285.28 |           221.422 | TSLA,ZS,PDD       | 2020-08-31      | 2020-09-30    |            -0.108  |                     -10.8  |              3.5272 |                      352.72 |
| 2020-09-30     | Bull Market     | True             | True             |               268.8  |           228.578 | TSLA,DDOG,SHOP    | 2020-09-30      | 2020-10-31    |            -0.1008 |                     -10.08 |              3.0707 |                      307.07 |
| 2020-10-31     | Bull Market     | True             | True             |               260.61 |           234.15  | TSLA,DDOG,MELI    | 2020-10-31      | 2020-11-30    |             0.2774 |                      27.74 |              4.1999 |                      419.99 |
| 2020-11-30     | Bull Market     | True             | True             |               289.87 |           242.025 | TSLA,MSTR,PDD     | 2020-11-30      | 2020-12-31    |             0.2189 |                      21.89 |              5.3383 |                      533.83 |
| 2020-12-31     | Bull Market     | True             | True             |               304.08 |           252.599 | MSTR,TSLA,PDD     | 2020-12-31      | 2021-01-31    |             0.2153 |                      21.53 |              6.703  |                      670.3  |
| 2021-01-31     | Bull Market     | True             | True             |               304.87 |           264.698 | MSTR,TSLA,WBD     | 2021-01-31      | 2021-02-28    |             0.1157 |                      11.57 |              7.5945 |                      759.45 |
| 2021-02-28     | Bull Market     | True             | True             |               304.47 |           274.003 | MSTR,WBD,PDD      | 2021-02-28      | 2021-03-31    |            -0.1646 |                     -16.46 |              6.1801 |                      618.01 |
| 2021-03-31     | Bull Market     | True             | True             |               309.69 |           282.435 | MSTR,PLTR,FANG    | 2021-03-31      | 2021-04-30    |             0.0232 |                       2.32 |              6.3465 |                      634.65 |
| 2021-04-30     | Bull Market     | True             | True             |               328    |           291.281 | MSTR,PLTR,FANG    | 2021-04-30      | 2021-05-31    |            -0.1014 |                     -10.14 |              5.6018 |                      560.18 |
| 2021-05-31     | Bull Market     | True             | True             |               324.06 |           297.972 | FANG,FTNT,WDC     | 2021-05-31      | 2021-06-30    |             0.0695 |                       6.95 |              6.0608 |                      606.08 |
| 2021-06-30     | Bull Market     | True             | True             |               344.35 |           303.879 | MSTR,FANG,AMAT    | 2021-06-30      | 2021-07-31    |            -0.0846 |                      -8.46 |              5.4635 |                      546.35 |
| 2021-07-31     | Bull Market     | True             | True             |               354.2  |           312.419 | FTNT,NVDA,GOOG    | 2021-07-31      | 2021-08-31    |             0.1272 |                      12.72 |              6.2855 |                      628.55 |
| 2021-08-31     | Bull Market     | True             | True             |               369.14 |           323.272 | FTNT,NVDA,REGN    | 2021-08-31      | 2021-09-30    |            -0.0831 |                      -8.31 |              5.6804 |                      568.04 |
| 2021-09-30     | Bull Market     | True             | True             |               348.16 |           329.102 | DDOG,FTNT,NVDA    | 2021-09-30      | 2021-10-31    |             0.1892 |                      18.92 |              6.9445 |                      694.45 |
| 2021-10-31     | Bull Market     | True             | True             |               375.54 |           336.248 | DDOG,APP,NVDA     | 2021-10-31      | 2021-11-30    |             0.0909 |                       9.09 |              7.6665 |                      766.65 |
| 2021-11-30     | Bull Market     | True             | True             |               383.04 |           344.065 | NVDA,AMD,DDOG     | 2021-11-30      | 2021-12-31    |            -0.0641 |                      -6.41 |              7.1113 |                      711.13 |
| 2021-12-31     | Bull Market     | True             | True             |               387.46 |           352.364 | DDOG,TSLA,AMD     | 2021-12-31      | 2022-01-31    |            -0.1664 |                     -16.64 |              5.7613 |                      576.13 |
| 2022-01-31     | Bear Market     | False            | False            |               353.57 |           356.751 | CASH              | 2022-01-31      | 2022-02-28    |             0      |                       0    |              5.7613 |                      576.13 |
| 2022-02-28     | Bear Market     | False            | False            |               337.74 |           357.726 | CASH              | 2022-02-28      | 2022-03-31    |             0      |                       0    |              5.7613 |                      576.13 |
| 2022-03-31     | Bear Market     | False            | False            |               353.51 |           360.671 | CASH              | 2022-03-31      | 2022-04-30    |             0      |                       0    |              5.7613 |                      576.13 |
| 2022-04-30     | Bear Market     | False            | False            |               305.44 |           356.78  | CASH              | 2022-04-30      | 2022-05-31    |             0      |                       0    |              5.7613 |                      576.13 |
| 2022-05-31     | Bear Market     | False            | False            |               300.6  |           351.42  | CASH              | 2022-05-31      | 2022-06-30    |             0      |                       0    |              5.7613 |                      576.13 |
| 2022-06-30     | Bear Market     | False            | False            |               273.82 |           341.888 | CASH              | 2022-06-30      | 2022-07-31    |             0      |                       0    |              5.7613 |                      576.13 |
| 2022-07-31     | Bear Market     | False            | False            |               308.19 |           337.89  | CASH              | 2022-07-31      | 2022-08-31    |             0      |                       0    |              5.7613 |                      576.13 |
| 2022-08-31     | Bear Market     | False            | False            |               292.37 |           329.573 | CASH              | 2022-08-31      | 2022-09-30    |             0      |                       0    |              5.7613 |                      576.13 |
| 2022-09-30     | Bear Market     | False            | False            |               261.57 |           317.426 | CASH              | 2022-09-30      | 2022-10-31    |             0      |                       0    |              5.7613 |                      576.13 |
| 2022-10-31     | Bear Market     | False            | False            |               272.03 |           305.884 | CASH              | 2022-10-31      | 2022-11-30    |             0      |                       0    |              5.7613 |                      576.13 |
| 2022-11-30     | Bear Market     | False            | False            |               287.11 |           299.239 | CASH              | 2022-11-30      | 2022-12-31    |             0      |                       0    |              5.7613 |                      576.13 |
| 2022-12-31     | Bear Market     | False            | False            |               261.23 |           291.588 | CASH              | 2022-12-31      | 2023-01-31    |             0      |                       0    |              5.7613 |                      576.13 |
| 2023-01-31     | Bull Market     | True             | True             |               289.04 |           285.141 | PDD,AXON,ALNY     | 2023-01-31      | 2023-02-28    |            -0.078  |                      -7.8  |              5.2338 |                      523.38 |
| 2023-02-28     | Bull Market     | True             | True             |               288    |           283.397 | AXON,NVDA,MSTR    | 2023-02-28      | 2023-03-31    |             0.1446 |                      14.46 |              6.135  |                      613.5  |
| 2023-03-31     | Bull Market     | True             | True             |               315.34 |           284.871 | NVDA,AXON,SHOP    | 2023-03-31      | 2023-04-30    |            -0.0178 |                      -1.78 |              6.0084 |                      600.84 |
| 2023-04-30     | Bull Market     | True             | True             |               316.94 |           289.182 | META,NVDA,MSTR    | 2023-04-30      | 2023-05-31    |             0.1278 |                      12.78 |              6.9043 |                      690.43 |
| 2023-05-31     | Bull Market     | True             | True             |               341.92 |           292.556 | PLTR,NVDA,META    | 2023-05-31      | 2023-06-30    |             0.0815 |                       8.15 |              7.5484 |                      754.84 |
| 2023-06-30     | Bull Market     | True             | True             |               363.48 |           299.667 | NVDA,PLTR,MSTR    | 2023-06-30      | 2023-07-31    |             0.2259 |                      22.59 |              9.4792 |                      947.92 |
| 2023-07-31     | Bull Market     | True             | True             |               377.51 |           311.261 | PLTR,APP,NVDA     | 2023-07-31      | 2023-08-31    |             0.0626 |                       6.26 |             10.1348 |                     1013.48 |
| 2023-08-31     | Bull Market     | True             | True             |               371.91 |           321.248 | APP,PLTR,NVDA     | 2023-08-31      | 2023-09-30    |            -0.042  |                      -4.2  |              9.6674 |                      966.74 |
| 2023-09-30     | Bull Market     | True             | True             |               353.02 |           327.839 | APP,PLTR,NVDA     | 2023-09-30      | 2023-10-31    |            -0.0752 |                      -7.52 |              8.8653 |                      886.53 |
| 2023-10-31     | Bull Market     | True             | True             |               345.73 |           336.288 | PLTR,APP,ZS       | 2023-10-31      | 2023-11-30    |             0.2093 |                      20.93 |             10.9305 |                     1093.05 |
| 2023-11-30     | Bull Market     | True             | True             |               383.13 |           345.698 | PDD,MSTR,APP      | 2023-11-30      | 2023-12-31    |             0.1077 |                      10.77 |             12.2155 |                     1221.55 |
| 2023-12-31     | Bull Market     | True             | True             |               404.54 |           357.351 | PDD,MSTR,CRWD     | 2023-12-31      | 2024-01-31    |            -0.0646 |                      -6.46 |             11.3621 |                     1136.21 |
| 2024-01-31     | Bull Market     | True             | True             |               411.9  |           367.007 | CRWD,PDD,AMD      | 2024-01-31      | 2024-02-29    |             0.0793 |                       7.93 |             12.3427 |                     1234.27 |
| 2024-02-29     | Bull Market     | True             | True             |               433.66 |           378.679 | MSTR,CRWD,PLTR    | 2024-02-29      | 2024-03-31    |             0.191  |                      19.1  |             14.8911 |                     1489.11 |
| 2024-03-31     | Bull Market     | True             | True             |               439.19 |           388.405 | MSTR,ARM,NVDA     | 2024-03-31      | 2024-04-30    |            -0.2031 |                     -20.31 |             11.6641 |                     1166.41 |
| 2024-04-30     | Bull Market     | True             | True             |               419.98 |           394.055 | MSTR,ARM,NVDA     | 2024-04-30      | 2024-05-31    |             0.297  |                      29.7  |             15.4256 |                     1542.56 |
| 2024-05-31     | Bull Market     | True             | True             |               445.81 |           400.886 | MSTR,INSM,ARM     | 2024-05-31      | 2024-06-30    |             0.1594 |                      15.94 |             18.0442 |                     1804.42 |
| 2024-06-30     | Bull Market     | True             | True             |               474.66 |           411.16  | MSTR,INSM,ARM     | 2024-06-30      | 2024-07-31    |             0.0463 |                       4.63 |             18.9264 |                     1892.64 |
| 2024-07-31     | Bull Market     | True             | True             |               466.69 |           422.528 | MSTR,INSM,ARM     | 2024-07-31      | 2024-08-31    |            -0.069  |                      -6.9  |             17.5518 |                     1755.18 |
| 2024-08-31     | Bull Market     | True             | True             |               471.85 |           435.14  | INSM,ALNY,MSTR    | 2024-08-31      | 2024-09-30    |             0.0916 |                       9.16 |             19.2513 |                     1925.13 |
| 2024-09-30     | Bull Market     | True             | True             |               484.21 |           445.248 | INSM,ALNY,APP     | 2024-09-30      | 2024-10-31    |             0.0628 |                       6.28 |             20.5235 |                     2052.35 |
| 2024-10-31     | Bull Market     | True             | True             |               480.03 |           452.797 | INSM,MSTR,APP     | 2024-10-31      | 2024-11-30    |             0.5633 |                      56.33 |             32.6476 |                     3264.76 |
| 2024-11-30     | Bull Market     | True             | True             |               505.71 |           462.179 | APP,PLTR,MSTR     | 2024-11-30      | 2024-12-31    |            -0.0545 |                      -5.45 |             30.8144 |                     3081.44 |
| 2024-12-31     | Bull Market     | True             | True             |               508.01 |           469.614 | APP,PLTR,MSTR     | 2024-12-31      | 2025-01-31    |             0.1293 |                      12.93 |             34.9288 |                     3492.88 |
| 2025-01-31     | Bull Market     | True             | True             |               519    |           477.596 | APP,PLTR,MSTR     | 2025-01-31      | 2025-02-28    |            -0.1087 |                     -10.87 |             31.0218 |                     3102.18 |
| 2025-02-28     | Bull Market     | True             | True             |               504.97 |           486.095 | APP,PLTR,MSTR     | 2025-02-28      | 2025-03-31    |            -0.0214 |                      -2.14 |             30.3374 |                     3033.74 |
| 2025-03-31     | Bear Market     | False            | False            |               466.66 |           488.179 | CASH              | 2025-03-31      | 2025-04-30    |             0      |                       0    |             30.3374 |                     3033.74 |
| 2025-04-30     | Bear Market     | False            | False            |               473.18 |           488.031 | CASH              | 2025-04-30      | 2025-05-31    |             0      |                       0    |             30.3374 |                     3033.74 |
| 2025-05-31     | Bull Market     | True             | True             |               516.61 |           493.023 | PLTR,AVGO,CRWD    | 2025-05-31      | 2025-06-30    |             0.0854 |                       8.54 |             33.0151 |                     3301.51 |
| 2025-06-30     | Bull Market     | True             | True             |               549.6  |           500.799 | PLTR,STX,ZS       | 2025-06-30      | 2025-07-31    |             0.053  |                       5.3  |             34.8186 |                     3481.86 |
| 2025-07-31     | Bull Market     | True             | True             |               562.92 |           508.669 | PLTR,STX,WDC      | 2025-07-31      | 2025-08-31    |             0.0256 |                       2.56 |             35.7354 |                     3573.54 |
| 2025-08-31     | Bull Market     | True             | True             |               568.29 |           517.495 | LITE,PLTR,ALNY    | 2025-08-31      | 2025-09-30    |             0.1368 |                      13.68 |             40.7614 |                     4076.14 |
| 2025-09-30     | Bull Market     | True             | True             |               598.84 |           526.808 | SNDK,WDC,APP      | 2025-09-30      | 2025-10-31    |             0.3049 |                      30.49 |             53.4939 |                     5349.39 |
| 2025-10-31     | Bull Market     | True             | True             |               627.47 |           538.754 | SNDK,WDC,LITE     | 2025-10-31      | 2025-11-30    |             0.2736 |                      27.36 |             68.4019 |                     6840.19 |
| 2025-11-30     | Bull Market     | True             | True             |               617.67 |           548.621 | SNDK,LITE,WDC     | 2025-11-30      | 2025-12-31    |             0.0841 |                       8.41 |             74.2385 |                     7423.85 |
| 2025-12-31     | Bull Market     | True             | True             |               613.54 |           559.478 | SNDK,LITE,WDC     | 2025-12-31      | 2026-01-31    |             0.6477 |                      64.77 |            122.972  |                    12297.2  |
| 2026-01-31     | Bull Market     | True             | True             |               621.09 |           574.921 | SNDK,MU,LITE      | 2026-01-31      | 2026-02-28    |             0.2951 |                      29.51 |            159.556  |                    15955.6  |
| 2026-02-28     | Bull Market     | True             | True             |               606.53 |           588.255 | SNDK,LITE,WDC     | 2026-02-28      | 2026-03-31    |            -0.01   |                      -1    |            157.958  |                    15795.8  |
| 2026-03-31     | Bear Market     | False            | False            |               577.18 |           594.312 | CASH              | 2026-03-31      | 2026-04-30    |             0      |                       0    |            157.958  |                    15795.8  |
| 2026-04-30     | Bull Market     | True             | True             |               667.74 |           606.126 | SNDK,LITE,WDC     | 2026-04-30      | 2026-05-31    |             0.2386 |                      23.86 |            195.887  |                    19588.7  |

The full monthly return history is saved in:

```text
nasdaq100_mean_momentum_backtest_returns.csv
```

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
