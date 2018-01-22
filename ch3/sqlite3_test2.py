import sqlite3

filepath = 'test2.sqlite'
conn = sqlite3.connect(filepath)

cur = conn.cursor()
cur.execute('drop table if exists items')
cur.execute('''
create table items(
    item_id integer primary key,
    name text,
    price integer
);
''')

conn.commit()

cur = conn.cursor()
cur.execute(
    'insert into items (name, price) values(?,?)', ('Orange', 5200)
)
conn.commit()

cur = conn.cursor()
data = [('Mango', 7700), ('Kiwi', 4000), ('Grape', 8000),
    ('Peach', 9400), ('Persimmon', 7000), ('Banana', 4000)]
cur.executemany(
    'insert into items(name, price) values(?,?)', data
)
conn.commit()

cur = conn.cursor()
price_range = (4000, 7000)
cur.execute(
    'select * from items where price >=? AND price <=?', price_range
)
fr_list = cur.fetchall()
for fr in fr_list:
    print(fr)