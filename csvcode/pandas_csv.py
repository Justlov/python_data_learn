# -*- coding: utf-8 -*-
#! /usr/bin/env/python3


import sys
import pandas as pd

input_file = sys.argv[1]
out_file = sys.argv[2]
# 默认使用C engine作为parser engine，而当文件名中含有中文的时候，用C engine在部分情况下就会出错。所以在调用read_csv()方法时指定engine为Python就可以
data_frame = pd.read_csv(input_file,engine='python')
# 或者直接用open打开
# data_frame = pd.read_csv(open(input_file))
print(data_frame)
# data_frame.to_csv(out_file,index=False)
# 不加index= False 则会添加一列默认索引
data_frame.to_csv(out_file)