# Nasdaq-100 Six-Month Mean Momentum Strategy

This repository builds a rule-based momentum ranking and backtesting system for Nasdaq-100 stocks.

The core idea is simple:

> At the beginning of each month, rank Nasdaq-100 stocks by their average monthly return over the previous six months, buy the top three stocks, and hold them for the following month.


Last updated: **2026-05-30 03:55:57 UTC**

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

| strategy_name                            | start_date   | end_date   |   lookback_months |   top_n |   total_return_percent |   annualized_return_percent |   annualized_volatility_percent |   sharpe_ratio_without_risk_free_rate |   max_drawdown_percent |   win_rate_percent |   number_of_months |
|:-----------------------------------------|:-------------|:-----------|------------------:|--------:|-----------------------:|----------------------------:|--------------------------------:|--------------------------------------:|-----------------------:|-------------------:|-------------------:|
| Nasdaq-100 Top 3 Six-Month Mean Momentum | 2016-07-31   | 2026-05-31 |                 6 |       3 |                75610.2 |                       96.24 |                           50.37 |                               1.91089 |                 -29.15 |              61.86 |                118 |

---

## Backtest Monthly Return Statistics

The following table summarizes the distribution of monthly strategy returns.

| metric                         |   value |
|:-------------------------------|--------:|
| Total months                   |  118    |
| Winning months                 |   73    |
| Losing months                  |   45    |
| Flat months                    |    0    |
| Win rate percent               |   61.86 |
| Average monthly return percent |    6.69 |
| Average winning month percent  |   14.69 |
| Average losing month percent   |   -6.28 |
| Best month percent             |   64.77 |
| Worst month percent            |  -20.31 |
| Monthly volatility percent     |   14.54 |
| Profit loss ratio              |    2.34 |

---

## Full Monthly Backtest Returns

The following table shows the full monthly strategy return history.

