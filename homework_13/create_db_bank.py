import sqlite3

with sqlite3.connect('bank.db') as connection:
    result = connection.execute("""
        CREATE TABLE IF NOT EXISTS bank_accounts (
            card_holder VARCHAR ,
            money REAL,
            card_number INTEGER  ,
            account_number VARCHAR(20) PRIMARY KEY
            );""")
