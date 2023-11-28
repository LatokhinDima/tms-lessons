import sqlite3

with sqlite3.connect('bank.db') as connection:
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS bank_accounts (
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        card_holder VARCHAR,
                        money INTEGER,
                        card_number INTEGER,
                        account_number VARCHAR
                        )''')
