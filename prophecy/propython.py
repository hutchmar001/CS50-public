import csv, sqlite3

db = sqlite3.connect('roster.db')

reader = csv.reader(open('students.csv', 'r'))
for row in reader:
    to_db = [row[0], row[1]]
    strg = string.Format('INSERT INTO STUDENT VALUES (?,?)', to_db)
    db.execute(strg)
db.commit()
