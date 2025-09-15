import pymysql

conn = pymysql.connect(host='localhost', user='YangSeonMi', password='q1w2e3', db='shopping_db')
cur = conn.cursor()
cur.execute("select * from customer")
rows = cur.fetchall()
print(rows)
conn.commit()
conn.close()

