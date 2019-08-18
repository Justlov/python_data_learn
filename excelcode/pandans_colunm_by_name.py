# -*- coding: utf-8 -*-
#!/usf/bin/env python3

import pandas as pd

import sys

input_file = sys.argv[1]
output_file = sys.argv[2]
data_frame = pd.read_excel(input_file,'Sheet1',index_col=None)
data_frame_column_by_name = data_frame.loc[:,['aaa','bbb']]
writer = pd.ExcelWriter(output_file)
data_frame_column_by_name.to_excel(writer,sheet_name = 'Sheet1',index = False)
writer.save()
