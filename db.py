import sqlite3 as sq

con = sq.connect("login.db")
cur = con.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS register (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fullname VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL UNIQUE,
        password VARCHAR(100) NOT NULL
    )
""")
con.commit()
con.close()