import sqlite3 as sq


countries = [
    ("Россия", 146980061, 1820000000000),
    ("Франция", 68084217, 2954000000000),
    ("Германия", 83019200, 4672000000000),
    ("Китай", 1411778724, 18100000000000),
    ("Индия", 1400000000, 11750000000000),
    ("США", 333449281, 21433000000000),
    ("Италия", 58983122, 1848000000000),
    ("Испания", 47163418, 1394000000000),
    ("Бразилия", 207353391, 1839000000000),
    ("Хорватия", 4188853, 161246000000),
    ("Нидерланды", 17715700, 1029000000000),
]

with sq.connect("data_base.db") as con:
    cur = con.cursor()

    cur.execute("""DROP TABLE IF EXISTS countries""")
    cur.execute("""CREATE TABLE IF NOT EXISTS countries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    population INTEGER,
    gdp INTEGER
    )""")

    cur.executemany("INSERT INTO countries (name,population,gdp) VALUES(?,?,?)", countries)

