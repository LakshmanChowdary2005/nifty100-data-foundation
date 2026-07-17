import sqlite3
import pandas as pd
from pathlib import Path

DB = "db/nifty100.db"

conn = sqlite3.connect(DB)

cursor = conn.cursor()

tables = [
    "companies",
    "profitandloss",
    "balancesheet",
    "cashflow",
    "analysis",
    "documents",
    "prosandcons",
    "sectors",
    "stock_prices",
    "financial_ratios",
    "peer_groups"
]

audit = []

for table in tables:

    cursor.execute(f"SELECT COUNT(*) FROM {table}")

    rows = cursor.fetchone()[0]

    audit.append([table, rows])

audit_df = pd.DataFrame(
    audit,
    columns=[
        "Table",
        "Rows"
    ]
)

Path("output").mkdir(exist_ok=True)

audit_df.to_csv(
    "output/load_audit.csv",
    index=False
)

print(audit_df)

conn.close()