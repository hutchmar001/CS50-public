import csv, sqlite3

db = sqlite3.connect('roster.db')

reader = csv.reader(open('students.csv', 'r'))
for row in reader:
    db.execute(INSERT INTO STUDENT(id) row[0])
db.commit()
