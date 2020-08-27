"""title: sqlite3 is python's built-in database
topics: 
    creating and connecting to a SQLite DB;
    Pandas; 
reference1: 
    "Do you know python has a built-in database?"
    Christopher Tao in: Towards Data Science (Medium.com archive)
reference2:
    www.sqlite.org
so what? 
    some scenarios that you could use SQLite include embedded devices and IoT, data analysis, stand-in for
    enterprise database during demos or testing;
    no need to install any server-side/client-side software - it is already a built-in python library that acts as
    a relational database management system;
    even though SQLite is lightweight, it is so widely used that most SQL clients software can connect with it;
    SQLite DB can seamlessly integrate with Pandas Data Frame; 
further reading/links: 
    ? Google Colab Notebook
    ? Pandas Data Frame 
github: 
    piettoon_koud > master 
dependencies:
    a built-in python library (thus no need to pip install, simply import)
"""

import sqlite3 as sl

con = sl.connect("C:\\Users\\Administrator\\my_test.db") #create an SQLite DB and have a connection object

with con:
    con.execute("""
        CREATE TABLE USER (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER
        );
    """)  #create a USER table and add three columns 

# now to insert multiple records in one go
sql = 'INSERT INTO USER (id, name, age) values(?, ?, ?)'
data = [
    (1, 'Alice', 21),
    (2, 'Bob', 22),
    (3, 'Chris', 23)
]
with con:
    con.executemany(sql, data)

# to query the table
with con:
    data = con.execute("SELECT * FROM USER WHERE age <= 22")
    for row in data:
        print(row)