#!/usr/bin/python

import glob
import os
import shutil
import subprocess
import re

bs=['STO-3G', '3-21G', '6-31G', '6-311G']


for i in bs:
    filename=i+'.gjf'
    shutil.copy('C2H4.gjf', filename)
  #  gjf=open(filename, 'w+')
    with open(filename,'r') as f:
        inp=f.read()
        inp=inp.replace('bs', i)
        inp=inp.replace('ppp', i)

    with open(filename,'w') as f:
        f.write(inp)
        f.close()
