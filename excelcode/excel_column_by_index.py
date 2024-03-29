# -*- coding: utf-8 -*-
#!/usf/bin/env python3

import sys
from datetime import date
from xlrd import open_workbook,xldate_as_tuple
from xlwt import  Workbook
input_file = sys.argv[1]
output_file = sys.argv[2]
output_work = Workbook()
out_worksheet = output_work.add_sheet('aaa')
my_columns = [1,4]
with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_index(1)
    data = []
    for row_index in range(worksheet.nrows):
        row_list = []
        for colum_index in my_columns:
            cell_value = worksheet.cell_value(row_index,colum_index)
            cell_type = worksheet.cell_type(row_index,colum_index)
            if cell_type ==3:
                date_cell = xldate_as_tuple(cell_value,workbook.datemode)
                date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                row_list.append(date_cell)
            else:
                row_list.append(cell_value)
        data.append(row_list)

    for list_index, output_list in enumerate(data):
        for elment_indec ,elment in enumerate(output_list):
            out_worksheet.write(list_index,elment_indec,elment)
output_work.save(output_file)

