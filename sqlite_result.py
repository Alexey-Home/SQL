import sqlite3 as sq

with sq.connect("data_base.db") as con:
    cur = con.cursor()

    cur.execute("""DROP TABLE IF EXISTS result""")
    cur.execute("""CREATE TABLE IF NOT EXISTS result (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    count_company INTEGER
    )""")

    cur.execute("SELECT id, name FROM countries")
    countries = cur.fetchall()
    cur.executemany("INSERT INTO result (id, name) VALUES(?,?)", countries)
    for i in countries:
        cur.execute("""UPDATE result SET count_company = 
        (SELECT count(country_id) as country_id FROM(
        SELECT country_id FROM companies 
        JOIN cities ON cities.id = companies.city_id 
        WHERE companies.labors > 1000) 
        WHERE country_id = {0}) WHERE id == {0}""".format(i[0]))


