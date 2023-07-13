import sqlite3

def create_database():
    dbase.execute('''CREATE TABLE IF NOT EXISTS test_table(
        ID INT PRIMARY KEY NOT NULL,
        NAME TEXT NOT NULL,
        PASSWORD TEXT NOT NULL
    )''')
    # Apply changes
    dbase.commit()

def add_data(ID, NAME, PASSWORD):
    dbase.execute('''INSERT INTO test_table(ID, NAME, PASSWORD)
        VALUES(?, ?, ?)
    ''', (ID, NAME, PASSWORD))
    # Apply changes
    dbase.commit()


# main
if __name__ == '__main__':   
    # Open the data base    
    dbase = sqlite3.connect('test_db.db')               
    create_database()
    add_data(5, 'hi', 'pw')
    # Close the data base
    dbase.close