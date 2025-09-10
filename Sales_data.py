import sqlite3

conn=sqlite3.connect('sales_data.db')
curser=conn.cursor()

curser.execute('''
               CREATE TABLE IF NOT EXISTS sales(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   product TEXT NOT NULL,
                   quantity INTEGER NOT NULL,
                   price REAL NOT NULL)''')

sales_data = [
    ('Laptop', 5, 1000.0),
    ('Mouse', 10, 25.0),
    ('Keyboard', 7, 45.0),
    ('Monitor', 3, 150.0),
    ('Headphones', 8, 60.0)
]
curser.executemany('INSERT INTO sales(product,quantity,price) VALUES(?,?,?)',sales_data)

conn.commit()
conn.close()