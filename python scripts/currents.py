import netCDF4
import scipy.interpolate
import numpy as np
import math


laty=[]
lony=[]

with open('latlong.txt') as f:
    for line in f:
        laty.append(line.split()[0])
        lony.append(line.split()[1])

nc=netCDF4.Dataset('grid_tpxo8atlas_30_v1.nc','r')
lat=nc.variables['lat_u'][:]
lon=nc.variables['lon_u'][:]
hu=nc.variables['hu'][:] #m
intp=scipy.interpolate.RegularGridInterpolator((lat,lon),hu.T)

latv=nc.variables['lat_v'][:]
lonv=nc.variables['lon_v'][:]
hv=nc.variables['hv'][:]
intp2=scipy.interpolate.RegularGridInterpolator((latv,lonv),hv.T)

#M2 COMPONENT
#u direction
ncm2=netCDF4.Dataset('uv.m2_tpxo8_atlas_30c_v1.nc','r')
uRem2=ncm2.variables['uRe'][:]
uIm2=ncm2.variables['uIm'][:]
uampm2=abs(uRem2+1j*uIm2) #cm2/s
intpum2=scipy.interpolate.RegularGridInterpolator((lat,lon),uampm2.T)

#v direction
vRem2=ncm2.variables['vRe'][:]
vIm2=ncm2.variables['vIm'][:]
vampm2=abs(vRem2+1j*vIm2) #cm2/s
intpvm2=scipy.interpolate.RegularGridInterpolator((latv,lonv),vampm2.T)

#S2 COMPONENT
#u direction
ncs2=netCDF4.Dataset('uv.s2_tpxo8_atlas_30c_v1.nc','r')
uRes2=ncs2.variables['uRe'][:]
uIms2=ncs2.variables['uIm'][:]
uamps2=abs(uRes2+1j*uIms2)
intpus2=scipy.interpolate.RegularGridInterpolator((lat,lon),uamps2.T)

#v direction
vRes2=ncs2.variables['vRe'][:]
vIms2=ncs2.variables['vIm'][:]
vamps2=abs(vRes2+1j*vIms2)
intpvs2=scipy.interpolate.RegularGridInterpolator((latv,lonv),vamps2.T)

#K1 COMPONENT
#u direction
nck1=netCDF4.Dataset('uv.k1_tpxo8_atlas_30c_v1.nc','r')
uRek1=nck1.variables['uRe'][:]
uImk1=nck1.variables['uIm'][:]
uampk1=abs(uRek1+1j*uImk1)
intpuk1=scipy.interpolate.RegularGridInterpolator((lat,lon),uampk1.T)

#v direction
vRek1=nck1.variables['vRe'][:]
vImk1=nck1.variables['vIm'][:]
vampk1=abs(vRek1+1j*vImk1)
intpvk1=scipy.interpolate.RegularGridInterpolator((latv,lonv),vampk1.T)

#K2 COMPONENT
#u direction
nck2=netCDF4.Dataset('uv.k2_tpxo8_atlas_30c_v1.nc','r')
uRek2=nck2.variables['uRe'][:]
uImk2=nck2.variables['uIm'][:]
uampk2=abs(uRek2+1j*uImk2)
intpuk2=scipy.interpolate.RegularGridInterpolator((lat,lon),uampk2.T)

#v direction
vRek2=nck2.variables['vRe'][:]
vImk2=nck2.variables['vIm'][:]
vampk2=abs(vRek2+1j*uImk2)
intpvk2=scipy.interpolate.RegularGridInterpolator((latv,lonv),vampk2.T)

#M4 COMPONENT
#u direction
ncm4=netCDF4.Dataset('uv.m4_tpxo8_atlas_30c_v1.nc','r')
uRem4=ncm4.variables['uRe'][:]
uImm4=ncm4.variables['uIm'][:]
uampm4=abs(uRem4+1j*uImm4)
intpum4=scipy.interpolate.RegularGridInterpolator((lat,lon),uampm4.T)

#v direction
vRem4=ncm4.variables['vRe'][:]
vImm4=ncm4.variables['vIm'][:]
vampm4=abs(vRem4+1j*vImm4)
intpvm4=scipy.interpolate.RegularGridInterpolator((latv,lonv),vampm4.T)

