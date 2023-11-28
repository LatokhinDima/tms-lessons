import sqlite3

with sqlite3.connect('phone_book.db') as connection:
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS phone_book(
                    name VARCHAR UNIQUE,
                    number VARCHAR
                    )''')
