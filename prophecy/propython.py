import sqlite3

db = sqlite3.connect('roster.db')

cursor = db.cursor()
with open('students.csv', 'r') as file:
    
cursor.execute()

for row in rows:
    print(row)