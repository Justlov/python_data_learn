# -*- coding: utf-8 -*-
#!/usf/bin/env python3

import sys
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]
data_frame = pd.read_excel(input_file,sheetname=None,index_col=None)
row_output = []
for worksheetname, data in data_frame.items():
    data['sale Amount' ] = data['sale Amount'].str.replace(r'\s','')
    data['sale Amount' ] = data['sale Amount'].str.replace(r',','')
    data['sale Amount' ] = data['sale Amount'].astype(float)
    row_output.append(data[data['sale Amount'].astype(float) > 2000])
filrered_rows = pd.concat(row_output,axis=0,ignore_index=True)
writer = pd.ExcelWriter(output_file)
filrered_rows.to_excel(writer,sheetname='Sheet',index = False)
writer.save()
