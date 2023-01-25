import sqlite3 as sq

companies = [
    ("IKEA", 32, 59200000000, 211000),
    ('Apple', 33, 366000000000, 164000),
    ("Газпром", 10, 10241000000000, 468000),
    ("Xiaomi", 4, 174915000000, 16683),
    ("Renault", 34, 46213000000, 156466),
    ("Mercedes-BENZ", 35, 93877000000, 152048),
    ("Роснефть", 1, 8760000000000, 315400),
    ("Volvo", 36, 372220000000, 95850),
    ("МТС", 1, 534000000000, 58415),
    ("Take-Two", 26, 3370000000, 6495),
    ("Domahin_company", 1, 10000000000, 500)
]

with sq.connect("data_base.db") as con:
    cur = con.cursor()

    cur.execute("""DROP TABLE IF EXISTS companies""")
    cur.execute("""CREATE TABLE IF NOT EXISTS companies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    city_id INTEGER,
    revenue INTEGER,
    labors INTEGER
    )""")

    cur.executemany("INSERT INTO companies (name,city_id,revenue,labors) VALUES(?,?,?,?)", companies)
