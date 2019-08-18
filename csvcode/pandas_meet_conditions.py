# -*- coding: utf-8 -*-

import csv
import sys
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file,engine='python')
# print(data_frame["巴林"])
# print(data_frame['时间']> 2011)
data_meet_condition = data_frame.loc[data_frame['时间']== 2015]
data_meet_condition.to_csv(output_file,index="False")
