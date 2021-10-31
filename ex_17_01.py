import json
import sqlite3

con = sqlite3.connect('rosterdb.sqlite')
cur = con.cursor()

cur.executescript('''
    DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
);

''')

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data.json'

str_data = open(fname).read()
json_data = json.loads(str_data)

for entry in json_data:

    name = entry[0]
    title = entry[1]
    role = entry[2]

    #print((name,"|", title,"|", role,"|"))

    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', ( name, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ? )''',
        ( user_id, course_id, role ) )

    con.commit()


sqlstr1 = '''SELECT User.name,Course.title, Member.role FROM
    User JOIN Member JOIN Course
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2;'''

print(" ---- SQLSTR1 ----\n")
for row in cur.execute(sqlstr1):
    #print(row)
    #print(row[0],"|",row[1],"|",row[2])
    i = 0
    for data in row:
        print(row[i],end = "|")
        i = i + 1

    print("\n")

sqlstr2 = '''SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X FROM
    User JOIN Member JOIN Course
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X LIMIT 5; '''
# || means concatenation,we are using hex function in sqlstr1 so it shoes contents of column X that hex(...||...||....||...)
print(" ---- SQLSTR2 ----\n")
for row in cur.execute(sqlstr2):
    #print(row)
    #print(row[0],"|",row[1],"|",row[2])
    i = 0
    for data in row:
        print(row[i])
        i = i + 1

    print("\n")