| ranking_date   | selected_stocks   | holding_start   | holding_end   |   portfolio_return |   portfolio_return_percent |   cumulative_return |   cumulative_return_percent |
|:---------------|:------------------|:----------------|:--------------|-------------------:|---------------------------:|--------------------:|----------------------------:|
| 2016-07-31     | AMD,NVDA,AXON     | 2016-07-31      | 2016-08-31    |             0.03   |                       3    |              0.03   |                        3    |
| 2016-08-31     | AMD,NVDA,SHOP     | 2016-08-31      | 2016-09-30    |             0.0295 |                       2.95 |              0.0604 |                        6.04 |
| 2016-09-30     | AMD,NVDA,MU       | 2016-09-30      | 2016-10-31    |             0.0167 |                       1.67 |              0.0781 |                        7.81 |
| 2016-10-31     | AMD,NVDA,STX      | 2016-10-31      | 2016-11-30    |             0.2329 |                      23.29 |              0.3292 |                       32.92 |
| 2016-11-30     | AMD,NVDA,STX      | 2016-11-30      | 2016-12-31    |             0.1326 |                      13.26 |              0.5055 |                       50.55 |
| 2016-12-31     | NVDA,AMD,LITE     | 2016-12-31      | 2017-01-31    |            -0.0269 |                      -2.69 |              0.4649 |                       46.49 |
| 2017-01-31     | NVDA,MU,WDC       | 2017-01-31      | 2017-02-28    |            -0.0443 |                      -4.43 |              0.4    |                       40    |
| 2017-02-28     | AMD,CSX,WDC       | 2017-02-28      | 2017-03-31    |             0.015  |                       1.5  |              0.421  |                       42.1  |
| 2017-03-31     | AMD,MU,NVDA       | 2017-03-31      | 2017-04-30    |            -0.057  |                      -5.7  |              0.3401 |                       34.01 |
| 2017-04-30     | AMD,SHOP,CSX      | 2017-04-30      | 2017-05-31    |             0.0401 |                       4.01 |              0.3938 |                       39.38 |
| 2017-05-31     | SHOP,TSLA,MELI    | 2017-05-31      | 2017-06-30    |            -0.027  |                      -2.7  |              0.3561 |                       35.61 |
| 2017-06-30     | ALNY,SHOP,VRTX    | 2017-06-30      | 2017-07-31    |             0.0928 |                       9.28 |              0.4819 |                       48.19 |
| 2017-07-31     | ALNY,SHOP,VRTX    | 2017-07-31      | 2017-08-31    |             0.0981 |                       9.81 |              0.6274 |                       62.74 |
| 2017-08-31     | SHOP,VRTX,TTWO    | 2017-08-31      | 2017-09-30    |             0.0142 |                       1.42 |              0.6505 |                       65.05 |
| 2017-09-30     | INSM,ALNY,TTWO    | 2017-09-30      | 2017-10-31    |            -0.0051 |                      -0.51 |              0.6422 |                       64.22 |
| 2017-10-31     | INSM,ALNY,NVDA    | 2017-10-31      | 2017-11-30    |             0.0767 |                       7.67 |              0.7682 |                       76.82 |
| 2017-11-30     | INSM,ALNY,TTWO    | 2017-11-30      | 2017-12-31    |            -0.024  |                      -2.4  |              0.7258 |                       72.58 |
| 2017-12-31     | INSM,ALNY,TTWO    | 2017-12-31      | 2018-01-31    |            -0.0024 |                      -0.24 |              0.7217 |                       72.17 |
| 2018-01-31     | INSM,STX,ALNY     | 2018-01-31      | 2018-02-28    |            -0.0522 |                      -5.22 |              0.6319 |                       63.19 |
| 2018-02-28     | INSM,STX,NFLX     | 2018-02-28      | 2018-03-31    |             0.0171 |                       1.71 |              0.6597 |                       65.97 |
| 2018-03-31     | STX,AXON,NFLX     | 2018-03-31      | 2018-04-30    |             0.0384 |                       3.84 |              0.7234 |                       72.34 |
| 2018-04-30     | AXON,DXCM,NFLX    | 2018-04-30      | 2018-05-31    |             0.2815 |                      28.15 |              1.2086 |                      120.86 |
| 2018-05-31     | AXON,NFLX,DXCM    | 2018-05-31      | 2018-06-30    |             0.0616 |                       6.16 |              1.3447 |                      134.47 |
| 2018-06-30     | AXON,NFLX,DXCM    | 2018-06-30      | 2018-07-31    |            -0.0204 |                      -2.04 |              1.2969 |                      129.69 |
| 2018-07-31     | AXON,DXCM,AMD     | 2018-07-31      | 2018-08-31    |             0.2986 |                      29.86 |              1.9827 |                      198.27 |
| 2018-08-31     | DXCM,AMD,AXON     | 2018-08-31      | 2018-09-30    |             0.0735 |                       7.35 |              2.2019 |                      220.19 |
| 2018-09-30     | AMD,DXCM,AXON     | 2018-09-30      | 2018-10-31    |            -0.1934 |                     -19.34 |              1.5825 |                      158.25 |
| 2018-10-31     | AMD,DXCM,AXON     | 2018-10-31      | 2018-11-30    |            -0.05   |                      -5    |              1.4534 |                      145.34 |
| 2018-11-30     | AMD,DXCM,ZS       | 2018-11-30      | 2018-12-31    |            -0.0701 |                      -7.01 |              1.2815 |                      128.15 |
| 2018-12-31     | AMD,DXCM,WDAY     | 2018-12-31      | 2019-01-31    |             0.2121 |                      21.21 |              1.7655 |                      176.55 |
| 2019-01-31     | AMD,DXCM,PDD      | 2019-01-31      | 2019-02-28    |            -0.0077 |                      -0.77 |              1.7442 |                      174.42 |
| 2019-02-28     | INSM,PDD,MELI     | 2019-02-28      | 2019-03-31    |            -0.0282 |                      -2.82 |              1.6668 |                      166.68 |
| 2019-03-31     | INSM,ZS,MELI      | 2019-03-31      | 2019-04-30    |            -0.0121 |                      -1.21 |              1.6346 |                      163.46 |
| 2019-04-30     | INSM,ZS,SHOP      | 2019-04-30      | 2019-05-31    |            -0.0237 |                      -2.37 |              1.5721 |                      157.21 |
| 2019-05-31     | ZS,SHOP,INSM      | 2019-05-31      | 2019-06-30    |             0.0887 |                       8.87 |              1.8001 |                      180.01 |
| 2019-06-30     | INSM,SHOP,MELI    | 2019-06-30      | 2019-07-31    |            -0.0226 |                      -2.26 |              1.7369 |                      173.69 |
| 2019-07-31     | SHOP,ZS,MELI      | 2019-07-31      | 2019-08-31    |            -0.005  |                      -0.5  |              1.7232 |                      172.32 |
| 2019-08-31     | SHOP,QCOM,TTWO    | 2019-08-31      | 2019-09-30    |            -0.0843 |                      -8.43 |              1.4936 |                      149.36 |
| 2019-09-30     | SHOP,QCOM,PDD     | 2019-09-30      | 2019-10-31    |             0.1098 |                      10.98 |              1.7674 |                      176.74 |
| 2019-10-31     | PDD,TSLA,KLAC     | 2019-10-31      | 2019-11-30    |            -0.033  |                      -3.3  |              1.6762 |                      167.62 |
| 2019-11-30     | DXCM,PDD,LITE     | 2019-11-30      | 2019-12-31    |             0.0303 |                       3.03 |              1.7573 |                      175.73 |
| 2019-12-31     | PDD,TSLA,ALNY     | 2019-12-31      | 2020-01-31    |             0.161  |                      16.1  |              2.2013 |                      220.13 |
| 2020-01-31     | TSLA,PDD,DXCM     | 2020-01-31      | 2020-02-29    |             0.063  |                       6.3  |              2.4031 |                      240.31 |
| 2020-02-29     | TSLA,DXCM,NVDA    | 2020-02-29      | 2020-03-31    |            -0.088  |                      -8.8  |              2.1038 |                      210.38 |
| 2020-03-31     | TSLA,DXCM,REGN    | 2020-03-31      | 2020-04-30    |             0.2713 |                      27.13 |              2.9459 |                      294.59 |
| 2020-04-30     | TSLA,DXCM,SHOP    | 2020-04-30      | 2020-05-31    |             0.1317 |                      13.17 |              3.4655 |                      346.55 |
| 2020-05-31     | TSLA,SHOP,ZS      | 2020-05-31      | 2020-06-30    |             0.2207 |                      22.07 |              4.451  |                      445.1  |
| 2020-06-30     | TSLA,DDOG,SHOP    | 2020-06-30      | 2020-07-31    |             0.1611 |                      16.11 |              5.3291 |                      532.91 |
| 2020-07-31     | PDD,TSLA,ZS       | 2020-07-31      | 2020-08-31    |             0.2714 |                      27.14 |              7.0468 |                      704.68 |
| 2020-08-31     | TSLA,ZS,PDD       | 2020-08-31      | 2020-09-30    |            -0.108  |                     -10.8  |              6.1781 |                      617.81 |
| 2020-09-30     | TSLA,DDOG,SHOP    | 2020-09-30      | 2020-10-31    |            -0.1008 |                     -10.08 |              5.4542 |                      545.42 |
| 2020-10-31     | TSLA,DDOG,MELI    | 2020-10-31      | 2020-11-30    |             0.2774 |                      27.74 |              7.2447 |                      724.47 |
| 2020-11-30     | TSLA,MSTR,PDD     | 2020-11-30      | 2020-12-31    |             0.2189 |                      21.89 |              9.0496 |                      904.96 |
| 2020-12-31     | MSTR,TSLA,PDD     | 2020-12-31      | 2021-01-31    |             0.2153 |                      21.53 |             11.2134 |                     1121.34 |
| 2021-01-31     | MSTR,TSLA,WBD     | 2021-01-31      | 2021-02-28    |             0.1157 |                      11.57 |             12.6268 |                     1262.68 |
| 2021-02-28     | MSTR,WBD,PDD      | 2021-02-28      | 2021-03-31    |            -0.1646 |                     -16.46 |             10.3843 |                     1038.43 |
| 2021-03-31     | MSTR,PLTR,FANG    | 2021-03-31      | 2021-04-30    |             0.0232 |                       2.32 |             10.6481 |                     1064.81 |
| 2021-04-30     | MSTR,PLTR,FANG    | 2021-04-30      | 2021-05-31    |            -0.1014 |                     -10.14 |              9.4674 |                      946.74 |
| 2021-05-31     | FANG,FTNT,WDC     | 2021-05-31      | 2021-06-30    |             0.0695 |                       6.95 |             10.1951 |                     1019.51 |
| 2021-06-30     | MSTR,FANG,AMAT    | 2021-06-30      | 2021-07-31    |            -0.0846 |                      -8.46 |              9.248  |                      924.8  |
| 2021-07-31     | FTNT,NVDA,GOOG    | 2021-07-31      | 2021-08-31    |             0.1272 |                      12.72 |             10.5513 |                     1055.13 |
| 2021-08-31     | FTNT,NVDA,REGN    | 2021-08-31      | 2021-09-30    |            -0.0831 |                      -8.31 |              9.5919 |                      959.19 |
| 2021-09-30     | DDOG,FTNT,NVDA    | 2021-09-30      | 2021-10-31    |             0.1892 |                      18.92 |             11.5962 |                     1159.62 |
| 2021-10-31     | DDOG,APP,NVDA     | 2021-10-31      | 2021-11-30    |             0.0909 |                       9.09 |             12.7411 |                     1274.11 |
| 2021-11-30     | NVDA,AMD,DDOG     | 2021-11-30      | 2021-12-31    |            -0.0641 |                      -6.41 |             11.8608 |                     1186.08 |
| 2021-12-31     | DDOG,TSLA,AMD     | 2021-12-31      | 2022-01-31    |            -0.1664 |                     -16.64 |              9.7202 |                      972.02 |
| 2022-01-31     | FANG,TSLA,DDOG    | 2022-01-31      | 2022-02-28    |             0.0422 |                       4.22 |             10.1724 |                     1017.24 |
| 2022-02-28     | FANG,BKR,PANW     | 2022-02-28      | 2022-03-31    |             0.0946 |                       9.46 |             11.2294 |                     1122.94 |
| 2022-03-31     | TSLA,BKR,FANG     | 2022-03-31      | 2022-04-30    |            -0.1397 |                     -13.97 |              9.5208 |                      952.08 |
| 2022-04-30     | VRTX,BKR,EXC      | 2022-04-30      | 2022-05-31    |             0.069  |                       6.9  |             10.2468 |                     1024.68 |
| 2022-05-31     | BKR,FANG,VRTX     | 2022-05-31      | 2022-06-30    |            -0.1173 |                     -11.73 |              8.928  |                      892.8  |
| 2022-06-30     | BKR,VRTX,FANG     | 2022-06-30      | 2022-07-31    |            -0.0194 |                      -1.94 |              8.735  |                      873.5  |
| 2022-07-31     | CEG,TMUS,CDNS     | 2022-07-31      | 2022-08-31    |             0.0589 |                       5.89 |              9.3083 |                      930.83 |
| 2022-08-31     | CEG,PDD,ALNY      | 2022-08-31      | 2022-09-30    |            -0.0447 |                      -4.47 |              8.8472 |                      884.72 |
| 2022-09-30     | PDD,CEG,ALNY      | 2022-09-30      | 2022-10-31    |             0.016  |                       1.6  |              9.005  |                      900.5  |
| 2022-10-31     | ALNY,CEG,NFLX     | 2022-10-31      | 2022-11-30    |             0.0431 |                       4.31 |              9.4364 |                      943.64 |
| 2022-11-30     | PDD,AXON,ALNY     | 2022-11-30      | 2022-12-31    |            -0.009  |                      -0.9  |              9.3425 |                      934.25 |
| 2022-12-31     | AXON,NFLX,ALNY    | 2022-12-31      | 2023-01-31    |             0.1102 |                      11.02 |             10.482  |                     1048.2  |
| 2023-01-31     | PDD,AXON,ALNY     | 2023-01-31      | 2023-02-28    |            -0.078  |                      -7.8  |              9.5861 |                      958.61 |
| 2023-02-28     | AXON,NVDA,MSTR    | 2023-02-28      | 2023-03-31    |             0.1446 |                      14.46 |             11.1167 |                     1111.67 |
| 2023-03-31     | NVDA,AXON,SHOP    | 2023-03-31      | 2023-04-30    |            -0.0178 |                      -1.78 |             10.9016 |                     1090.16 |
| 2023-04-30     | META,NVDA,MSTR    | 2023-04-30      | 2023-05-31    |             0.1278 |                      12.78 |             12.423  |                     1242.3  |
| 2023-05-31     | PLTR,NVDA,META    | 2023-05-31      | 2023-06-30    |             0.0815 |                       8.15 |             13.5168 |                     1351.68 |
| 2023-06-30     | NVDA,PLTR,MSTR    | 2023-06-30      | 2023-07-31    |             0.2259 |                      22.59 |             16.7958 |                     1679.58 |
| 2023-07-31     | PLTR,APP,NVDA     | 2023-07-31      | 2023-08-31    |             0.0626 |                       6.26 |             17.909  |                     1790.9  |
| 2023-08-31     | APP,PLTR,NVDA     | 2023-08-31      | 2023-09-30    |            -0.042  |                      -4.2  |             17.1153 |                     1711.53 |
| 2023-09-30     | APP,PLTR,NVDA     | 2023-09-30      | 2023-10-31    |            -0.0752 |                      -7.52 |             15.7531 |                     1575.31 |
| 2023-10-31     | PLTR,APP,ZS       | 2023-10-31      | 2023-11-30    |             0.2093 |                      20.93 |             19.2602 |                     1926.02 |
| 2023-11-30     | PDD,MSTR,APP      | 2023-11-30      | 2023-12-31    |             0.1077 |                      10.77 |             21.4424 |                     2144.24 |
| 2023-12-31     | PDD,MSTR,CRWD     | 2023-12-31      | 2024-01-31    |            -0.0646 |                      -6.46 |             19.9932 |                     1999.32 |
| 2024-01-31     | CRWD,PDD,AMD      | 2024-01-31      | 2024-02-29    |             0.0793 |                       7.93 |             21.6585 |                     2165.85 |
| 2024-02-29     | MSTR,CRWD,PLTR    | 2024-02-29      | 2024-03-31    |             0.191  |                      19.1  |             25.9861 |                     2598.61 |
| 2024-03-31     | MSTR,ARM,NVDA     | 2024-03-31      | 2024-04-30    |            -0.2031 |                     -20.31 |             20.5061 |                     2050.61 |
| 2024-04-30     | MSTR,ARM,NVDA     | 2024-04-30      | 2024-05-31    |             0.297  |                      29.7  |             26.8939 |                     2689.39 |
| 2024-05-31     | MSTR,INSM,ARM     | 2024-05-31      | 2024-06-30    |             0.1594 |                      15.94 |             31.3407 |                     3134.07 |
| 2024-06-30     | MSTR,INSM,ARM     | 2024-06-30      | 2024-07-31    |             0.0463 |                       4.63 |             32.8389 |                     3283.89 |
| 2024-07-31     | MSTR,INSM,ARM     | 2024-07-31      | 2024-08-31    |            -0.069  |                      -6.9  |             30.5045 |                     3050.45 |
| 2024-08-31     | INSM,ALNY,MSTR    | 2024-08-31      | 2024-09-30    |             0.0916 |                       9.16 |             33.3905 |                     3339.05 |
| 2024-09-30     | INSM,ALNY,APP     | 2024-09-30      | 2024-10-31    |             0.0628 |                       6.28 |             35.551  |                     3555.1  |
| 2024-10-31     | INSM,MSTR,APP     | 2024-10-31      | 2024-11-30    |             0.5633 |                      56.33 |             56.14   |                     5614    |
| 2024-11-30     | APP,PLTR,MSTR     | 2024-11-30      | 2024-12-31    |            -0.0545 |                      -5.45 |             53.027  |                     5302.7  |
| 2024-12-31     | APP,PLTR,MSTR     | 2024-12-31      | 2025-01-31    |             0.1293 |                      12.93 |             60.014  |                     6001.4  |
| 2025-01-31     | APP,PLTR,MSTR     | 2025-01-31      | 2025-02-28    |            -0.1087 |                     -10.87 |             53.3791 |                     5337.91 |
| 2025-02-28     | APP,PLTR,MSTR     | 2025-02-28      | 2025-03-31    |            -0.0214 |                      -2.14 |             52.217  |                     5221.7  |
| 2025-03-31     | APP,PLTR,MSTR     | 2025-03-31      | 2025-04-30    |             0.2461 |                      24.61 |             65.3134 |                     6531.34 |
| 2025-04-30     | PLTR,APP,MSTR     | 2025-04-30      | 2025-05-31    |             0.1809 |                      18.09 |             77.3127 |                     7731.27 |
| 2025-05-31     | PLTR,AVGO,CRWD    | 2025-05-31      | 2025-06-30    |             0.0854 |                       8.54 |             84.0043 |                     8400.43 |
| 2025-06-30     | PLTR,STX,ZS       | 2025-06-30      | 2025-07-31    |             0.053  |                       5.3  |             88.5112 |                     8851.12 |
| 2025-07-31     | PLTR,STX,WDC      | 2025-07-31      | 2025-08-31    |             0.0256 |                       2.56 |             90.8023 |                     9080.23 |
| 2025-08-31     | LITE,PLTR,ALNY    | 2025-08-31      | 2025-09-30    |             0.1368 |                      13.68 |            103.362  |                    10336.2  |
| 2025-09-30     | SNDK,WDC,APP      | 2025-09-30      | 2025-10-31    |             0.3049 |                      30.49 |            135.181  |                    13518.1  |
| 2025-10-31     | SNDK,WDC,LITE     | 2025-10-31      | 2025-11-30    |             0.2736 |                      27.36 |            172.436  |                    17243.6  |
| 2025-11-30     | SNDK,LITE,WDC     | 2025-11-30      | 2025-12-31    |             0.0841 |                       8.41 |            187.022  |                    18702.2  |
| 2025-12-31     | SNDK,LITE,WDC     | 2025-12-31      | 2026-01-31    |             0.6477 |                      64.77 |            308.808  |                    30880.8  |
| 2026-01-31     | SNDK,MU,LITE      | 2026-01-31      | 2026-02-28    |             0.2951 |                      29.51 |            400.232  |                    40023.2  |
| 2026-02-28     | SNDK,LITE,WDC     | 2026-02-28      | 2026-03-31    |            -0.01   |                      -1    |            396.239  |                    39623.9  |
| 2026-03-31     | SNDK,LITE,WDC     | 2026-03-31      | 2026-04-30    |             0.5387 |                      53.87 |            610.251  |                    61025.1  |
| 2026-04-30     | SNDK,LITE,WDC     | 2026-04-30      | 2026-05-31    |             0.2386 |                      23.86 |            756.102  |                    75610.2  |

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

