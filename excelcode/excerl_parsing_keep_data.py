import sys
from datetime import  date
import xlwt
from xlrd import open_workbook, xldate_as_tuple

input_file = sys.argv[1]
work_book = open_workbook(input_file)
output_file = sys.argv[2]
output_workbook = xlwt.Workbook()
output_file_sheet = output_workbook.add_sheet("aaaa")
worksheet = work_book.sheet_by_index(0)

for row_index in range(worksheet.nrows):
    row_list_output = []
    for col_index in range(worksheet.ncols):
        if worksheet.cell_type(row_index,col_index) ==3:
            data_cell = xldate_as_tuple(worksheet.cell_value(row_index,col_index),work_book.datemode)
            data_cell = date(*data_cell[0:3].strftime('%m%d%Y'))
            row_list_output.append(data_cell)
            output_file_sheet.write(row_index,col_index,data_cell)
        else:
            nodate_cell = worksheet.cell_value(row_index,col_index)
            row_list_output.append(nodate_cell)
            output_file_sheet.write(row_index,col_index,nodate_cell)
output_workbook.save(output_file)
