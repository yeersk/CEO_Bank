import sqlite3

db = sqlite3.connect('BANK.db')
cursor = db.cursor()

cursor.execute(
    '''
    CREATE TABLE users(
                user_id INTEGER NOT NULL PRIMARY KEY,
                name VARCHAR,
                surname VARCHAR,
                login VARCHAR,
                password VARCHAR
    );
    
    '''
)


db.commit()
db.close()