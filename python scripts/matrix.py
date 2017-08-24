import numpy as np

file = 'countries_coordinates.txt'
outfile = open('matrix.txt', 'w')

p = []
k = []
m = []
l = []
n=[]
#b=[]
r=0
with open(file) as f:
    next(f)
    for line in f:
        p.append(line.split()[0])
        k.append(line.split()[1])
        l.append(line.split()[2])
        m.append(line.split()[3])
        n.append(line.split()[4])
        p=[int(x) for x in p]
        k = [float(x) for x in k]
        l = [float(x) for x in l]
        m = [float(x) for x in m]
        n=[float(x) for x in n]
    for o in range(len(p)):
        a=[]
        if k[o]>m[o]: #when countries_coordinates has been made, small islands had
            c=k[o]    #their coordinates taken wrongly
            k[o]=m[o]
            m[o]=c
        if l[o]<n[o]:
            c=l[o]
            l[o]=n[o]
            n[o]=c
        for j in np.arange(k[o], m[o],1): #longitude
            for i in np.arange(l[o], n[o],-1): #latitude
                outfile.write(" {0}".format([p[o],i,j]))
                outfile.write('\n')
                r+=1
outfile.close()
print (r)
print (len(p))
print (p)
