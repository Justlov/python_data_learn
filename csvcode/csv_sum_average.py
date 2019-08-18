# -*- coding: utf-8 -*-

import csv
import glob
import os
import sys


input_file = sys.argv[1]
output_file = sys.argv[2]
for file in glob.glob(os.path.join(input_file,"亚洲国家*")):
    with open(file,'r',newline='',encoding='ISO-8859-1') as csv_in_file:
        with open(output_file, 'a', newline='',encoding='ISO-8859-1') as csv_out_file:
            filereader = csv.reader(csv_in_file)
            filewriter = csv.writer(csv_out_file)
            rowslist = []
            print(filereader)
            for row_list in filereader:
                rowslist.append(row_list[0])
                rowslist.append(row_list[1])
            print(rowslist)



