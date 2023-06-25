import sqlite3

db = sqlite3.connect('roster.db')

cursor = db.cursor()

cursor.execute()

for row in rows:
    print(row)