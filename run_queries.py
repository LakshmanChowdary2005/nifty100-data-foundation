import sqlite3

conn = sqlite3.connect("db/nifty100.db")
cursor = conn.cursor()

queries = [
    ("Total Companies", "SELECT COUNT(*) FROM companies"),
    ("Average Net Profit", "SELECT AVG(net_profit) FROM profitandloss"),
    ("Average Assets", "SELECT AVG(assets) FROM balancesheet")
]

for title, query in queries:
    print(f"\n{title}")
    print("-" * len(title))
    cursor.execute(query)
    print(cursor.fetchone())

conn.close()