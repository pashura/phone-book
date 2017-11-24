import sqlite3

db = sqlite3.connect('db.sqlite3')
cursor = db.cursor()
# cursor.execute("insert into students (name, subj, mark) values (?, ?, ?)", ('John', 'DB', 3.5))
# db.commit()


aaa = cursor.execute('''SELECT * FROM phone_book''')
print(aaa.fetchall())
# for a in aaa.fetchall():
#     print('Bob' in a)
# print([a[1] for a in aaa.fetchall()])
# print('Bob' in [a[1] for a in aaa.fetchall()])
db.commit()


bbb = cursor.execute("SELECT name FROM phone_book WHERE (name = ?)", ('Bob',))

# print(bbb.fetchall())
print('Bob' in [a[0] for a in bbb.fetchall()])