# -*- coding: utf-8 -*-
#!/usf/bin/env python3

import pandas as pd

import sys

input_file = sys.argv[1]
output_file = sys.argv[2]
data_frame = pd.read_excel(input_file,'Sheet1',index_col=None)
data_frame_value_matches_pattern = data_frame[data_frame['Coustomer Name'].str.startwith('J')]
writer = pd.ExcelWriter(output_file)
data_frame_value_matches_pattern.to_excel(writer,sheet_name='aaa',index=False)
writer.save()
