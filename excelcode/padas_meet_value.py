# -*- coding: utf-8 -*-
#!/usf/bin/env python3
import sys
import pandas as pd

input_file = sys.argv[1]
out_file = sys.argv[2]
data_frame = pd.read_excel(input_file,'Sheet',index_col=None)
data_frame_value_meets