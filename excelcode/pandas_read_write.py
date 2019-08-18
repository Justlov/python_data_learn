# -*- coding: utf-8 -*-
#!/usf/bin/env python3

import pandas as pd
import sys
input_file = sys.argv[1]
out_file = sys.argv[2]
data_frame = pd.read_excel(input_file,sheetname='Sheet1')
writer = pd.ExcelWriter(out_file)
data_frame.to_excel(writer,sheet_name="aaa",index=False)
writer.save()