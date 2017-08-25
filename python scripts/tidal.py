#!/usr/bin/python
import numpy as np
import re
import sys

SPACES = re.compile('\s+')
data_by_country = {}
with open('C:\Users\Radu Roxana\Documents\tidal data\currents.txt') as f:
    # get and print header
    line = next(f)
    print  ("rgn_id_OHI"+'\t'+"currents")
    for line in f:
        data = SPACES.split(line.strip())
        data_by_country.setdefault((data[0]), []).append(data[3])

c=[]
avg=[]
for country, tid in data_by_country.items():
    s=0
    c.append(country)
    n=len(tid)
    for d in tid:
        if d!='0':
            s+=float(d)
        else:
            n=n-1
        avg.append(s/n)

for i in range (len(c)):
	print (c[i]+'\t'+str(avg[i]))
