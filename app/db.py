from collections import OrderedDict
import sqlite3

class Db:
    def __init__(self):
        self.db_file = "web.db"


    @property
    def entries(self):
        with sqlite3.connect(self.db_file) as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM people")
            return cur.fetchall()
    
    def add(self, name, amount):
        with sqlite3.connect(self.db_file) as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO people(name,amount) VALUES(?,?)", (name, amount))
            conn.commit()

    def remove(self, id):
        with sqlite3.connect(self.db_file) as conn:
            cur = conn.cursor()
            cur.execute("DELETE FROM people WHERE id=?", (id,))
            conn.commit()

    def edit(self, id, name, amount):
        with sqlite3.connect(self.db_file) as conn:
            cur = conn.cursor()
            cur.execute("UPDATE people SET name=?, amount=? WHERE id=?", (name, amount, id))
            conn.commit()

    def names(self):
        with sqlite3.connect(self.db_file) as conn:
            cur = conn.cursor()
            cur.execute("SELECT name FROM people ORDER BY id DESC")
            names = cur.fetchall()
            names = [name for (name,) in names if name]
            names = tuple(OrderedDict.fromkeys(names))
            cur.execute("SELECT sum(amount) FROM people")
            [(amount,)] = cur.fetchall()
            if not amount:
                amount = 0
            return names, amount


    @property
    def maxamount(self):
        with sqlite3.connect(self.db_file) as conn:
            cur = conn.cursor()
            cur.execute("SELECT amount FROM maxamount LIMIT 1")
            [(amount,)] =  cur.fetchall()
            return amount

    @maxamount.setter
    def maxamount(self, amount):
        with sqlite3.connect(self.db_file) as conn:
            cur = conn.cursor()
            cur.execute("UPDATE maxamount SET amount=?", (amount, ))
            conn.commit()
