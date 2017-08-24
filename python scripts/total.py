#!/usr/bin/python
import re
import sys

SPACES = re.compile('\s+')
data_by_lat_long = {}
with open("total.txt") as f:
    # get and print header
    line = next(f)
    print(line.strip())

    for line in f:
        data = SPACES.split(line.strip())
        data_by_lat_long.setdefault((data[0], data[1]), []).append(data[2:])

for lat_long, data in data_by_lat_long.items():
    results = zip(*data)
    if '-9.99' in results[0]:
        results[0] = ('-9.99', )
    avg = tuple(str(sum(float(x) for x in d) / len(d)) for d in results)
    print('\t'.join(lat_long + avg))

