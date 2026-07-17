import sqlite3

conn=sqlite3.connect("db/nifty100.db")

cursor=conn.cursor()

tables=[
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

print("="*50)

for t in tables:

    cursor.execute(f"SELECT COUNT(*) FROM {t}")

    c=cursor.fetchone()[0]

    print(f"{t:<25}{c}")

print("="*50)

conn.close()