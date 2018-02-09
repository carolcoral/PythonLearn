'''
Created on 2018年2月9日

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

sql_insert = "select * from tb_student(id,name) values(10,'zhangfei')"
sql_update = "update tb_student set name = 'guanyu' where name='zhangfei'"
sql_delete = "delete from tb_student where name = 'guanyu' "  

#conn.autocommit()
try:
    cursor.execute(sql_insert)
    cursor.execute(sql_update)
    cursor.execute(sql_delete)
    # 提交
    conn.commit()
except Exception as e:
    print (e)
    conn.rollback()

cursor.close()
conn.close()

