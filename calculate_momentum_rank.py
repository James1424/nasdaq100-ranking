import os
import pandas as pd

from stock_database import (
    get_nasdaq100_tickers,
    build_stock_database,
    load_stock_database,
)


pd.set_option("display.max_columns", None)
pd.set_option("display.width", 2000)


def calculate_six_month_momentum(price_data):
    results = []

    for ticker, df in price_data.groupby("Ticker"):
        df = df.sort_values("date")

        first_row = df.iloc[0]
        last_row = df.iloc[-1]

        first_price = first_row["adj_close"]
        last_price = last_row["adj_close"]

        if first_price == 0 or pd.isna(first_price) or pd.isna(last_price):
            continue

        momentum = last_price / first_price - 1

        results.append(
            {
                "Ticker": ticker,
                "start_date": first_row["date"].strftime("%Y-%m-%d"),
                "end_date": last_row["date"].strftime("%Y-%m-%d"),
                "start_price": first_price,
                "end_price": last_price,
                "six_month_momentum": momentum,
                "six_month_momentum_percent": momentum * 100,
                "trading_days": len(df),
            }
        )

    rank = pd.DataFrame(results)

    rank = rank.sort_values(
        by="six_month_momentum",
        ascending=False
    ).reset_index(drop=True)

    rank.insert(0, "rank", rank.index + 1)

    return rank


if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)

    end_date = pd.Timestamp.today().normalize()
    start_date = end_date - pd.DateOffset(months=6)

    start_date_str = start_date.strftime("%Y-%m-%d")
    end_date_str = end_date.strftime("%Y-%m-%d")

    db_path = "data/nasdaq100_last_6_months.sqlite"
    output_path = "data/nasdaq100_six_month_momentum_rank.csv"

    print("Getting Nasdaq-100 tickers...")
    tickers = get_nasdaq100_tickers()

    print(f"Number of tickers: {len(tickers)}")
    print(tickers)

    print("\nBuilding stock price database...")
    build_stock_database(
        tickers=tickers,
        start_date=start_date_str,
        end_date=end_date_str,
        db_path=db_path,
    )

    print("\nLoading database...")
    price_data = load_stock_database(db_path)

    print("\nCalculating six-month momentum rank...")
    rank = calculate_six_month_momentum(price_data)

    rank.to_csv(output_path, index=False)

    print("\nTop 20 Nasdaq-100 stocks by six-month momentum:")
    print(rank.head(20).to_string(index=False))

    print("\nMomentum rank saved to:")
    print(output_path)