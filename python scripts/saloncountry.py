#!/usr/bin/python
import numpy as np
import re
import sys

SPACES = re.compile('\s+')
coord=[]
with open("countries_coordinates.txt") as f:
    next(f) #skipping header
    for line in f:
        coord.append(SPACES.split(line.strip('\t')))
        
coordinates=zip(*coord)


#rgn_id_OHI -coord[0]	long_NW - coord[1]	lat_NW-coord[2]	long_SE-coord[3]	lat_SE-coord[4]

data=[]

with open("salinity.txt") as f:
    # get and print header
    line = next(f)
    print("rgn_id_OHI"+'\t'+line.strip())
    for line in f:
        data.append(SPACES.split(line.strip('\t')))


results = zip(*data)
for i in range(len(results[0])):
	for j in range(len(coordinates[0])):
    		if(results[1][i]>=coordinates[1][j] and results[1][i]<=coordinates[3][j] and results[0][i]<=coordinates[2][j] and results[0][i]>=coordinates[4][j]):
			print(coordinates[0][j]+'\t'+results[0][i]+'\t'+results[1][i]+'\t'+ results[2][i]) 
