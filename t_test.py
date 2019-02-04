#!/usr/bin/env python

import pandas as pd
import numpy as np
import sys
from scipy import stats

list = []
k = 0

df = pd.read_table(sys.argv[1], names=(
    'sequence', 'input', 'CON1', 'CON2', 'CON3', 'B1', 'B2', 'B3'
))

for row in df.iterrows():
    series1 = [df.iat[k, 2], df.iat[k, 3], df.iat[k, 4]]
    series2 = [df.iat[k, 5], df.iat[k, 6], df.iat[k, 7]]
    t, p = stats.ttest_rel(series1, series2)
    list.append(p)
    k += 1
    p = ''
    t = ''
arr_list = np.array(list)
df['p-value'] = arr_list

df.to_csv(sys.argv[2])

