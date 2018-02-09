'''
Created on 2018年2月7日

@author: Carol
'''
import pymysql

conn = pymysql.Connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="947752894",
    db="db_exam",
    charset="utf8"
    )

cursor = conn.cursor()
sql = "select* from tb_student"
cursor.execute(sql)

conn.autocommite = False



rs = cursor.fetchall()
for i in rs:
    print(i)

# print (cursor.rowcount)
# 
# rs = cursor.fetchone()
# print(rs)
# 
# rs = cursor.fetchmany(3)
# print(rs)
# 
# rs = cursor.fetchall()
# print(rs)

conn.close()
cursor.close()

