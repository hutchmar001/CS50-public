import csv, SQL

db = SQL("sqlite:///roster.db")

reader = csv.reader(open('students.csv', 'r'))
for row in reader:
    to_db = [(row[0], "utf8"), (row[1], "utf8")]
    db.execute("INSERT INTO STUDENT(id, student_name) VALUES (?, ?);", to_db)
db.commit()
