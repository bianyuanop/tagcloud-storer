import sqlite3

with open('./schema.sql', 'r') as f:
    scripts = f.read()

db = sqlite3.connect('./images.db')
db.executescript(scripts)
db.commit()

print('Database initialized')