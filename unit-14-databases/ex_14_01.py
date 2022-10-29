import sqlite3

connection = sqlite3.connect('database_01.db')
cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS Proyect_1')
cursor.execute('CREATE TABLE Proyect_1 (Email TEXT, Count INTEGER)')

data = input('Enter a file to open it: ')
if len(data) < 1: data = 'mbox-short.txt'
data = open(data)

for line in data:
    line = line.strip()
    if line.startswith('From: '):
        line = line.split()
        mails = line[1]
        #print(mails)

        cursor.execute('SELECT Email FROM Proyect_1 WHERE Email = ?', (mails,))
        row = cursor.fetchone()

        if row is None:
            cursor.execute('INSERT INTO Proyect_1 (Email, Count) VALUES (?,1)',(mails,))
        else:
            cursor.execute('UPDATE Proyect_1 SET Count = Count + 1 WHERE Email = ?',(mails,))

        connection.commit()

sqlstr = 'SELECT Email, Count FROM Proyect_1 ORDER BY Count DESC LIMIT 10'

for row in cursor.execute(sqlstr):
    print(str(row[0]), str(row[1]))

cursor.close()
