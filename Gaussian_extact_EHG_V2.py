#!/usr/bin/python

import glob
import os


a=glob.glob('*.gjf.out')       
b=os.path.splitext(a[0])

temp = 0
HF = 0
H = 0
G = 0
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
            if "Enthalpies" in line: 
                temp1 = line.split()
                H = temp1[6]
            if "Free Energies" in line:
                temp2 = line.split()
                G = temp2[7]
                E.write(" HF= %s  H= %s  G= %s \n " % (HF,H,G))
        log.close()
        
E.close()