#N2 COMPONENT
#u direction
ncn2=netCDF4.Dataset('uv.n2_tpxo8_atlas_30c_v1.nc','r')
uRen2=ncn2.variables['uRe'][:]
uImn2=ncn2.variables['uIm'][:]
uampn2=abs(uRen2+1j*uImn2)
intpun2=scipy.interpolate.RegularGridInterpolator((lat,lon),uampn2.T)

#v direction
vRen2=ncn2.variables['vRe'][:]
vImn2=ncn2.variables['vIm'][:]
vampn2=abs(vRen2+1j*vImn2)
intpvn2=scipy.interpolate.RegularGridInterpolator((latv,lonv),vampn2.T)

#O1 COMPONENT
#u direction
nco1=netCDF4.Dataset('uv.k1_tpxo8_atlas_30c_v1.nc','r')
uReo1=nco1.variables['uRe'][:]
uImo1=nco1.variables['uIm'][:]
uampo1=abs(uReo1+1j*uImo1)
intpuo1=scipy.interpolate.RegularGridInterpolator((lat,lon),uampo1.T)

#v direction
vReo1=nco1.variables['vRe'][:]
vImo1=nco1.variables['vIm'][:]
vampo1=abs(vReo1+1j*vImo1)
intpvo1=scipy.interpolate.RegularGridInterpolator((latv,lonv),vampo1.T)

#P1 COMPONENT
#u direction
ncp1=netCDF4.Dataset('uv.p1_tpxo8_atlas_30c_v1.nc','r')
uRep1=ncp1.variables['uRe'][:]
uImp1=ncp1.variables['uIm'][:]
uampp1=abs(uRep1+1j*uImp1)
intpup1=scipy.interpolate.RegularGridInterpolator((lat,lon),uampp1.T)

#v direction
vRep1=ncp1.variables['vRe'][:]
vImp1=ncp1.variables['vIm'][:]
vampp1=abs(vRep1+1j*vImp1)
intpvp1=scipy.interpolate.RegularGridInterpolator((latv,lonv),vampp1.T)

#Q1 COMPONENT
#u direction
ncq1=netCDF4.Dataset('uv.q1_tpxo8_atlas_30c_v1.nc','r')
uReq1=ncq1.variables['uRe'][:]
uImq1=ncq1.variables['uIm'][:]
uampq1=abs(uReq1+1j*uImq1)
intpuq1=scipy.interpolate.RegularGridInterpolator((lat,lon),uampq1.T)

#v direction
vReq1=ncq1.variables['vRe'][:]
vImq1=ncq1.variables['vIm'][:]
vampq1=abs(vReq1+1j*vImq1)
intpvq1=scipy.interpolate.RegularGridInterpolator((latv,lonv),vampq1.T)

uk1=[]
vk1=[]
uk2=[]
vk2=[]
um2=[]
vm2=[]
um4=[]
vm4=[]
uk2=[]
vk2=[]
un2=[]
vn2=[]
us2=[]
vs2=[]
uo1=[]
vo1=[]
up1=[]
vp1=[]
uq1=[]
vq1=[]

laty=[float(x) for x in laty]
lony=[float(x) for x in lony]
laty=[x%360 for x in laty]
lony=[x%360 for x in lony]

