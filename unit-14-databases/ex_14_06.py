import json
import sqlite3

#Doing the connection with sqlite3
connection = sqlite3.connect('database_06.db')
cursor = connection.cursor()

# Coding the sqlite3 database to create the tables
cursor.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, Name TEXT UNIQUE);
CREATE TABLE Member (User_ID INTEGER, Course_ID INTEGER, Role INTEGER, PRIMARY KEY (User_ID, Course_ID));
CREATE TABLE Course (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, Title TEXT UNIQUE)
''')

# Opening the file that contains the .json data, use the "read()" method to be aviable to read it
data = input('Enter a JSON-File to open it: ')
if len(data) < 1: data = 'roster_data.json'
data = open(data).read()

# Parsing the json file
json_data = json.loads(data)

# Searching all the relevant data to later open it in a database
for entry in json_data:
    name = entry[0]
    title = entry[1]
    role = entry[2]

    cursor.execute('INSERT OR IGNORE INTO User (Name) VALUES (?)',(name,))
    cursor.execute('SELECT ID FROM User WHERE Name = ?',(name,))
    User_ID = cursor.fetchone()[0]

    cursor.execute('INSERT OR IGNORE INTO Course (Title) VALUES (?)',(title,))
    cursor.execute('SELECT ID FROM Course WHERE Title = ?',(title,))
    Course_ID = cursor.fetchone()[0]

    cursor.execute('INSERT OR IGNORE INTO Member (User_ID, Course_ID, Role) VALUES (?, ?, ?)',(User_ID, Course_ID, role))

    connection.commit()
