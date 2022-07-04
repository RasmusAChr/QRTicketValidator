import sqlite3

# Create database
conn = sqlite3.connect('database.db')
c = conn.cursor()
c.execute('''CREATE TABLE codetable(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, code TEXT)''')
conn.commit()
conn.close()