| metric                              |   original_strategy |   with_market_regime_filter |   difference |
|:------------------------------------|--------------------:|----------------------------:|-------------:|
| total_return_percent                |         75610.2     |                 19588.7     | -56021.4     |
| annualized_return_percent           |            96.2435  |                    73.5388  |    -22.7047  |
| annualized_volatility_percent       |            50.3658  |                    46.6504  |     -3.71538 |
| sharpe_ratio_without_risk_free_rate |             1.91089 |                     1.57638 |     -0.33451 |
| max_drawdown_percent                |           -29.1543  |                   -32.6792  |     -3.52489 |
| win_rate_percent                    |            61.8644  |                    49.5652  |    -12.2992  |
| number_of_months                    |           118       |                   115       |     -3       |

---

## Market Regime Backtest Summary

The following table shows the summary statistics of the strategy after adding the Nasdaq market regime filter.

| strategy_name                                                      | market_index_ticker   |   market_trend_months | start_date   | end_date   |   lookback_months |   top_n |   bull_market_months |   bear_market_months |   trading_months |   cash_months |   total_return_percent |   annualized_return_percent |   annualized_volatility_percent |   sharpe_ratio_without_risk_free_rate |   max_drawdown_percent |   win_rate_percent |   number_of_months |
|:-------------------------------------------------------------------|:----------------------|----------------------:|:-------------|:-----------|------------------:|--------:|---------------------:|---------------------:|-----------------:|--------------:|-----------------------:|----------------------------:|--------------------------------:|--------------------------------------:|-----------------------:|-------------------:|-------------------:|
| Nasdaq-100 Top 3 Six-Month Mean Momentum With Market Regime Filter | QQQ                   |                    10 | 2016-10-31   | 2026-05-31 |                 6 |       3 |                   94 |                   21 |               94 |            21 |                19588.7 |                       73.54 |                           46.65 |                               1.57638 |                 -32.68 |              49.57 |                115 |

---

## Market Regime Monthly Return Statistics

The following table summarizes the distribution of monthly strategy returns after applying the market regime filter.

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

## Bull Market Months

The following table lists all months classified as bull-market months by the Nasdaq market regime filter.

