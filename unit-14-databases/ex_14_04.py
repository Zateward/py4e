import sqlite3
import urllib.error, urllib.parse, urllib.request
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

connection = sqlite3.connect('database_04.sqlite')
cursor = connection.cursor()

url = input('Enter URL: ')
html = urllib.request.urlopen(url)
count = 0
dictionary = {}

cursor.execute('DROP TABLE IF EXISTS Counts')
cursor.execute('CREATE TABLE Counts (Org TEXT,  Count INTEGER)')

for data in html:
    data = data.decode().strip()
    if not data.startswith('From: '): continue
    data = data.split('@')
    org = data[1]
    #print(org)

    cursor.execute('SELECT Org FROM Counts WHERE Org = ?',(org,))
    row = cursor.fetchone()

    if row is None:
        cursor.execute('INSERT INTO Counts (Org, Count) VALUES (?,1)',(org,))
    else:
        cursor.execute('UPDATE Counts SET Count = Count + 1 WHERE Org = ?',(org,))

    connection.commit()

sqlstr = ('SELECT * FROM Counts ORDER BY Count DESC LIMIT 15')
for row in cursor.execute(sqlstr):
    print(str(row[0]), str(row[1]))

cursor.close()
