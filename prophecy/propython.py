import csv, sqlite3

db = sqlite3.connect('roster.db')
cursor = db.cursor()

reader = csv.reader(open('students.csv', 'r'))
for row in reader:
    to_db = [unicode(row[0], "utf8"), unicode(row[1], "utf8"), unicode(row[2], "utf8")]
    cursor.execute("INSERT INTO PCFC (type, term, definition) VALUES (?, ?, ?);", to_db)
db.commit()
