import csv, sqlite3
from tabulate import tabulate

db = sqlite3.connect('roster.db')

with open('students.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        to_db0 = row['id']
        to_db1 = row['student_name']
        db.execute('INSERT OR IGNORE INTO STUDENT(id, student_name) VALUES (?,?)', (to_db0, to_db1))
        print(tabulate(row))
    db.commit()

