import sqlite3

def connect_db():
    return sqlite3.connect('travel_guide.db')

def create_tables():
    conn = connect_db()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS places (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE,
        state TEXT,
        famous_places TEXT,
        hotels TEXT,
        details TEXT,
        image_path TEXT
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS itineraries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        place_name TEXT,
        notes TEXT,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )''')
    conn.commit()
    conn.close()

def add_place(name, state, famous_places, hotels, details, image_path):
    conn = connect_db()
    c = conn.cursor()
    c.execute('INSERT OR IGNORE INTO places (name, state, famous_places, hotels, details, image_path) VALUES (?, ?, ?, ?, ?, ?)', 
              (name, state, famous_places, hotels, details, image_path))
    conn.commit()
    conn.close()

def fetch_place(name):
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM places WHERE name=?', (name.lower(),))
    row = c.fetchone()
    conn.close()
    return row

def add_user(username, pwd_hash):
    conn = connect_db()
    c = conn.cursor()
    c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, pwd_hash))
    conn.commit()
    conn.close()

def check_user(username, pwd_hash):
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username=? AND password=?', (username, pwd_hash))
    row = c.fetchone()
    conn.close()
    return row
