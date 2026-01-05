# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd

df = pd.read_csv(
"http://www.thetransparencyproject.org/datasets/AnalyticDataset_Gray_LaPlante_PAB_2012.dat",
delimiter="\\t",
na_values=" "
)

print('Number of Observations:',len(df))