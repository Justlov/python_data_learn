# -*- coding: utf-8 -*-
#!/usf/bin/env python3

import sys

import xlwt
from xlrd import open_workbook
input_file = sys.argv[1]
work_book = open_workbook(input_file)
output_file = sys.argv[2]
output_workbook = xlwt.Workbook()
output_file_sheet = output_workbook.add_sheet("aaaa")
worksheet = work_book.sheet_by_index(0)
for row_index in range(worksheet.nrows):
    for col_index in range(worksheet.ncols):
        output_file_sheet.write(row_index,col_index,worksheet.cell_value(row_index,col_index))
output_workbook.save(output_file)


