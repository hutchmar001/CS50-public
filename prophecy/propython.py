import csv, sqlite3

db = sqlite3.connect('roster.db')
cursor = db.cursor()

reader = csv.reader(open('students.csv', 'r'))
for row in reader:
    to_db = [row[0], row[1]]
    cursor.execute("INSERT INTO STUDENT(id, student_name) VALUES (?, ?);", to_db)
db.commit()
