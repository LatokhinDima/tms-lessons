import sqlite3

with sqlite3.connect('phone_book.db') as connection:
    cur = connection.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS contacts(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR UNIQUE,
                    number VARCHAR
                    )''')
