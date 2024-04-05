#!/usr/bin/env python

# extract xyz coordinates from multiple Gaussian outputfiles, and save to .xyz files
import glob
import os


a=glob.glob('*.gjf.out')
b=os.path.splitext(a[0])

start="Unable to Open any file for archive entry."
end="The archive entry for this job was punched."

for filename in a:
    n = filename.split('.')[0]
    log = open('%s.gjf.out' %n,'r')
    xyz = open('%s.xyz' %n,'w')
    geo=''
    count=0
    for line in log.readlines():
        if start in line:
            count+=1
        elif count>=1 and end not in line:
            i=line.replace('\n', '')
            geo+=i
        elif count>=1 and end in line:
            break
        
    #coord=repr(geo)
    coord=geo
    coord=coord.split("\\")
    coord=coord[16:-10]
    xyz.write("%s" %len(coord))
    xyz.write('\n'+'\n')

    for i in coord:
        i=i.replace(' ', '')
        i= i.replace(',', '  ')
        xyz.write("%s\n" %i)
    log.close()
    xyz.close()


