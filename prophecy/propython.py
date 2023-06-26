import csv, sqlite3

db = sqlite3.connect('roster.db')

with open('students.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        to_db0 = row['id']
        to_db1 = row['student_name']
        to_db2 = row['house']
        to_db3 = row['head']
        db.execute('INSERT OR IGNORE INTO STUDENT(id, student_name) VALUES (?,?)', (to_db0, to_db1))
        db.execute('INSERT OR IGNORE INTO HOUSES(house, head) VALUES (?,?)', (to_db2, to_db3))
        db.execute('INSERT OR IGNORE INTO ASSIGNMENTS(id, house) VALUES (?,?)', (to_db0, to_db2))
    db.commit()
    db.execute('SELECT * FROM STUDENT')

