#!/usr/bin/python
import numpy as np
import re
import sys

SPACES = re.compile('\s+')
data_by_country = {}
with open("salinitycountry.txt") as f:
    # get and print header
    line = next(f)
    print  ("rgn_id_OHI"+'\t'+"salinity")
    for line in f:
        data = SPACES.split(line.strip())
        data_by_country.setdefault((data[0]), []).append(data[3])

c=[]
avg=[]
for country, sal in data_by_country.items():
	s=0
	c.append(country)
	n=len(sal)
	for d in sal:
		if d!='0':
			s+=float(d)
		else:
			n=n-1
        avg.append(s/n)

for i in range (len(c)):
	print (c[i]+'\t'+str(avg[i]))
