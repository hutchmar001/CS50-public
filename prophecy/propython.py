from cs50 import SQL

db = SQL("sqlite:///roster.db")

cursor = db.cursor()
rows ="""CREATE TABLE student(NAME )
cursor.execute(rows)

="""CREATE TABLE STUDENT(NAME VARCHAR(255), CLASS VARCHAR(255),
SECTION VARCHAR(255));"""

for row in rows:
    print(row)