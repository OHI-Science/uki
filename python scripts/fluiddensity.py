#!/usr/bin/python
import re
import sys

SPACES = re.compile('\s+')
data=[]
countries=[]
salinity=[]
data2=[]
with open("salinitydata.txt") as f:
    next(f)
    for line in f:
        countries.append(line.split()[0])
	salinity.append(line.split()[1])
	countries=[float(x) for x in countries]
	salinity=[float(x) for x in salinity]


with open("data.txt") as f2:
    next(f2)
    for line in f2:
        data2.append(SPACES.split(line.strip()))
results2=zip(*data2)
temperature=(float(x) for x in results2[2])
sea_water_density=[]
print salinity
print temperature

for i in salinity:
	for j in temperature:
		A = 8.24493e-1- 4.0899e-3*j+7.6438e-5*j**2-8.2467e-7*j**3+ 5.3875e-9*j**4
		B = -5.72466e-3 + 1.0227e-4*j- 1.6546e-6*j**2
		C = 4.8314e-4
	#Calculating the water density
		water_density = 999.842594+6.793952e-2*j-9.095290e-3*j**2+1.001685e-4*j**3-1.120083e-6*j**4+6.536336e-9*j**5
	#Calculating the sea water density
		sea_water_density.append(water_density + A*i + B*(i**1.5)+C*(i**2))

for i in range(len(countries)):
	print str(countries[i])+'\t'+str(sea_water_density[i])
