import sqlite3
import time
from pathlib import Path

import pandas as pd
import yfinance as yf


def get_nasdaq100_tickers():
    """
    从 Wikipedia 获取 Nasdaq-100 当前成分股 ticker。
    """
    import requests
    import pandas as pd
    from io import StringIO

    url = "https://en.wikipedia.org/wiki/Nasdaq-100"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers, timeout=20)
    response.raise_for_status()

    # 关键修改：用 StringIO 包一层
    tables = pd.read_html(StringIO(response.text))

    for table in tables:
        columns = [str(c).lower() for c in table.columns]

        if "ticker" in columns:
            ticker_col = table.columns[columns.index("ticker")]
            tickers = table[ticker_col].dropna().astype(str).tolist()
            return sorted(tickers)

        if "symbol" in columns:
            symbol_col = table.columns[columns.index("symbol")]
            tickers = table[symbol_col].dropna().astype(str).tolist()
            return sorted(tickers)

    raise ValueError("Could not find Nasdaq-100 ticker table.")


def download_one_stock(ticker, start_date, end_date):
    """
    下载单只股票的日线数据。
    返回标准格式 DataFrame。
    """
    print(f"Downloading {ticker}...")

    df = yf.download(
        ticker,
        start=start_date,
        end=end_date,
        interval="1d",
        auto_adjust=False,
        progress=False,
        threads=False,
    )

    if df.empty:
        print(f"No data for {ticker}")
        return None

    df = df.reset_index()

    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    df["Ticker"] = ticker

    df = df.rename(
        columns={
            "Date": "date",
            "Open": "open",
            "High": "high",
            "Low": "low",
            "Close": "close",
            "Adj Close": "adj_close",
            "Volume": "volume",
        }
    )

    required_columns = [
        "date",
        "Ticker",
        "open",
        "high",
        "low",
        "close",
        "adj_close",
        "volume",
    ]

    df = df[required_columns]

    df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")

    return df


def build_stock_database(tickers, start_date, end_date, db_path):
    """
    下载一组股票的历史价格，并保存到 SQLite 数据库。
    """
    db_path = Path(db_path)
    all_rows = []
    failed = []

    for ticker in tickers:
        try:
            df = download_one_stock(ticker, start_date, end_date)

            if df is None:
                failed.append(ticker)
                continue

            all_rows.append(df)

            time.sleep(0.5)

        except Exception as e:
            print(f"Failed to download {ticker}: {e}")
            failed.append(ticker)

    if not all_rows:
        raise ValueError("No stock data was downloaded.")

    database = pd.concat(all_rows, ignore_index=True)

    conn = sqlite3.connect(db_path)
    database.to_sql("daily_prices", conn, if_exists="replace", index=False)
    conn.close()

    print(f"\nDatabase saved to: {db_path}")
    print(f"Successful tickers: {database['Ticker'].nunique()}")
    print(f"Failed tickers: {failed}")

    return database, failed


def load_stock_database(db_path):
    """
    从 SQLite 数据库读取股票价格数据。
    """
    db_path = Path(db_path)

    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT * FROM daily_prices", conn)
    conn.close()

    df["date"] = pd.to_datetime(df["date"])

    return df