#!/usr/bin/env python3
# encoding = 'utf-8'
import csv
import sqlite3
import sys

# csv输入文件名
input_file= r'D:\data0611\csv\国家各项税收.csv'

# 创建sqlite3 内存数据库
# 创建带有5个属性的supoliers表
con  = sqlite3.connect(r'C:\Users\huangqi\Desktop\0530\my_sqlite3.db')
c = con.cursor()
#
create_tabel = """CREATE TABLE IF NOT EXISTS Supp
                (Supplier_Name VACHAR(20),
                Invoice_Number VARCHAR(20),
                part_Number VARCHAR(20),
                Cost VARCHAR(20),
                Cos VARCHAR(20),
                Co VARCHAR(20),
                Ct VARCHAR(20),
                t VARCHAR(20),
                st VARCHAR(20),
                ost VARCHAR(20),
                Purchase_Date DATE);
"""
#

c.execute(create_tabel)
con.commit()
#
# 读取csv 文件
file_reader = csv.reader(open(input_file,'r',encoding='utf-8'),delimiter = ',')
header = next(file_reader,None)
for row in file_reader:
    data = []
    for colum_index in range(len(header)):
        data.append(row[colum_index] if row[colum_index] else None)
    # print(data)
    c.execute("insert  into Supp VALUES(?,?,?,?,?,?,?,?,?,?,?);",data)

con.commit()
#
# print('')

# 查询Suppliers表

output= c.execute("select  * from Supp")
rows = output.fetchall()
print(rows)
for row in rows:
    output = []
    for colum_index in range(len(row)):
        output.append(str(row[colum_index]))

    print(output)
