import csv, sqlite3
from tabulate import tabulate


db = sqlite3.connect('roster.db')
tables = ["student", "houses", "assignments"]


def get_input():
    global ipt
    try:
        ipt = input("Please enter a valid table.\n")
    except ValueError:
        get_input()
    if ipt not in tables:
        get_input()
get_input()


with open('students.csv', "r") as file:
    reader = csv.DictReader(file, fieldnames=[id,student_name,house,head])
    for row in reader:
        to_db0 = row['id']
        to_db1 = row['student_name']
        to_db2 = row['house']
        to_db3 = row['head']
        db.execute('INSERT OR IGNORE INTO student(id, student_name) VALUES (?,?);', (to_db0, to_db1))
        db.execute('INSERT OR IGNORE INTO houses(house, head) VALUES (?,?);', (to_db2, to_db3))
        db.execute('INSERT OR IGNORE INTO assignments(id, house) VALUES (?,?);', (to_db0, to_db2))
    file.close()


if ipt == "houses":
    r = db.execute('SELECT * FROM houses;')
elif ipt == "student":
    r = db.execute('SELECT * FROM student;')
else:
    r = db.execute('SELECT * FROM assignments;')


results = r.fetchall()
print(tabulate(results, tablefmt='fancy_grid'))

