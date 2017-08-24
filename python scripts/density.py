import numpy as np
import math

def pow_with_nan(x, y):
    try:
        return math.pow(x, y)
    except ValueError:
        return 0

file = 'airdata.txt'

country=[]
lat=[]
long=[]
elevation=[]
temperature=[]
pressure=[]
density=[]

with open(file, "r+") as f:
    for line in f:
        #country.append(line.split()[0])
        try:
            elevation.append(line.split()[3])
        except IndexError:
            elevation.append(0)
    elevation=[float(x) for x in elevation]
    elevation=[i*3.2808399 for i in elevation]
    temperature=[59-0.0035*i for i in elevation]
    pressure=[2116*(pow_with_nan(((i+459.7)/518.6),5.256)) for i in temperature]
    density=[i/(1718*(k+459.7)) for k,i in zip(temperature,pressure)]
    elevation=[i*0.3048 for i in elevation]
    temperature=[(i-32)*(5./9.) for i in temperature]
    pressure=[i*47.8824274 for i in pressure]
    density=[i*515.378818 for i in density]
    print(elevation)
    print (temperature)
    print(pressure)
    print (density)
    for i in pressure:
        f.write("%s\n" %i)
        #f.write(pressure)
    #f.write(density)

f.close()


