import xml.etree.ElementTree as ET
import sqlite3

connection = sqlite3.connect('database_05.sqlite')
cursor = connection.cursor()

cursor.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT UNIQUE);
CREATE TABLE Genre (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT UNIQUE);
CREATE TABLE Album (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, Artist_ID INTEGER, Title TEXT UNIQUE);
CREATE TABLE Track (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, Title TEXT UNIQUE, Album_ID INTEGER, Genre_ID INTEGER, Length INTEGER, Rating INTEGER, Count INTEGER);
''')

xml = input('Enter a XML-File to open it: ')
if len(xml) < 1: xml = 'Library.xml'

def lookup(d, key):
    found = False
    for child in d:
        if found: return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None

data = ET.parse(xml)
data = data.findall('dict/dict/dict')
print('Dict count:', len(data))

for entry in data:
    if lookup(entry,'Track ID') is None: continue

    name_of_track = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    genre = lookup(entry, 'Genre')
    album = lookup(entry, 'Album')
    length = lookup(entry, 'Total Time')
    rating = lookup(entry, 'Rating')
    count = lookup(entry, 'Play Count')

    if name_of_track is None or album is None or genre is None: continue

    print(name_of_track, artist, genre, album)

    cursor.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)',(artist,))
    cursor.execute('SELECT ID FROM Artist WHERE name = ?',(artist,))
    Artist_ID = cursor.fetchone()[0]

    cursor.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)',(genre,))
    cursor.execute('SELECT ID FROM Genre WHERE name = ?',(genre,))
    Genre_ID = cursor.fetchone()[0]

    cursor.execute('INSERT OR IGNORE INTO Album (Artist_ID, Title) VALUES (?, ?)',(Artist_ID, album))
    cursor.execute('SELECT ID FROM Album WHERE Title = ?', (album, ))
    Album_ID = cursor.fetchone()[0]

    cursor.execute('INSERT OR IGNORE INTO Track (Title, Album_ID, Genre_ID, Length, Rating, Count) VALUES (?, ?, ?, ?, ?, ?)',(name_of_track, Album_ID, Genre_ID, length, rating, count))

    connection.commit()
