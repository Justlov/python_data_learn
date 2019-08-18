# -*- coding: utf-8 -*-
#!/usf/bin/env python3

import glob
import os
import sys
from  datetime import date
from xlwt import Workbook
from xlrd import  open_workbook,xldate_as_tuple
input_folder = sys.argv[1]
output_file = sys.argv[2]
output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('aaa')
data = []
first_worksheet = True
for input_file in glob.glob(os.path.join(input_folder,"*.xls")):
    print(os.path.basename(input_file))
    with open_workbook(input_file) as workbook:
        for worksheet in workbook.sheets():
            if first_worksheet:
                header_row = worksheet.row_values(0)
                data.append(header_row)
                first_worksheet = False
            for row_index in range(1,worksheet.nrows):
                row_list = []
                for colum_index in range(worksheet.ncols):
                    cell_value = worksheet.cell_value(row_index,colum_index)
                    cell_type = worksheet.cell_type(row_index,colum_index)
                    if cell_type ==3:



