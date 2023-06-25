from cs50 import SQL

db = SQL("sqlite:///roster.db")

cursor = db.cursor()
rows ="""CREATE TABLE STUDENT(id INTEGER, student_name VARCHAR(255));"""
cursor.execute(rows)



for row in rows:
    print(row)