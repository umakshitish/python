#sql 
import sqlite3
conn = sqlite3.connect('database1.db')

cursor = conn.cursor()
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS users(
#         id INTEGER PRIMARY KEY,
#         username TEXT NOT NULL,
#         age INTEGER,
#         email TEXT UNIQUE
#     )
# ''')


# cursor.execute("INSERT INTO users (username, age, email) VALUES ('bedant', 9, 'bedant@example.com')")

# c = conn.execute()
# c.execute('INSERT INTO users (name, age, email) VALUES (?, ?, ?)', (name, age, email))

# cursor.executemany("INSERT INTO users (username, age, email) values(?, ?, ?)", users)



# cursor.execute('SELECT * FROM users')
# cursor.execute('SELECT email, username FROM users')
cursor.execute('SELECT * FROM users WHERE age>30')
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.commit()