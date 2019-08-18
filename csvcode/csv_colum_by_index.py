# -*- coding: utf-8 -*-
#! /usr/bin/env/python3

import csv
import sys

input_file = sys.argv[1]
output_file =sys.argv[2]
my_colum = [0,3]
with open(input_file,'r',newline='') as csv_in_file:
    with open(output_file,'w',newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        for row_list in filereader:
            row_list_out = []
            for index_valur in my_colum:
                row_list_out.append(row_list[index_valur])

            print(row_list_out)
            filewriter.writerow(row_list_out)
