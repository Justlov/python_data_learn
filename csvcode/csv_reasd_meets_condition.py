# -*- coding: utf-8 -*-

import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file,'r',newline='') as csv_in_file:
    with open(output_file,'w',newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file,delimiter=",")
        filewriter = csv.writer(csv_out_file,delimiter=",")
        for row in filereader:
            number1 = row[1].strip()
            number2 = row[2].strip()
            if number1 > number2:
                filewriter.writerow(row)