for i in range(len(laty)):
    try:
        um2.append(intpum2((laty[i],lony[i]))/(intp((laty[i],lony[i]))*10000.))
    except ValueError:
        um2.append(0)
    try:
        vm2.append(intpvm2((laty[i],lony[i]))/(intp2((laty[i],lony[i]))*10000.))
    except ValueError:
        vm2.append(0)
    try:
        us2.append(intpus2((laty[i], lony[i])) / (intp((laty[i], lony[i])) * 10000.))
    except ValueError:
        us2.append(0)
    try:
        vs2.append(intpvs2((laty[i], lony[i])) / (intp2((laty[i], lony[i])) * 10000.))
    except ValueError:
        vs2.append(0)
    try:
        un2.append(intpun2((laty[i], lony[i])) / (intp((laty[i], lony[i])) * 10000.))
    except ValueError:
        un2.append(0)
    try:
        vn2.append(intpvn2((laty[i], lony[i])) / (intp2((laty[i], lony[i])) * 10000.))
    except ValueError:
        vn2.append(0)
    try:
        uk2.append(intpuk2((laty[i], lony[i])) / (intp((laty[i], lony[i])) * 10000.))
    except ValueError:
        uk2.append(0)
    try:
        vk2.append(intpvk2((laty[i], lony[i])) / (intp2((laty[i], lony[i])) * 10000.))
    except ValueError:
        vk2.append(0)
    try:
        uk1.append(intpuk1((laty[i], lony[i])) / (intp((laty[i], lony[i])) * 10000.))
    except ValueError:
        uk1.append(0)
    try:
        vk1.append(intpvk1((laty[i], lony[i])) / (intp2((laty[i], lony[i])) * 10000.))
    except ValueError:
        vk1.append(0)
    try:
        um4.append(intpum4((laty[i], lony[i])) / (intp((laty[i], lony[i])) * 10000.))
    except ValueError:
        um4.append(0)
    try:
        vm4.append(intpvm4((laty[i], lony[i])) / (intp2((laty[i], lony[i])) * 10000.))
    except ValueError:
        vm4.append(0)
    try:
        uo1.append(intpuo1((laty[i], lony[i])) / (intp((laty[i], lony[i])) * 10000.))
    except ValueError:
        uo1.append(0)
    try:
        vo1.append(intpvo1((laty[i], lony[i])) / (intp2((laty[i], lony[i])) * 10000.))
    except ValueError:
        vo1.append(0)
    try:
        up1.append(intpup1((laty[i], lony[i])) / (intp((laty[i], lony[i])) * 10000.))
    except ValueError:
        up1.append(0)
    try:
        vp1.append(intpvp1((laty[i], lony[i])) / (intp2((laty[i], lony[i])) * 10000.))
    except ValueError:
        vp1.append(0)
    try:
        uq1.append(intpuq1((laty[i], lony[i])) / (intp((laty[i], lony[i])) * 10000.))
    except ValueError:
        uq1.append(0)
    try:
        vq1.append(intpvq1((laty[i], lony[i])) / (intp2((laty[i], lony[i])) * 10000.))
    except ValueError:
        vq1.append(0)

for i in range(len(vm2)):
    if (math.isnan(vm2[i])):
        vm2[i]=0
    if(math.isnan(um2[i])):
        um2[i]=0
    if(math.isnan(vs2[i])):
        vs2[i]=0
    if(math.isnan(us2[i])):
        us2[i]=0
    if (math.isnan(uk1[i])):
        uk1[i] = 0
    if (math.isnan(vk1[i])):
        vk1[i] = 0
    if (math.isnan(vk2[i])):
        vk2[i] = 0
    if (math.isnan(uk2[i])):
        uk2[i] = 0
    if (math.isnan(vm4[i])):
        vm4[i] = 0
    if (math.isnan(um4[i])):
        um4[i] = 0
    if (math.isnan(vn2[i])):
        vn2[i] = 0
    if (math.isnan(un2[i])):
        un2[i] = 0
    if (math.isnan(vo1[i])):
        vo1[i] = 0
    if (math.isnan(uo1[i])):
        uo1[i] = 0
    if (math.isnan(vp1[i])):
        vp1[i] = 0
    if (math.isnan(up1[i])):
        up1[i] = 0
    if (math.isnan(vq1[i])):
        vq1[i] = 0
    if (math.isnan(uq1[i])):
        uq1[i] = 0

vel=[]

for i in range(len(vm2)):
    vel.append(math.sqrt(vm2[i]**2+um2[i]**2)+math.sqrt(vs2[i] ** 2 + us2[i] ** 2)+math.sqrt(vk1[i] ** 2 + uk1[i] ** 2)+math.sqrt(vm4[i] ** 2 + um4[i] ** 2)+math.sqrt(vk2[i] ** 2 + uk2[i] ** 2)+math.sqrt(vn2[i] ** 2 + un2[i] ** 2)+math.sqrt(vo1[i] ** 2 + uo1[i] ** 2)+math.sqrt(vp1[i] ** 2 + up1[i] ** 2)+math.sqrt(vq1[i] ** 2 + uq1[i] ** 2))

for i in range(len(vel)):
    print (str(vel[i]))