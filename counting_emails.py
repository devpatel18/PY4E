import sqlite3

con = sqlite3.connect('email1.sqlite')
cur = con.cursor()

cur.execute('''DROP TABLE IF EXISTS Counts''')

cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input("Enter file name:")

try:
    fhand = open(fname)
except:
    print("Error")

for line in fhand:
    if not line.startswith("From: "):
        continue
    line = line.strip()
    pieces = line.split()
    email = pieces[1]
    temp = email.split('@')
    host = temp[1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (host,))
    row = cur.fetchone()#grabbing the first one
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (host,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (host,))
    con.commit()

sqlstr = 'SELECT * FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