| ranking_date   | market_regime   |   market_index_price |   market_index_ma | selected_stocks   | holding_start   | holding_end   |   portfolio_return_percent |   cumulative_return_percent |
|:---------------|:----------------|---------------------:|------------------:|:------------------|:----------------|:--------------|---------------------------:|----------------------------:|
| 2016-10-31     | Bull Market     |               109.56 |            103.26 | AMD,NVDA,STX      | 2016-10-31      | 2016-11-30    |                      23.29 |                       23.29 |
| 2016-11-30     | Bull Market     |               110.04 |            104.59 | AMD,NVDA,STX      | 2016-11-30      | 2016-12-31    |                      13.26 |                       39.64 |
| 2016-12-31     | Bull Market     |               111.28 |            106.2  | NVDA,AMD,LITE     | 2016-12-31      | 2017-01-31    |                      -2.69 |                       35.88 |
| 2017-01-31     | Bull Market     |               117.01 |            107.72 | NVDA,MU,WDC       | 2017-01-31      | 2017-02-28    |                      -4.43 |                       29.86 |
| 2017-02-28     | Bull Market     |               122.12 |            110.09 | AMD,CSX,WDC       | 2017-02-28      | 2017-03-31    |                       1.5  |                       31.81 |
| 2017-03-31     | Bull Market     |               124.6  |            112.27 | AMD,MU,NVDA       | 2017-03-31      | 2017-04-30    |                      -5.7  |                       24.3  |
| 2017-04-30     | Bull Market     |               128    |            115.02 | AMD,SHOP,CSX      | 2017-04-30      | 2017-05-31    |                       4.01 |                       29.29 |
| 2017-05-31     | Bull Market     |               132.99 |            117.56 | SHOP,TSLA,MELI    | 2017-05-31      | 2017-06-30    |                      -2.7  |                       25.79 |
| 2017-06-30     | Bull Market     |               129.9  |            119.67 | ALNY,SHOP,VRTX    | 2017-06-30      | 2017-07-31    |                       9.28 |                       37.46 |
| 2017-07-31     | Bull Market     |               135.18 |            122.07 | ALNY,SHOP,VRTX    | 2017-07-31      | 2017-08-31    |                       9.81 |                       50.95 |
| 2017-08-31     | Bull Market     |               137.98 |            124.91 | SHOP,VRTX,TTWO    | 2017-08-31      | 2017-09-30    |                       1.42 |                       53.1  |
| 2017-09-30     | Bull Market     |               137.57 |            127.66 | INSM,ALNY,TTWO    | 2017-09-30      | 2017-10-31    |                      -0.51 |                       52.32 |
| 2017-10-31     | Bull Market     |               143.91 |            130.93 | INSM,ALNY,NVDA    | 2017-10-31      | 2017-11-30    |                       7.67 |                       64.01 |
| 2017-11-30     | Bull Market     |               146.75 |            133.9  | INSM,ALNY,TTWO    | 2017-11-30      | 2017-12-31    |                      -2.4  |                       60.08 |
| 2017-12-31     | Bull Market     |               147.63 |            136.45 | INSM,ALNY,TTWO    | 2017-12-31      | 2018-01-31    |                      -0.24 |                       59.7  |
| 2018-01-31     | Bull Market     |               160.56 |            140.05 | INSM,STX,ALNY     | 2018-01-31      | 2018-02-28    |                      -5.22 |                       51.37 |
| 2018-02-28     | Bull Market     |               158.49 |            143.1  | INSM,STX,NFLX     | 2018-02-28      | 2018-03-31    |                       1.71 |                       53.95 |
| 2018-03-31     | Bull Market     |               152.02 |            145    | STX,AXON,NFLX     | 2018-03-31      | 2018-04-30    |                       3.84 |                       59.86 |
| 2018-04-30     | Bull Market     |               152.79 |            147.29 | AXON,DXCM,NFLX    | 2018-04-30      | 2018-05-31    |                      28.15 |                      104.86 |
| 2018-05-31     | Bull Market     |               161.46 |            149.92 | AXON,NFLX,DXCM    | 2018-05-31      | 2018-06-30    |                       6.16 |                      117.49 |
| 2018-06-30     | Bull Market     |               163.31 |            152.45 | AXON,NFLX,DXCM    | 2018-06-30      | 2018-07-31    |                      -2.04 |                      113.05 |
| 2018-07-31     | Bull Market     |               167.88 |            155.48 | AXON,DXCM,AMD     | 2018-07-31      | 2018-08-31    |                      29.86 |                      176.67 |
| 2018-08-31     | Bull Market     |               177.58 |            158.85 | DXCM,AMD,AXON     | 2018-08-31      | 2018-09-30    |                       7.35 |                      197    |
| 2018-09-30     | Bull Market     |               177.08 |            161.88 | AMD,DXCM,AXON     | 2018-09-30      | 2018-10-31    |                     -19.34 |                      139.55 |
| 2019-02-28     | Bull Market     |               165.54 |            164.43 | INSM,PDD,MELI     | 2019-02-28      | 2019-03-31    |                      -2.82 |                      132.79 |
| 2019-03-31     | Bull Market     |               172.04 |            165.49 | INSM,ZS,MELI      | 2019-03-31      | 2019-04-30    |                      -1.21 |                      129.98 |
| 2019-04-30     | Bull Market     |               181.5  |            167.31 | INSM,ZS,SHOP      | 2019-04-30      | 2019-05-31    |                      -2.37 |                      124.52 |
| 2019-06-30     | Bull Market     |               179.21 |            167.34 | INSM,SHOP,MELI    | 2019-06-30      | 2019-07-31    |                      -2.26 |                      119.45 |
| 2019-07-31     | Bull Market     |               183.4  |            167.97 | SHOP,ZS,MELI      | 2019-07-31      | 2019-08-31    |                      -0.5  |                      118.35 |
| 2019-08-31     | Bull Market     |               179.91 |            169.78 | SHOP,QCOM,TTWO    | 2019-08-31      | 2019-09-30    |                      -8.43 |                       99.94 |
| 2019-09-30     | Bull Market     |               181.57 |            171.79 | SHOP,QCOM,PDD     | 2019-09-30      | 2019-10-31    |                      10.98 |                      121.9  |
| 2019-10-31     | Bull Market     |               189.52 |            176    | PDD,TSLA,KLAC     | 2019-10-31      | 2019-11-30    |                      -3.3  |                      114.59 |
| 2019-11-30     | Bull Market     |               197.23 |            179.65 | DXCM,PDD,LITE     | 2019-11-30      | 2019-12-31    |                       3.03 |                      121.09 |
| 2019-12-31     | Bull Market     |               204.9  |            183.59 | PDD,TSLA,ALNY     | 2019-12-31      | 2020-01-31    |                      16.1  |                      156.69 |
| 2020-01-31     | Bull Market     |               211.12 |            187.49 | TSLA,PDD,DXCM     | 2020-01-31      | 2020-02-29    |                       6.3  |                      172.87 |
| 2020-02-29     | Bull Market     |               198.33 |            189.18 | TSLA,DXCM,NVDA    | 2020-02-29      | 2020-03-31    |                      -8.8  |                      148.87 |
| 2020-04-30     | Bull Market     |               211.42 |            194.13 | TSLA,DXCM,SHOP    | 2020-04-30      | 2020-05-31    |                      13.17 |                      181.64 |
| 2020-05-31     | Bull Market     |               225.37 |            198.33 | TSLA,SHOP,ZS      | 2020-05-31      | 2020-06-30    |                      22.07 |                      243.79 |
| 2020-06-30     | Bull Market     |               239.54 |            204.29 | TSLA,DDOG,SHOP    | 2020-06-30      | 2020-07-31    |                      16.11 |                      299.18 |
| 2020-07-31     | Bull Market     |               257.14 |            211.85 | PDD,TSLA,ZS       | 2020-07-31      | 2020-08-31    |                      27.14 |                      407.51 |
| 2020-08-31     | Bull Market     |               285.28 |            221.42 | TSLA,ZS,PDD       | 2020-08-31      | 2020-09-30    |                     -10.8  |                      352.72 |
| 2020-09-30     | Bull Market     |               268.8  |            228.58 | TSLA,DDOG,SHOP    | 2020-09-30      | 2020-10-31    |                     -10.08 |                      307.07 |
| 2020-10-31     | Bull Market     |               260.61 |            234.15 | TSLA,DDOG,MELI    | 2020-10-31      | 2020-11-30    |                      27.74 |                      419.99 |
| 2020-11-30     | Bull Market     |               289.87 |            242.02 | TSLA,MSTR,PDD     | 2020-11-30      | 2020-12-31    |                      21.89 |                      533.83 |
| 2020-12-31     | Bull Market     |               304.08 |            252.6  | MSTR,TSLA,PDD     | 2020-12-31      | 2021-01-31    |                      21.53 |                      670.3  |
| 2021-01-31     | Bull Market     |               304.87 |            264.7  | MSTR,TSLA,WBD     | 2021-01-31      | 2021-02-28    |                      11.57 |                      759.45 |
| 2021-02-28     | Bull Market     |               304.47 |            274    | MSTR,WBD,PDD      | 2021-02-28      | 2021-03-31    |                     -16.46 |                      618.01 |
| 2021-03-31     | Bull Market     |               309.69 |            282.44 | MSTR,PLTR,FANG    | 2021-03-31      | 2021-04-30    |                       2.32 |                      634.65 |
| 2021-04-30     | Bull Market     |               328    |            291.28 | MSTR,PLTR,FANG    | 2021-04-30      | 2021-05-31    |                     -10.14 |                      560.18 |
| 2021-05-31     | Bull Market     |               324.06 |            297.97 | FANG,FTNT,WDC     | 2021-05-31      | 2021-06-30    |                       6.95 |                      606.08 |
| 2021-06-30     | Bull Market     |               344.35 |            303.88 | MSTR,FANG,AMAT    | 2021-06-30      | 2021-07-31    |                      -8.46 |                      546.35 |
| 2021-07-31     | Bull Market     |               354.2  |            312.42 | FTNT,NVDA,GOOG    | 2021-07-31      | 2021-08-31    |                      12.72 |                      628.55 |
| 2021-08-31     | Bull Market     |               369.14 |            323.27 | FTNT,NVDA,REGN    | 2021-08-31      | 2021-09-30    |                      -8.31 |                      568.04 |
| 2021-09-30     | Bull Market     |               348.16 |            329.1  | DDOG,FTNT,NVDA    | 2021-09-30      | 2021-10-31    |                      18.92 |                      694.45 |
| 2021-10-31     | Bull Market     |               375.54 |            336.25 | DDOG,APP,NVDA     | 2021-10-31      | 2021-11-30    |                       9.09 |                      766.65 |
| 2021-11-30     | Bull Market     |               383.04 |            344.07 | NVDA,AMD,DDOG     | 2021-11-30      | 2021-12-31    |                      -6.41 |                      711.13 |
| 2021-12-31     | Bull Market     |               387.46 |            352.36 | DDOG,TSLA,AMD     | 2021-12-31      | 2022-01-31    |                     -16.64 |                      576.13 |
| 2023-01-31     | Bull Market     |               289.04 |            285.14 | PDD,AXON,ALNY     | 2023-01-31      | 2023-02-28    |                      -7.8  |                      523.37 |
| 2023-02-28     | Bull Market     |               288    |            283.4  | AXON,NVDA,MSTR    | 2023-02-28      | 2023-03-31    |                      14.46 |                      613.5  |
| 2023-03-31     | Bull Market     |               315.34 |            284.87 | NVDA,AXON,SHOP    | 2023-03-31      | 2023-04-30    |                      -1.78 |                      600.84 |
| 2023-04-30     | Bull Market     |               316.94 |            289.18 | META,NVDA,MSTR    | 2023-04-30      | 2023-05-31    |                      12.78 |                      690.43 |
| 2023-05-31     | Bull Market     |               341.92 |            292.56 | PLTR,NVDA,META    | 2023-05-31      | 2023-06-30    |                       8.15 |                      754.84 |
| 2023-06-30     | Bull Market     |               363.48 |            299.67 | NVDA,PLTR,MSTR    | 2023-06-30      | 2023-07-31    |                      22.59 |                      947.92 |
| 2023-07-31     | Bull Market     |               377.51 |            311.26 | PLTR,APP,NVDA     | 2023-07-31      | 2023-08-31    |                       6.26 |                     1013.48 |
| 2023-08-31     | Bull Market     |               371.91 |            321.25 | APP,PLTR,NVDA     | 2023-08-31      | 2023-09-30    |                      -4.2  |                      966.74 |
| 2023-09-30     | Bull Market     |               353.02 |            327.84 | APP,PLTR,NVDA     | 2023-09-30      | 2023-10-31    |                      -7.52 |                      886.53 |
| 2023-10-31     | Bull Market     |               345.73 |            336.29 | PLTR,APP,ZS       | 2023-10-31      | 2023-11-30    |                      20.93 |                     1093.05 |
| 2023-11-30     | Bull Market     |               383.13 |            345.7  | PDD,MSTR,APP      | 2023-11-30      | 2023-12-31    |                      10.77 |                     1221.55 |
| 2023-12-31     | Bull Market     |               404.54 |            357.35 | PDD,MSTR,CRWD     | 2023-12-31      | 2024-01-31    |                      -6.46 |                     1136.21 |
| 2024-01-31     | Bull Market     |               411.9  |            367.01 | CRWD,PDD,AMD      | 2024-01-31      | 2024-02-29    |                       7.93 |                     1234.27 |
| 2024-02-29     | Bull Market     |               433.66 |            378.68 | MSTR,CRWD,PLTR    | 2024-02-29      | 2024-03-31    |                      19.1  |                     1489.11 |
| 2024-03-31     | Bull Market     |               439.19 |            388.41 | MSTR,ARM,NVDA     | 2024-03-31      | 2024-04-30    |                     -20.31 |                     1166.41 |
| 2024-04-30     | Bull Market     |               419.98 |            394.06 | MSTR,ARM,NVDA     | 2024-04-30      | 2024-05-31    |                      29.7  |                     1542.56 |
| 2024-05-31     | Bull Market     |               445.81 |            400.89 | MSTR,INSM,ARM     | 2024-05-31      | 2024-06-30    |                      15.94 |                     1804.42 |
| 2024-06-30     | Bull Market     |               474.66 |            411.16 | MSTR,INSM,ARM     | 2024-06-30      | 2024-07-31    |                       4.63 |                     1892.64 |
| 2024-07-31     | Bull Market     |               466.69 |            422.53 | MSTR,INSM,ARM     | 2024-07-31      | 2024-08-31    |                      -6.9  |                     1755.18 |
| 2024-08-31     | Bull Market     |               471.85 |            435.14 | INSM,ALNY,MSTR    | 2024-08-31      | 2024-09-30    |                       9.16 |                     1925.13 |
| 2024-09-30     | Bull Market     |               484.21 |            445.25 | INSM,ALNY,APP     | 2024-09-30      | 2024-10-31    |                       6.28 |                     2052.35 |
| 2024-10-31     | Bull Market     |               480.03 |            452.8  | INSM,MSTR,APP     | 2024-10-31      | 2024-11-30    |                      56.33 |                     3264.76 |
| 2024-11-30     | Bull Market     |               505.71 |            462.18 | APP,PLTR,MSTR     | 2024-11-30      | 2024-12-31    |                      -5.45 |                     3081.44 |
| 2024-12-31     | Bull Market     |               508.01 |            469.61 | APP,PLTR,MSTR     | 2024-12-31      | 2025-01-31    |                      12.93 |                     3492.88 |
| 2025-01-31     | Bull Market     |               519    |            477.6  | APP,PLTR,MSTR     | 2025-01-31      | 2025-02-28    |                     -10.87 |                     3102.18 |
| 2025-02-28     | Bull Market     |               504.97 |            486.09 | APP,PLTR,MSTR     | 2025-02-28      | 2025-03-31    |                      -2.14 |                     3033.74 |
| 2025-05-31     | Bull Market     |               516.61 |            493.02 | PLTR,AVGO,CRWD    | 2025-05-31      | 2025-06-30    |                       8.54 |                     3301.51 |
| 2025-06-30     | Bull Market     |               549.6  |            500.8  | PLTR,STX,ZS       | 2025-06-30      | 2025-07-31    |                       5.3  |                     3481.86 |
| 2025-07-31     | Bull Market     |               562.92 |            508.67 | PLTR,STX,WDC      | 2025-07-31      | 2025-08-31    |                       2.56 |                     3573.54 |
| 2025-08-31     | Bull Market     |               568.29 |            517.5  | LITE,PLTR,ALNY    | 2025-08-31      | 2025-09-30    |                      13.68 |                     4076.14 |
| 2025-09-30     | Bull Market     |               598.84 |            526.81 | SNDK,WDC,APP      | 2025-09-30      | 2025-10-31    |                      30.49 |                     5349.39 |
| 2025-10-31     | Bull Market     |               627.47 |            538.75 | SNDK,WDC,LITE     | 2025-10-31      | 2025-11-30    |                      27.36 |                     6840.19 |
| 2025-11-30     | Bull Market     |               617.67 |            548.62 | SNDK,LITE,WDC     | 2025-11-30      | 2025-12-31    |                       8.41 |                     7423.85 |
| 2025-12-31     | Bull Market     |               613.54 |            559.48 | SNDK,LITE,WDC     | 2025-12-31      | 2026-01-31    |                      64.77 |                    12297.2  |
| 2026-01-31     | Bull Market     |               621.09 |            574.92 | SNDK,MU,LITE      | 2026-01-31      | 2026-02-28    |                      29.51 |                    15955.6  |
| 2026-02-28     | Bull Market     |               606.53 |            588.26 | SNDK,LITE,WDC     | 2026-02-28      | 2026-03-31    |                      -1    |                    15795.8  |
| 2026-04-30     | Bull Market     |               667.74 |            606.13 | SNDK,LITE,WDC     | 2026-04-30      | 2026-05-31    |                      23.86 |                    19588.7  |

