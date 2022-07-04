import sqlite3

# Connecting to the database
conn = sqlite3.connect('database.db')
c = conn.cursor()

# Selecting all records from the database
for row in c.execute('SELECT * FROM codetable'):
	print(row)
	
conn.close()
