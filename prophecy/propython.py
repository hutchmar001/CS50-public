import csv, sqlite3

db = sqlite3.connect('roster.db')

reader = csv.reader(open('students.csv', 'r'))
for row in reader:
    db.execute('INSERT INTO STUDENT VALUES (?)', row[0])
            ## ('insert into stocks values (?,?,?,?,?)', t)
db.commit()