---

## Full Market Regime Backtest Returns

The following table shows the full monthly strategy return history with the market regime filter.

| ranking_date   | market_regime   | is_bull_market   |   market_index_price |   market_index_ma | selected_stocks   | holding_start   | holding_end   |   portfolio_return |   portfolio_return_percent |   cumulative_return |   cumulative_return_percent |
|:---------------|:----------------|:-----------------|---------------------:|------------------:|:------------------|:----------------|:--------------|-------------------:|---------------------------:|--------------------:|----------------------------:|
| 2016-10-31     | Bull Market     | True             |               109.56 |            103.26 | AMD,NVDA,STX      | 2016-10-31      | 2016-11-30    |             0.2329 |                      23.29 |              0.2329 |                       23.29 |
| 2016-11-30     | Bull Market     | True             |               110.04 |            104.59 | AMD,NVDA,STX      | 2016-11-30      | 2016-12-31    |             0.1326 |                      13.26 |              0.3964 |                       39.64 |
| 2016-12-31     | Bull Market     | True             |               111.28 |            106.2  | NVDA,AMD,LITE     | 2016-12-31      | 2017-01-31    |            -0.0269 |                      -2.69 |              0.3588 |                       35.88 |
| 2017-01-31     | Bull Market     | True             |               117.01 |            107.72 | NVDA,MU,WDC       | 2017-01-31      | 2017-02-28    |            -0.0443 |                      -4.43 |              0.2986 |                       29.86 |
| 2017-02-28     | Bull Market     | True             |               122.12 |            110.09 | AMD,CSX,WDC       | 2017-02-28      | 2017-03-31    |             0.015  |                       1.5  |              0.3181 |                       31.81 |
| 2017-03-31     | Bull Market     | True             |               124.6  |            112.27 | AMD,MU,NVDA       | 2017-03-31      | 2017-04-30    |            -0.057  |                      -5.7  |              0.243  |                       24.3  |
| 2017-04-30     | Bull Market     | True             |               128    |            115.02 | AMD,SHOP,CSX      | 2017-04-30      | 2017-05-31    |             0.0401 |                       4.01 |              0.2929 |                       29.29 |
| 2017-05-31     | Bull Market     | True             |               132.99 |            117.56 | SHOP,TSLA,MELI    | 2017-05-31      | 2017-06-30    |            -0.027  |                      -2.7  |              0.2579 |                       25.79 |
| 2017-06-30     | Bull Market     | True             |               129.9  |            119.67 | ALNY,SHOP,VRTX    | 2017-06-30      | 2017-07-31    |             0.0928 |                       9.28 |              0.3746 |                       37.46 |
| 2017-07-31     | Bull Market     | True             |               135.18 |            122.07 | ALNY,SHOP,VRTX    | 2017-07-31      | 2017-08-31    |             0.0981 |                       9.81 |              0.5095 |                       50.95 |
| 2017-08-31     | Bull Market     | True             |               137.98 |            124.91 | SHOP,VRTX,TTWO    | 2017-08-31      | 2017-09-30    |             0.0142 |                       1.42 |              0.531  |                       53.1  |
| 2017-09-30     | Bull Market     | True             |               137.57 |            127.66 | INSM,ALNY,TTWO    | 2017-09-30      | 2017-10-31    |            -0.0051 |                      -0.51 |              0.5232 |                       52.32 |
| 2017-10-31     | Bull Market     | True             |               143.91 |            130.93 | INSM,ALNY,NVDA    | 2017-10-31      | 2017-11-30    |             0.0767 |                       7.67 |              0.6401 |                       64.01 |
| 2017-11-30     | Bull Market     | True             |               146.75 |            133.9  | INSM,ALNY,TTWO    | 2017-11-30      | 2017-12-31    |            -0.024  |                      -2.4  |              0.6008 |                       60.08 |
| 2017-12-31     | Bull Market     | True             |               147.63 |            136.45 | INSM,ALNY,TTWO    | 2017-12-31      | 2018-01-31    |            -0.0024 |                      -0.24 |              0.597  |                       59.7  |
| 2018-01-31     | Bull Market     | True             |               160.56 |            140.05 | INSM,STX,ALNY     | 2018-01-31      | 2018-02-28    |            -0.0522 |                      -5.22 |              0.5137 |                       51.37 |
| 2018-02-28     | Bull Market     | True             |               158.49 |            143.1  | INSM,STX,NFLX     | 2018-02-28      | 2018-03-31    |             0.0171 |                       1.71 |              0.5395 |                       53.95 |
| 2018-03-31     | Bull Market     | True             |               152.02 |            145    | STX,AXON,NFLX     | 2018-03-31      | 2018-04-30    |             0.0384 |                       3.84 |              0.5986 |                       59.86 |
| 2018-04-30     | Bull Market     | True             |               152.79 |            147.29 | AXON,DXCM,NFLX    | 2018-04-30      | 2018-05-31    |             0.2815 |                      28.15 |              1.0486 |                      104.86 |
| 2018-05-31     | Bull Market     | True             |               161.46 |            149.92 | AXON,NFLX,DXCM    | 2018-05-31      | 2018-06-30    |             0.0616 |                       6.16 |              1.1749 |                      117.49 |
| 2018-06-30     | Bull Market     | True             |               163.31 |            152.45 | AXON,NFLX,DXCM    | 2018-06-30      | 2018-07-31    |            -0.0204 |                      -2.04 |              1.1305 |                      113.05 |
| 2018-07-31     | Bull Market     | True             |               167.88 |            155.48 | AXON,DXCM,AMD     | 2018-07-31      | 2018-08-31    |             0.2986 |                      29.86 |              1.7667 |                      176.67 |
| 2018-08-31     | Bull Market     | True             |               177.58 |            158.85 | DXCM,AMD,AXON     | 2018-08-31      | 2018-09-30    |             0.0735 |                       7.35 |              1.97   |                      197    |
| 2018-09-30     | Bull Market     | True             |               177.08 |            161.88 | AMD,DXCM,AXON     | 2018-09-30      | 2018-10-31    |            -0.1934 |                     -19.34 |              1.3955 |                      139.55 |
| 2018-10-31     | Bear Market     | False            |               161.86 |            163.3  | CASH              | 2018-10-31      | 2018-11-30    |             0      |                       0    |              1.3955 |                      139.55 |
| 2018-11-30     | Bear Market     | False            |               161.43 |            163.39 | CASH              | 2018-11-30      | 2018-12-31    |             0      |                       0    |              1.3955 |                      139.55 |
| 2018-12-31     | Bear Market     | False            |               147.45 |            162.29 | CASH              | 2018-12-31      | 2019-01-31    |             0      |                       0    |              1.3955 |                      139.55 |
| 2019-01-31     | Bear Market     | False            |               160.73 |            163.16 | CASH              | 2019-01-31      | 2019-02-28    |             0      |                       0    |              1.3955 |                      139.55 |
| 2019-02-28     | Bull Market     | True             |               165.54 |            164.43 | INSM,PDD,MELI     | 2019-02-28      | 2019-03-31    |            -0.0282 |                      -2.82 |              1.3279 |                      132.79 |
| 2019-03-31     | Bull Market     | True             |               172.04 |            165.49 | INSM,ZS,MELI      | 2019-03-31      | 2019-04-30    |            -0.0121 |                      -1.21 |              1.2998 |                      129.98 |
| 2019-04-30     | Bull Market     | True             |               181.5  |            167.31 | INSM,ZS,SHOP      | 2019-04-30      | 2019-05-31    |            -0.0237 |                      -2.37 |              1.2452 |                      124.52 |
| 2019-05-31     | Bear Market     | False            |               166.57 |            167.18 | CASH              | 2019-05-31      | 2019-06-30    |             0      |                       0    |              1.2452 |                      124.52 |
| 2019-06-30     | Bull Market     | True             |               179.21 |            167.34 | INSM,SHOP,MELI    | 2019-06-30      | 2019-07-31    |            -0.0226 |                      -2.26 |              1.1945 |                      119.45 |
| 2019-07-31     | Bull Market     | True             |               183.4  |            167.97 | SHOP,ZS,MELI      | 2019-07-31      | 2019-08-31    |            -0.005  |                      -0.5  |              1.1835 |                      118.35 |
| 2019-08-31     | Bull Market     | True             |               179.91 |            169.78 | SHOP,QCOM,TTWO    | 2019-08-31      | 2019-09-30    |            -0.0843 |                      -8.43 |              0.9994 |                       99.94 |
| 2019-09-30     | Bull Market     | True             |               181.57 |            171.79 | SHOP,QCOM,PDD     | 2019-09-30      | 2019-10-31    |             0.1098 |                      10.98 |              1.219  |                      121.9  |
| 2019-10-31     | Bull Market     | True             |               189.52 |            176    | PDD,TSLA,KLAC     | 2019-10-31      | 2019-11-30    |            -0.033  |                      -3.3  |              1.1459 |                      114.59 |
| 2019-11-30     | Bull Market     | True             |               197.23 |            179.65 | DXCM,PDD,LITE     | 2019-11-30      | 2019-12-31    |             0.0303 |                       3.03 |              1.2109 |                      121.09 |
| 2019-12-31     | Bull Market     | True             |               204.9  |            183.59 | PDD,TSLA,ALNY     | 2019-12-31      | 2020-01-31    |             0.161  |                      16.1  |              1.5669 |                      156.69 |
| 2020-01-31     | Bull Market     | True             |               211.12 |            187.49 | TSLA,PDD,DXCM     | 2020-01-31      | 2020-02-29    |             0.063  |                       6.3  |              1.7287 |                      172.87 |
| 2020-02-29     | Bull Market     | True             |               198.33 |            189.18 | TSLA,DXCM,NVDA    | 2020-02-29      | 2020-03-31    |            -0.088  |                      -8.8  |              1.4887 |                      148.87 |
| 2020-03-31     | Bear Market     | False            |               183.88 |            190.91 | CASH              | 2020-03-31      | 2020-04-30    |             0      |                       0    |              1.4887 |                      148.87 |
| 2020-04-30     | Bull Market     | True             |               211.42 |            194.13 | TSLA,DXCM,SHOP    | 2020-04-30      | 2020-05-31    |             0.1317 |                      13.17 |              1.8164 |                      181.64 |
| 2020-05-31     | Bull Market     | True             |               225.37 |            198.33 | TSLA,SHOP,ZS      | 2020-05-31      | 2020-06-30    |             0.2207 |                      22.07 |              2.4379 |                      243.79 |
| 2020-06-30     | Bull Market     | True             |               239.54 |            204.29 | TSLA,DDOG,SHOP    | 2020-06-30      | 2020-07-31    |             0.1611 |                      16.11 |              2.9918 |                      299.18 |
| 2020-07-31     | Bull Market     | True             |               257.14 |            211.85 | PDD,TSLA,ZS       | 2020-07-31      | 2020-08-31    |             0.2714 |                      27.14 |              4.0751 |                      407.51 |
| 2020-08-31     | Bull Market     | True             |               285.28 |            221.42 | TSLA,ZS,PDD       | 2020-08-31      | 2020-09-30    |            -0.108  |                     -10.8  |              3.5272 |                      352.72 |
| 2020-09-30     | Bull Market     | True             |               268.8  |            228.58 | TSLA,DDOG,SHOP    | 2020-09-30      | 2020-10-31    |            -0.1008 |                     -10.08 |              3.0707 |                      307.07 |
| 2020-10-31     | Bull Market     | True             |               260.61 |            234.15 | TSLA,DDOG,MELI    | 2020-10-31      | 2020-11-30    |             0.2774 |                      27.74 |              4.1999 |                      419.99 |
| 2020-11-30     | Bull Market     | True             |               289.87 |            242.02 | TSLA,MSTR,PDD     | 2020-11-30      | 2020-12-31    |             0.2189 |                      21.89 |              5.3383 |                      533.83 |
| 2020-12-31     | Bull Market     | True             |               304.08 |            252.6  | MSTR,TSLA,PDD     | 2020-12-31      | 2021-01-31    |             0.2153 |                      21.53 |              6.703  |                      670.3  |
| 2021-01-31     | Bull Market     | True             |               304.87 |            264.7  | MSTR,TSLA,WBD     | 2021-01-31      | 2021-02-28    |             0.1157 |                      11.57 |              7.5945 |                      759.45 |
| 2021-02-28     | Bull Market     | True             |               304.47 |            274    | MSTR,WBD,PDD      | 2021-02-28      | 2021-03-31    |            -0.1646 |                     -16.46 |              6.1801 |                      618.01 |
| 2021-03-31     | Bull Market     | True             |               309.69 |            282.44 | MSTR,PLTR,FANG    | 2021-03-31      | 2021-04-30    |             0.0232 |                       2.32 |              6.3465 |                      634.65 |
| 2021-04-30     | Bull Market     | True             |               328    |            291.28 | MSTR,PLTR,FANG    | 2021-04-30      | 2021-05-31    |            -0.1014 |                     -10.14 |              5.6018 |                      560.18 |
| 2021-05-31     | Bull Market     | True             |               324.06 |            297.97 | FANG,FTNT,WDC     | 2021-05-31      | 2021-06-30    |             0.0695 |                       6.95 |              6.0608 |                      606.08 |
| 2021-06-30     | Bull Market     | True             |               344.35 |            303.88 | MSTR,FANG,AMAT    | 2021-06-30      | 2021-07-31    |            -0.0846 |                      -8.46 |              5.4635 |                      546.35 |
| 2021-07-31     | Bull Market     | True             |               354.2  |            312.42 | FTNT,NVDA,GOOG    | 2021-07-31      | 2021-08-31    |             0.1272 |                      12.72 |              6.2855 |                      628.55 |
| 2021-08-31     | Bull Market     | True             |               369.14 |            323.27 | FTNT,NVDA,REGN    | 2021-08-31      | 2021-09-30    |            -0.0831 |                      -8.31 |              5.6804 |                      568.04 |
| 2021-09-30     | Bull Market     | True             |               348.16 |            329.1  | DDOG,FTNT,NVDA    | 2021-09-30      | 2021-10-31    |             0.1892 |                      18.92 |              6.9445 |                      694.45 |
| 2021-10-31     | Bull Market     | True             |               375.54 |            336.25 | DDOG,APP,NVDA     | 2021-10-31      | 2021-11-30    |             0.0909 |                       9.09 |              7.6665 |                      766.65 |
| 2021-11-30     | Bull Market     | True             |               383.04 |            344.07 | NVDA,AMD,DDOG     | 2021-11-30      | 2021-12-31    |            -0.0641 |                      -6.41 |              7.1113 |                      711.13 |
| 2021-12-31     | Bull Market     | True             |               387.46 |            352.36 | DDOG,TSLA,AMD     | 2021-12-31      | 2022-01-31    |            -0.1664 |                     -16.64 |              5.7613 |                      576.13 |
| 2022-01-31     | Bear Market     | False            |               353.57 |            356.75 | CASH              | 2022-01-31      | 2022-02-28    |             0      |                       0    |              5.7613 |                      576.13 |
| 2022-02-28     | Bear Market     | False            |               337.74 |            357.73 | CASH              | 2022-02-28      | 2022-03-31    |             0      |                       0    |              5.7613 |                      576.13 |
| 2022-03-31     | Bear Market     | False            |               353.51 |            360.67 | CASH              | 2022-03-31      | 2022-04-30    |             0      |                       0    |              5.7613 |                      576.13 |
| 2022-04-30     | Bear Market     | False            |               305.44 |            356.78 | CASH              | 2022-04-30      | 2022-05-31    |             0      |                       0    |              5.7613 |                      576.13 |
| 2022-05-31     | Bear Market     | False            |               300.6  |            351.42 | CASH              | 2022-05-31      | 2022-06-30    |             0      |                       0    |              5.7613 |                      576.13 |
| 2022-06-30     | Bear Market     | False            |               273.82 |            341.89 | CASH              | 2022-06-30      | 2022-07-31    |             0      |                       0    |              5.7613 |                      576.13 |
| 2022-07-31     | Bear Market     | False            |               308.19 |            337.89 | CASH              | 2022-07-31      | 2022-08-31    |             0      |                       0    |              5.7613 |                      576.13 |
| 2022-08-31     | Bear Market     | False            |               292.37 |            329.57 | CASH              | 2022-08-31      | 2022-09-30    |             0      |                       0    |              5.7613 |                      576.13 |
| 2022-09-30     | Bear Market     | False            |               261.57 |            317.43 | CASH              | 2022-09-30      | 2022-10-31    |             0      |                       0    |              5.7613 |                      576.13 |
| 2022-10-31     | Bear Market     | False            |               272.03 |            305.88 | CASH              | 2022-10-31      | 2022-11-30    |             0      |                       0    |              5.7613 |                      576.13 |
| 2022-11-30     | Bear Market     | False            |               287.11 |            299.24 | CASH              | 2022-11-30      | 2022-12-31    |             0      |                       0    |              5.7613 |                      576.13 |
| 2022-12-31     | Bear Market     | False            |               261.23 |            291.59 | CASH              | 2022-12-31      | 2023-01-31    |             0      |                       0    |              5.7613 |                      576.13 |
| 2023-01-31     | Bull Market     | True             |               289.04 |            285.14 | PDD,AXON,ALNY     | 2023-01-31      | 2023-02-28    |            -0.078  |                      -7.8  |              5.2337 |                      523.37 |
| 2023-02-28     | Bull Market     | True             |               288    |            283.4  | AXON,NVDA,MSTR    | 2023-02-28      | 2023-03-31    |             0.1446 |                      14.46 |              6.135  |                      613.5  |
| 2023-03-31     | Bull Market     | True             |               315.34 |            284.87 | NVDA,AXON,SHOP    | 2023-03-31      | 2023-04-30    |            -0.0178 |                      -1.78 |              6.0084 |                      600.84 |
| 2023-04-30     | Bull Market     | True             |               316.94 |            289.18 | META,NVDA,MSTR    | 2023-04-30      | 2023-05-31    |             0.1278 |                      12.78 |              6.9043 |                      690.43 |
| 2023-05-31     | Bull Market     | True             |               341.92 |            292.56 | PLTR,NVDA,META    | 2023-05-31      | 2023-06-30    |             0.0815 |                       8.15 |              7.5484 |                      754.84 |
| 2023-06-30     | Bull Market     | True             |               363.48 |            299.67 | NVDA,PLTR,MSTR    | 2023-06-30      | 2023-07-31    |             0.2259 |                      22.59 |              9.4792 |                      947.92 |
| 2023-07-31     | Bull Market     | True             |               377.51 |            311.26 | PLTR,APP,NVDA     | 2023-07-31      | 2023-08-31    |             0.0626 |                       6.26 |             10.1348 |                     1013.48 |
| 2023-08-31     | Bull Market     | True             |               371.91 |            321.25 | APP,PLTR,NVDA     | 2023-08-31      | 2023-09-30    |            -0.042  |                      -4.2  |              9.6674 |                      966.74 |
| 2023-09-30     | Bull Market     | True             |               353.02 |            327.84 | APP,PLTR,NVDA     | 2023-09-30      | 2023-10-31    |            -0.0752 |                      -7.52 |              8.8653 |                      886.53 |
| 2023-10-31     | Bull Market     | True             |               345.73 |            336.29 | PLTR,APP,ZS       | 2023-10-31      | 2023-11-30    |             0.2093 |                      20.93 |             10.9305 |                     1093.05 |
| 2023-11-30     | Bull Market     | True             |               383.13 |            345.7  | PDD,MSTR,APP      | 2023-11-30      | 2023-12-31    |             0.1077 |                      10.77 |             12.2155 |                     1221.55 |
| 2023-12-31     | Bull Market     | True             |               404.54 |            357.35 | PDD,MSTR,CRWD     | 2023-12-31      | 2024-01-31    |            -0.0646 |                      -6.46 |             11.3621 |                     1136.21 |
| 2024-01-31     | Bull Market     | True             |               411.9  |            367.01 | CRWD,PDD,AMD      | 2024-01-31      | 2024-02-29    |             0.0793 |                       7.93 |             12.3427 |                     1234.27 |
| 2024-02-29     | Bull Market     | True             |               433.66 |            378.68 | MSTR,CRWD,PLTR    | 2024-02-29      | 2024-03-31    |             0.191  |                      19.1  |             14.8911 |                     1489.11 |
| 2024-03-31     | Bull Market     | True             |               439.19 |            388.41 | MSTR,ARM,NVDA     | 2024-03-31      | 2024-04-30    |            -0.2031 |                     -20.31 |             11.6641 |                     1166.41 |
| 2024-04-30     | Bull Market     | True             |               419.98 |            394.06 | MSTR,ARM,NVDA     | 2024-04-30      | 2024-05-31    |             0.297  |                      29.7  |             15.4256 |                     1542.56 |
| 2024-05-31     | Bull Market     | True             |               445.81 |            400.89 | MSTR,INSM,ARM     | 2024-05-31      | 2024-06-30    |             0.1594 |                      15.94 |             18.0442 |                     1804.42 |
| 2024-06-30     | Bull Market     | True             |               474.66 |            411.16 | MSTR,INSM,ARM     | 2024-06-30      | 2024-07-31    |             0.0463 |                       4.63 |             18.9264 |                     1892.64 |
| 2024-07-31     | Bull Market     | True             |               466.69 |            422.53 | MSTR,INSM,ARM     | 2024-07-31      | 2024-08-31    |            -0.069  |                      -6.9  |             17.5518 |                     1755.18 |
| 2024-08-31     | Bull Market     | True             |               471.85 |            435.14 | INSM,ALNY,MSTR    | 2024-08-31      | 2024-09-30    |             0.0916 |                       9.16 |             19.2513 |                     1925.13 |
| 2024-09-30     | Bull Market     | True             |               484.21 |            445.25 | INSM,ALNY,APP     | 2024-09-30      | 2024-10-31    |             0.0628 |                       6.28 |             20.5235 |                     2052.35 |
| 2024-10-31     | Bull Market     | True             |               480.03 |            452.8  | INSM,MSTR,APP     | 2024-10-31      | 2024-11-30    |             0.5633 |                      56.33 |             32.6476 |                     3264.76 |
| 2024-11-30     | Bull Market     | True             |               505.71 |            462.18 | APP,PLTR,MSTR     | 2024-11-30      | 2024-12-31    |            -0.0545 |                      -5.45 |             30.8144 |                     3081.44 |
| 2024-12-31     | Bull Market     | True             |               508.01 |            469.61 | APP,PLTR,MSTR     | 2024-12-31      | 2025-01-31    |             0.1293 |                      12.93 |             34.9288 |                     3492.88 |
| 2025-01-31     | Bull Market     | True             |               519    |            477.6  | APP,PLTR,MSTR     | 2025-01-31      | 2025-02-28    |            -0.1087 |                     -10.87 |             31.0218 |                     3102.18 |
| 2025-02-28     | Bull Market     | True             |               504.97 |            486.09 | APP,PLTR,MSTR     | 2025-02-28      | 2025-03-31    |            -0.0214 |                      -2.14 |             30.3374 |                     3033.74 |
| 2025-03-31     | Bear Market     | False            |               466.66 |            488.18 | CASH              | 2025-03-31      | 2025-04-30    |             0      |                       0    |             30.3374 |                     3033.74 |
| 2025-04-30     | Bear Market     | False            |               473.18 |            488.03 | CASH              | 2025-04-30      | 2025-05-31    |             0      |                       0    |             30.3374 |                     3033.74 |
| 2025-05-31     | Bull Market     | True             |               516.61 |            493.02 | PLTR,AVGO,CRWD    | 2025-05-31      | 2025-06-30    |             0.0854 |                       8.54 |             33.0151 |                     3301.51 |
| 2025-06-30     | Bull Market     | True             |               549.6  |            500.8  | PLTR,STX,ZS       | 2025-06-30      | 2025-07-31    |             0.053  |                       5.3  |             34.8186 |                     3481.86 |
| 2025-07-31     | Bull Market     | True             |               562.92 |            508.67 | PLTR,STX,WDC      | 2025-07-31      | 2025-08-31    |             0.0256 |                       2.56 |             35.7354 |                     3573.54 |
| 2025-08-31     | Bull Market     | True             |               568.29 |            517.5  | LITE,PLTR,ALNY    | 2025-08-31      | 2025-09-30    |             0.1368 |                      13.68 |             40.7614 |                     4076.14 |
| 2025-09-30     | Bull Market     | True             |               598.84 |            526.81 | SNDK,WDC,APP      | 2025-09-30      | 2025-10-31    |             0.3049 |                      30.49 |             53.4939 |                     5349.39 |
| 2025-10-31     | Bull Market     | True             |               627.47 |            538.75 | SNDK,WDC,LITE     | 2025-10-31      | 2025-11-30    |             0.2736 |                      27.36 |             68.4019 |                     6840.19 |
| 2025-11-30     | Bull Market     | True             |               617.67 |            548.62 | SNDK,LITE,WDC     | 2025-11-30      | 2025-12-31    |             0.0841 |                       8.41 |             74.2385 |                     7423.85 |
| 2025-12-31     | Bull Market     | True             |               613.54 |            559.48 | SNDK,LITE,WDC     | 2025-12-31      | 2026-01-31    |             0.6477 |                      64.77 |            122.972  |                    12297.2  |
| 2026-01-31     | Bull Market     | True             |               621.09 |            574.92 | SNDK,MU,LITE      | 2026-01-31      | 2026-02-28    |             0.2951 |                      29.51 |            159.556  |                    15955.6  |
| 2026-02-28     | Bull Market     | True             |               606.53 |            588.26 | SNDK,LITE,WDC     | 2026-02-28      | 2026-03-31    |            -0.01   |                      -1    |            157.958  |                    15795.8  |
| 2026-03-31     | Bear Market     | False            |               577.18 |            594.31 | CASH              | 2026-03-31      | 2026-04-30    |             0      |                       0    |            157.958  |                    15795.8  |
| 2026-04-30     | Bull Market     | True             |               667.74 |            606.13 | SNDK,LITE,WDC     | 2026-04-30      | 2026-05-31    |             0.2386 |                      23.86 |            195.887  |                    19588.7  |

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
