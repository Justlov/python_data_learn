# -*- coding: utf-8 -*-
#!/usf/bin/env python3

import pandas as pd
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
data_frame = pd.read_excel(input_file,'Sheet1',index_col=None)
important_date = ['2012','2013']
data_frame_value_in_set = data_frame['Puchadate'].isin(important_date)
writer  = pd.ExcelWriter(output_file)
data_frame_value_in_set.to_excel(writer,sheet_name='Sheet1',index=False)
writer.save()