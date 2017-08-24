#!/usr/bin/python
import numpy as np
import re
import sys

SPACES = re.compile('\s+')
data_by_country = {}
with open("file.txt") as f:
    line = next(f)
    print  ("rgn_id_OHI"+'\t'+"air_temp"+'\t'+"sst"+'\t'+"wind_speed"+'\t'+"wave_height"+'\t'+"wave_period")
    for line in f:
        data = SPACES.split(line.strip())
        data_by_country.setdefault((data[0]), []).append(data[3:])

c=[]
avg=[]
for country, data in data_by_country.items():
    results = zip(*data)
    c.append(country)
    if '-9.99' in results[0]:
        results[0] = ('-9.99', )
    avg.append(tuple(str(sum(float(x) for x in d) / len(d)) for d in results))


for i in range (len(c)):
	print (c[i]+'\t'+str(avg[i]))
