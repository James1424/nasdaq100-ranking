# Nasdaq-100 Six-Month Momentum Ranking

This repository automatically calculates the six-month momentum ranking of Nasdaq-100 stocks.

The ranking is based on adjusted closing prices over the most recent six-month period.

## Latest Top 20 Ranking

Last updated: **2026-05-30 01:15:57 UTC**

|   rank | Ticker   | start_date   | end_date   |   start_price |   end_price |   six_month_momentum_percent |   trading_days |
|-------:|:---------|:-------------|:-----------|--------------:|------------:|-----------------------------:|---------------:|
|      1 | SNDK     | 2025-12-01   | 2026-05-29 |        210.17 |     1694.98 |                       706.48 |            124 |
|      2 | MU       | 2025-12-01   | 2026-05-29 |        240.26 |      971    |                       304.14 |            124 |
|      3 | STX      | 2025-12-01   | 2026-05-29 |        268.92 |      879.8  |                       227.16 |            124 |
|      4 | WDC      | 2025-12-01   | 2026-05-29 |        163.33 |      531.21 |                       225.24 |            124 |
|      5 | INTC     | 2025-12-01   | 2026-05-29 |         40.01 |      114.68 |                       186.63 |            124 |
|      6 | LITE     | 2025-12-01   | 2026-05-29 |        317.93 |      854.96 |                       168.91 |            124 |
|      7 | ARM      | 2025-12-01   | 2026-05-29 |        135.01 |      353.29 |                       161.68 |            124 |
|      8 | AMD      | 2025-12-01   | 2026-05-29 |        219.76 |      516.1  |                       134.85 |            124 |
|      9 | MRVL     | 2025-12-01   | 2026-05-29 |         90.99 |      205    |                       125.3  |            124 |
|     10 | LRCX     | 2025-12-01   | 2026-05-29 |        154.35 |      318.18 |                       106.14 |            124 |
|     11 | TXN      | 2025-12-01   | 2026-05-29 |        166.22 |      305.68 |                        83.9  |            124 |
|     12 | MCHP     | 2025-12-01   | 2026-05-29 |         52.85 |       94.65 |                        79.09 |            124 |
|     13 | AMAT     | 2025-12-01   | 2026-05-29 |        254.12 |      450.06 |                        77.11 |            124 |
|     14 | MPWR     | 2025-12-01   | 2026-05-29 |        924.93 |     1566.21 |                        69.33 |            124 |
|     15 | FTNT     | 2025-12-01   | 2026-05-29 |         81.82 |      137.97 |                        68.63 |            124 |
|     16 | KLAC     | 2025-12-01   | 2026-05-29 |       1154.21 |     1921.71 |                        66.5  |            124 |
|     17 | NXPI     | 2025-12-01   | 2026-05-29 |        197.58 |      321.35 |                        62.64 |            124 |
|     18 | ODFL     | 2025-12-01   | 2026-05-29 |        139.2  |      225.15 |                        61.75 |            124 |
|     19 | CSCO     | 2025-12-01   | 2026-05-29 |         75.23 |      120.42 |                        60.07 |            124 |
|     20 | DDOG     | 2025-12-01   | 2026-05-29 |        157.9  |      247.35 |                        56.65 |            124 |

## Methodology

For each stock, six-month momentum is calculated as:

```text
six_month_momentum = last_adjusted_close / first_adjusted_close - 1
```

The stocks are then sorted from highest momentum to lowest momentum.

## Output File

The full ranking is saved in:

```text
nasdaq100_six_month_momentum_rank.csv
```

## Notes

- Price data is downloaded using `yfinance`.
- Momentum is calculated using adjusted close prices.
- The ranking is updated by GitHub Actions.
- This project is for research and educational purposes only.
- This project does not provide financial advice.
