import csv, sqlite3

db = sqlite3.connect('roster.db')
cursor = db.cursor()

reader = csv.reader(open('students.csv', 'r'))
for row in reader:
    to_db = row[0]
    cursor.execute("INSERT INTO STUDENT(id) VALUES to_db;")
db.commit()
