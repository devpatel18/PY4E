import sqlite3
import xml.etree.ElementTree as ET

con = sqlite3.connect("tracksdb.sqlite")
cur = con.cursor()#cursor is like handle for your database server for reading and writing

#creating tables
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')


fname = input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'Library.xml'

def lookup(d,key): #function for finding data in xml tags
    found = False
    for child in d:
        if found:
            return child.text #loop will first identify the right tag first,and then return the right data from the next tag
        if child.tag == "key" and child.text == key:
            found = True
    return None

tree = ET.parse(fname)#taking up the xml data and parsing it into tree
stuff = tree.findall('dict/dict/dict')#stuff is list of all dicts,refer library.xml
print("Dict Count:",len(stuff))

for entry in stuff:
    if ( lookup(entry, 'Track ID') is None ):
        continue
    #getting the right data from the xml tags using the lookup function
    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    genre = lookup(entry,'Genre')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')

    if name is None or artist is None or album is None or genre is None :
        continue

    print(name, artist, album, genre, count, rating, length)

#IGNORE IS THERE TO PREVENT THE PROGRAM FROM BLOWING UP ,
#ARTIST NAME IS UNIQUE SO IF A DUPLICATE ENTRY COMES UP THE PROGRAM WILL BLOW UP,SO TO AVOID THAT THERE IS IGNORE
    cur.execute('''INSERT OR IGNORE INTO Artist (name)
        VALUES ( ? )''', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Genre (name)
        VALUES ( ? )''', (genre,  ) )
    cur.execute('''SELECT Genre.id FROM Genre WHERE name = ? ''', (genre, ))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]


    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count)
        VALUES ( ?, ?, ?, ?, ? ,?)''',
        ( name, album_id, genre_id, length, rating, count ) )


    sqlstr = '''SELECT Track.title, Artist.name, Album.title, Genre.name
    FROM Track JOIN Genre JOIN Album JOIN Artist
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3 '''

    for row in cur.execute(sqlstr):
        print("|  ",row,"  |")

    con.commit()
