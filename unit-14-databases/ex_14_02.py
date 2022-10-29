import sqlite3

connection = sqlite3.connect('database_02.db')
cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS Ages')
cursor.execute('CREATE TABLE Ages (Name VARCHAR(128), Age INTEGER)')

row = cursor.fetchall()

cursor.execute('DELETE FROM Ages')
cursor.execute('INSERT INTO Ages (name, age) VALUES (?, 34)',('Kasja',))
cursor.execute('INSERT INTO Ages (name, age) VALUES (?, 21)',('Sharleen',))
cursor.execute('INSERT INTO Ages (name, age) VALUES (?, 33)',('Daria',))
cursor.execute('INSERT INTO Ages (name, age) VALUES (?, 19)',('Ailee',))

#if row is None:
#    cursor.execute('INSERT INTO Ages (name, age) VALUES (?, 21)',('Sharleen',))
#    cursor.execute('INSERT INTO Ages (name, age) VALUES (?, 34)',('Kasja',))
#    cursor.execute('INSERT INTO Ages (name, age) VALUES (?, 33)',('Daria',))
#    cursor.execute('INSERT INTO Ages (name, age) VALUES (?, 19)',('Ailee',))

connection.commit()

sqlstr = 'SELECT hex(name || age) AS X FROM Ages ORDER BY X'

for row in cursor.execute(sqlstr):
    print(row[0])

cursor.close()
