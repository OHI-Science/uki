#!/usr/bin/python
import numpy as np
import re
import sys

SPACES = re.compile('\s+')
data_by_country = {}
with open("air.txt") as f:
    # get and print header
    line = next(f)
    print  ("rgn_id_OHI"+'\t'+"elevation"+'\t'+"temperature"+'\t'+"pressure"+'\t'+"density")
    for line in f:
        data = SPACES.split(line.strip())
        data_by_country.setdefault((data[0]), []).append(data[3:])

c=[]
avg=[]
for country, data in data_by_country.items():
    results = zip(*data)
    c.append(country)
    avg.append(tuple(str(sum(float(x) for x in d) / len(d)) for d in results))


for i in range (len(c)):
	print (c[i]+'\t'+str(avg[i][0])+'\t'+str(avg[i][1])+'\t'+str(avg[i][2])+'\t'+str(avg[i][3]))
