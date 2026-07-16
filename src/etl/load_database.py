import sqlite3
import pandas as pd
from pathlib import Path

DATA = Path("data/processed")

conn = sqlite3.connect("db/nifty100.db")

files = {
    "companies": "companies.xlsx",
    "profitandloss": "profitandloss.xlsx",
    "balancesheet": "balancesheet.xlsx",
    "cashflow": "cashflow.xlsx",
    "analysis": "analysis.xlsx",
    "documents": "documents.xlsx",
    "prosandcons": "prosandcons.xlsx",
    "sectors": "sectors.xlsx",
    "stock_prices": "stock_prices.xlsx",
    "financial_ratios": "financial_ratios.xlsx",
    "peer_groups": "peer_groups.xlsx"
}

for table, file in files.items():

    print(f"Loading {table}...")

    df = pd.read_excel(DATA / file)

    df.to_sql(table, conn, if_exists="append", index=False)

print("\nAll Tables Loaded Successfully!")

conn.close()