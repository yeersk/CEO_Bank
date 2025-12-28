import sqlite3

db = sqlite3.connect('BANK.db')
cursor = db.cursor()

cursor.execute(
    '''
    CREATE TABLE account(
    id INTEGER NOT NULL PRIMARY KEY,
    user INTEGER,
    name VARCHAR,
    balance INTEGER
    );
    
    '''
)


db.commit()
db.close()