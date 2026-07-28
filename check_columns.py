import sqlite3
import pandas as pd

conn = sqlite3.connect("db/nifty100.db")

tables = [
    "companies",
    "financial_ratios",
    "profitandloss",
    "balancesheet",
    "cashflow",
    "analysis",
    "sectors"
]

for table in tables:
    print(f"\n===== {table} =====")
    df = pd.read_sql(f"SELECT * FROM {table} LIMIT 5", conn)
    print(df.columns.tolist())

conn.close()