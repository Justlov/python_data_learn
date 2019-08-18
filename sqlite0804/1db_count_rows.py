#!/usr/bin/env python3
# encoding = 'utf-8'

import  sqlite3
con = sqlite3.connect(r'C:\Users\huangqi\Desktop\0530\my_sqlite3.db')
query = """CREATE TABLE sale
            (coustomer VARCHAR(20),
            product VARCHAR(40),
            amount  FLOAT,
            date DATE);"""

# 执行创建数据库语句 并提交
con.execute(query)
con.commit()

# 在表中插入数据

data = [('xiaohuang','Notepad',2.5,'2018-01-02'),
        ('xiaohong','apple',4.15,'2019-02-03'),
        ('xiaozhang','watch', 5.15, '2019-03-03'),
         ('xiaoming', 'pen', 6.15, '2019-04-03')]



statement = 'INSERT INTO sales VALUES (?,?,?,?)'
con.executemany(statement,data)
con.commit()


# 查询sales 表
cursor = con.execute("select * from sales")
rows = cursor.fetchall()

row_counter = 0
for row in rows:
    print(row)
    row_counter += 1
print('Number of rows: %d' %(row_counter))