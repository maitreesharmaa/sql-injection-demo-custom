import sqlite3

with open("data.sql", "r") as f:
    data = f.read()

conn = sqlite3.connect("database.db")
cursor = conn.cursor()
cursor.executescript(data)
conn.commit()
conn.close()

print("Database created.")