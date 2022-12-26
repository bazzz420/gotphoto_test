import pymysql
import json
import os

conn = pymysql.Connect(host='database',user='codetest',password='swordfish')

cur = conn.cursor()
cur.execute('use codetest;')
sql = 'select country,count(first_name) from people_stg p join places_stg pp on p.place_of_birth = pp.city group by 1 ;'
cur.execute(sql)
d = dict((x, y) for x, y in cur.fetchall())
j = json.dumps(d)
with open('/data/output.json' , 'w' , encoding="utf8") as f :
    f.write(j)