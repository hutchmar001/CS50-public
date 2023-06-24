from cs50 import SQL

db = SQL("sqlite:///roster.db")

rows = db.execute("SELECT * FROM student")

for row in rows:
    print(row)