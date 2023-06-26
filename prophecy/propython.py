import csv, sqlite3

db = sqlite3.connect('roster.db')

with open('students.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        to_db0 = row['id']
        to_db1 = row['student_name']
        to_db2 = row['house']
        to_db3 = row['head']
        db.execute('INSERT OR IGNORE INTO student(id, student_name) VALUES (?,?)', (to_db0, to_db1))
        db.execute('INSERT OR IGNORE INTO houses(house, head) VALUES (?,?)', (to_db2, to_db3))
        db.execute('INSERT OR IGNORE INTO assignments(id, house) VALUES (?,?)', (to_db0, to_db2))
    db.commit()
    db.execute('SELECT * FROM student')

