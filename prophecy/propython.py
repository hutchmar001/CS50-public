import csv, sqlite3

db = sqlite3.connect('roster.db')

with open('students.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        to_db0 = row['id']
        to_db1 = row['student_name']
        db.execute('INSERT INTO STUDENT(id, student_name) VALUES (?,?)', (to_db0, to_db1))
    db.commit()

