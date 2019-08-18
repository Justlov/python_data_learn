# -*- coding: utf-8 -*-
#!/usf/bin/env python3

import sys
from datetime import date
from  xlrd import open_workbook,xldate_as_tuple
from xlwt import Workbook
input_file = sys.argv[1]
output_file = sys.argv[2]
out_workbook = Workbook()
out_worksheet = out_workbook.add_sheet('aaa')
my_column = ["aaa","bbb"]
with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_index(1)
    data = [my_column]
    header_list = worksheet.row_values(0)
    header_index_list = []
    for header_index in range(len(header_list)):
        if header_list[header_index] in my_column:
            header_index_list.append(header_index)
    for  row_index in range(1,worksheet.nrows):
        row_list = []
        for column_index in header_index_list:
            cell_value = worksheet.cell_value(row_index,column_index)
            cell_type = worksheet.cell_type(row_index,column_index)
            if cell_type ==3:
                date_cell = xldate_as_tuple(cell_value,workbook.datemode)
                date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                row_list.append(date_cell)
            else:
                row_list.append(cell_value)
        data.append(row_list)

    for list_index,output_list in enumerate(data):
        for elment_index, elment in enumerate(output_list):
            out_worksheet.write(list_index,elment_index,elment)
out_workbook.save(output_file)