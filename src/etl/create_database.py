import sqlite3
from pathlib import Path

db_folder = Path("db")
db_folder.mkdir(exist_ok=True)

connection = sqlite3.connect(db_folder / "nifty100.db")

cursor = connection.cursor()

with open("db/schema.sql", "r") as file:
    cursor.executescript(file.read())

connection.commit()

print("Database Created Successfully!")

connection.close()