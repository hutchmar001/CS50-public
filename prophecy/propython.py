import csv, sqlite3

db = sqlite3.connect('roster.db')

reader = csv.reader(open('students.csv', 'r'))
for row in reader:
    to_db = [row[0], row[1]]
    db.execute('INSERT INTO STUDENT VALUES (?,?)', to_db)
            ## ('insert into stocks values (?,?,?,?,?)', t)
db.commit()
