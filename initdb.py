import sqlite3


conn = sqlite3.connect("web.db")
cur = conn.cursor()
cur.execute("CREATE TABLE people (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, amount INTEGER)")
cur.execute("CREATE TABLE maxamount (amount INTEGER)")
cur.execute("INSERT INTO maxamount(amount) VALUES(?)", (200000,))
conn.commit()
conn.close()
