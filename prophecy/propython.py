import csv, sqlite3

db = sqlite3.connect('roster.db')

cursor = db.cursor()
reader = csv.reader(open('students.csv', 'r'))
for row in reader:
    print(row)
