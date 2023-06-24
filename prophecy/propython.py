from cs50 import SQL

db = SQL("sqlite:///roster.db")

rows = db.execute("SELECT COUNT(*) AS n FROM houses")

for row in rows:
    print(row["n"])