# -*- coding: utf-8 -*-
#!/usf/bin/env python3

import sys
from xlrd import open_workbook
input_file = sys.argv[1]
work_book = open_workbook(input_file)
print("Number of worksheets:",work_book.nsheets)
for sheet in work_book.sheets():
    print("sheetname:",sheet.name)
    print("mrows:",sheet.nrows)
    print("mcols:",sheet.ncols)