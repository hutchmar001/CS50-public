import csv, sqlite3

db = sqlite3.connect('roster.db')

reader = csv.reader(open('students.csv', 'r'))
for row in reader:
    to_db0 = row[0]
    to_db1 = row[1]
    db.execute('INSERT INTO STUDENT(id, student_name) VALUES (?,?)', to_db0, to_db1)
            ## ('insert into stocks values (?,?,?,?,?)', t)
db.commit()
