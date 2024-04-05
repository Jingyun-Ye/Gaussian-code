#!/usr/bin/python

# python code to extract electronic energy(E) from mulitiple Gaussian output files to E.txt file.

import glob
import os


a=glob.glob('*.gjf.out')       
b=os.path.splitext(a[0])

HF = 0
log = []
E = open('E.txt','w')

for filename in a:
        n = filename.split('.')[0]
        E.write(n + ' ')
        log = open('%s.gjf.out' %n,'r')
        for line in log:
            if "SCF Done" in line:
                temp = line.split()
                HF = temp[4]
                E.write("      %s   \n" % HF)
        log.close()
        
E.close()

