# -*- coding: utf-8 -*-
import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
#cursor.execute('select * from user')
#print(cursor.fetchall())
cursor.close()
conn.commit()
conn.close()

def get_score_in(low, high):
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
#       cursor.execute('select * from user')
#       print(cursor.fetchall())
        cursor.execute(r"select name from user where score >= ? and score <= ? order by score", (low, high))
        datas = cursor.fetchall()
    finally:
        cursor.close()
        conn.close()
#   l = []
#   for x in datas:
#       l.append(x[0])
    l = [x[0] for x in datas]
    return l

print(get_score_in(80, 95))
print(get_score_in(60, 80))
print(get_score_in(60, 100))

assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print('Pass')
