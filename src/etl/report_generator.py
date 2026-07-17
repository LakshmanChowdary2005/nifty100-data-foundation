import sqlite3
import pandas as pd
from pathlib import Path

conn = sqlite3.connect("db/nifty100.db")

output = Path("output")
output.mkdir(exist_ok=True)
company_df = pd.read_sql_query("""
SELECT
company_id,
company_name,
ticker,
sector
FROM companies
ORDER BY company_name
""", conn)

company_df.to_csv(
    output/"company_report.csv",
    index=False
)

print("Company Report Generated")
sector_df = pd.read_sql_query("""
SELECT
sector,
COUNT(*) AS total_companies
FROM companies
GROUP BY sector
ORDER BY total_companies DESC
""", conn)

sector_df.to_csv(
    output/"sector_report.csv",
    index=False
)

print("Sector Report Generated")
financial_df = pd.read_sql_query("""
SELECT
AVG(net_profit) AS average_profit,
MAX(net_profit) AS highest_profit,
MIN(net_profit) AS lowest_profit
FROM profitandloss
""", conn)

financial_df.to_csv(
    output/"financial_summary.csv",
    index=False
)

print("Financial Summary Generated")
conn.close()

print("\nAll reports generated successfully!")