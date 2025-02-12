import sqlite3

def init_db():
    conn = sqlite3.connect('new_data.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT NOT NULL, age INTEGER, email TEXT UNIQUE)')
    conn.commit()
    conn.close()

def create_records(name, age, email):
    conn = sqlite3.connect('new_data.db')
    c = conn.cursor()
    c.execute('INSERT INTO users(name, age, email) VALUES (?, ?, ?)', (name, age, email))
    conn.commit()
    conn.close()

def display_records():
    conn = sqlite3.connect('new_data.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users')
    rows = c.fetchall()
    print(rows)
    conn.close()

def update_records():
    conn = sqlite3.connect('new_data.db')
    c = conn.cursor()
    c.execute("UPDATE users SET age = 31 WHERE name = 'Kshitish'")
    conn.commit()
    conn.close()

def delete_records():
    conn = sqlite3.connect('new_data.db')
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE id = ?", (userid,))
    conn.commit()
    conn.close()