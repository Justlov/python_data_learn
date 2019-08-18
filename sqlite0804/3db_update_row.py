#!/usr/bin/env python3
import csv
import sys
import sqlite3
input_file = sys.argv[1]
# 创建Sqlite3 内存数据库
# 创建带有四个属性的sales 表
con =  sqlite3.connect(r'C:\Users\huangqi\Desktop\0530\my_sqlite3.db')
query = """     CREATE TABLE IF NOT EXIST sales
                (coustomer VARCHAR(20),
                product VARCHAR (40),
                amount float ,
                date DATE);
            """

con.execute(query)
con.commit()

# 向表中插入数据
data = [('xiaohuang','Notepad',2.5,'2018-01-02'),
        ('xiaohong','apple',4.15,'2019-02-03'),
        ('xiaozhang','watch', 5.15, '2019-03-03'),
         ('xiaoming', 'pen', 6.15, '2019-04-03')]

for tuple in data:
    print(tuple)

statement = "INSERT INTO sales VALUES (?,?,?,?)"
con.executemany(statement,data)
con.commit()

# 读取csv 文件并更新特定的行
fileder  =  csv.reader(open(input_file,'r',encoding='utf-8'),delimiter = ',')
header = next(fileder,None)
for row in fileder:
    data =[]
    for colum_index in range(len(header)):
        data.append(row[colum_index])

    print(data)
    con.execute("UPDATE sales SET amount = ?,data = ? where  coustomer = ?;",data)
con.commit()

# 查询sales 表

cursor = con.execute("SELECT * FROM sales")
rows = cursor.fetchall()
for row in rows:
    output = []
    for colum_index in len(row):
        output.append(str(row[colum_index]))

    print(output)

