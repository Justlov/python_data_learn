# -*- coding: utf-8 -*-
import csv
import glob
import os
import sys

input_path = sys.argv[1]
file_counter = 0
for input_file in glob.glob(os.path.join(input_path,"亚洲国家*")):
    row_counter = 1
    with open(input_file,'r',newline='' ,encoding='ISO-8859-1') as csv_in_file:
        filereader = csv.reader(csv_in_file)
        header = next(filereader,None)
        for row in filereader:
            row_counter +=1
        print("文件{}行数{}列数{}".format(os.path.basename(input_file),row_counter,len(header)))
    file_counter +=1
print("文件个数{}".format(file_counter))