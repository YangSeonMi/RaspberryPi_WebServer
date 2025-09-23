import pymysql

conn = pymysql.connect(host='localhost', user='YangSeonMi', password='q1w2e3', db='study')
cur = conn.cursor()

def add_status(status):
    cur.execute("insert into record_led(status) values('{0}')".format(status))
    conn.commit()
