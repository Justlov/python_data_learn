# -*- coding: utf-8 -*-
#! /usr/bin/env/python3

import pandas as pd
import glob
import os
import sys

input_path = sys.argv[1]
output_path = sys.argv[2]
all_files = glob.glob(os.path.join(input_path,"亚洲国家*"))
all_data = []
for input_file in all_files:
    data_frame = pd.read_csv(input_file,index_col=None)

    total_sales = pd.DataFrame([float(str(value).strip("$").replace(",",'')) for value in data_frame.loc[:,"sale Amount"]]).sum()

    averagte_sales = pd.DataFrame([float(str(value).strip("$").replace(",",'')) for value in data_frame.loc[:,"sale Amount"]]).mean()

    data = {"file_name" : os.path.basename(input_file),
            'totale_sales': total_sales,
            'average_sales':averagte_sales}

    all_data.append(pd.DataFrame(data,columns=['filename',"total_sales","average_sale"]))
data_frame_concat = pd.concat(all_data,axis=0,ignore_index=True)
data_frame_concat.to_csv(output_path,index = False)