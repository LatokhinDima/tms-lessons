import sqlite3

with sqlite3.connect('sqlite.db') as connection:
    result = connection.execute('SELECT * FROM user')
    for i in result.fetchall():
        print(i)


min_age = int(input('Введите минимальный возраст: '))
result = connection.execute('SELECT * FROM user WHERE age >= ?;', (min_age,))

for i in result.fetchall:
    print(i)


