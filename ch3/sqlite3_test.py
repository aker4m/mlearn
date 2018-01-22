import sqlite3

dbpath = 'test.sqlite'
conn = sqlite3.connect(dbpath)

cur = conn.cursor()
cur.executescript("""
drop table if exists items;

create table items(
    item_id integer primary key, 
    name text unique,
    price integer
);

insert into items(name, price) values('Apple', 800);
insert into items(name, price) values('Orange', 780);
insert into items(name, price) values('Banana', 430);

""")

conn.commit()

cur = conn.cursor()
cur.execute('select item_id, name, price from items')
item_list = cur.fetchall()

for it in item_list:
    print(it)
