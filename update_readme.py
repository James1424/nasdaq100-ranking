from datetime import datetime, timezone

import pandas as pd


CSV_PATH = "nasdaq100_six_month_momentum_rank.csv"
README_PATH = "README.md"


def generate_readme(top_n=20):
    rank = pd.read_csv(CSV_PATH)

    top_rank = rank.head(top_n).copy()

    top_rank["six_month_momentum_percent"] = top_rank[
        "six_month_momentum_percent"
    ].round(2)

    top_rank["start_price"] = top_rank["start_price"].round(2)
    top_rank["end_price"] = top_rank["end_price"].round(2)

    table = top_rank[
        [
            "rank",
            "Ticker",
            "start_date",
            "end_date",
            "start_price",
            "end_price",
            "six_month_momentum_percent",
            "trading_days",
        ]
    ].to_markdown(index=False)

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    readme_lines = [
        "# Nasdaq-100 Six-Month Momentum Ranking",
        "",
        "This repository automatically calculates the six-month momentum ranking of Nasdaq-100 stocks.",
        "",
        "The ranking is based on adjusted closing prices over the most recent six-month period.",
        "",
        f"## Latest Top {top_n} Ranking",
        "",
        f"Last updated: **{now}**",
        "",
        table,
        "",
        "## Methodology",
        "",
        "For each stock, six-month momentum is calculated as:",
        "",
        "```text",
        "six_month_momentum = last_adjusted_close / first_adjusted_close - 1",
        "```",
        "",
        "The stocks are then sorted from highest momentum to lowest momentum.",
        "",
        "## Output File",
        "",
        "The full ranking is saved in:",
        "",
        "```text",
        CSV_PATH,
        "```",
        "",
        "## Notes",
        "",
        "- Price data is downloaded using `yfinance`.",
        "- Momentum is calculated using adjusted close prices.",
        "- The ranking is updated by GitHub Actions.",
        "- This project is for research and educational purposes only.",
        "- This project does not provide financial advice.",
        "",
    ]

    readme = "\n".join(readme_lines)

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(readme)


if __name__ == "__main__":
    generate_readme(top_n=20)
