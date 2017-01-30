#!/usr/bin/python

import csv
import sqlite3

conn = sqlite3.connect('AskBronco.db')
cur = conn.cursor()
cur.execute("""DROP TABLE IF EXISTS User""")
cur.execute("""CREATE TABLE User
            (username text, firstname text, lastname text, email text, password text)""")

#cur.execute("""INSERT INTO User VALUES ('abc','abc','abc','abc','abc')""")

with open('User.csv', 'r') as f:
    reader = csv.reader(f.readlines()[1:])  # exclude header line
    cur.executemany("""INSERT INTO User VALUES (?,?,?,?,?)""",
			 (row for row in reader))

conn.commit()
conn.close()
