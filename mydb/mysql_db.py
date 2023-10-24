import pymysql
from config import mydb

con = pymysql.connect(**mydb)
cursor = con.cursor()

class con_mysql(object):
    def __init__(self,sql):
        self.sql = sql

    def select_sql(self):
        cursor.execute(self.sql)
        r = cursor.fetchall()
        print(r)
        cursor.close()

sql1 = 'select * from mytable;'
db1 = con_mysql(sql1)
db1.select_sql()







