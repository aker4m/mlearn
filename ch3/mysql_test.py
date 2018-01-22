import MySQLdb

conn = MySQLdb.connect(
    user='root',
    passwd = 'test-password',
    host = 'localhost',
    db = 'test'
)

cur = conn.cursor()

cur.execute('drop table if exists items')
cur.execute('''
    create table items(
        item_id integer primary key auto_increment,
        name text,
        price integer
    )
''')

data = [('Banana', 300), ('Mango', 640), ('Kiwi', 280)]
for i in data:
    cur.execute('insert into items(name, price) values(%s,%s)', i)

cur.execute('select * from items')
for row in cur.fetchall():
    print(row)