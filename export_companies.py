import sqlite3
import pandas as pd

conn = sqlite3.connect("db/nifty100.db")

companies = pd.read_sql(
    """
    SELECT company_id,
           company_name
    FROM companies
    ORDER BY company_id
    """,
    conn,
)

companies["market_cap_crore"] = 100000  # Placeholder value

companies.to_excel(
    "data/market_cap.xlsx",
    index=False
)

conn.close()

print("market_cap.xlsx created successfully!")