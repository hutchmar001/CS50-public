from cs50 import SQL

db = SQL("sqlite:///roster.db")

db.execute("SELECT * FROM student")