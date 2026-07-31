import sqlite3
import pandas as pd

conn = sqlite3.connect("db/nifty100.db")

companies = pd.read_sql(
    "SELECT company_id, company_name FROM companies ORDER BY company_id",
    conn
)

print("=" * 50)
print("Total Companies in Database")
print("=" * 50)

print("Rows:", len(companies))
print(companies.head(10))

conn.close()