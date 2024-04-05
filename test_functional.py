#!/usr/bin/python

import glob
import os
import shutil
import subprocess
import re

functional=['hf', 'LSDA', 'pbepbe', 'B3LYP', 'WB97XD']


for i in functional:
    filename=i+'.gjf'
    shutil.copy('H2.gjf', filename)
  #  gjf=open(filename, 'w+')
    with open(filename,'r') as f:
        inp=f.read()
        inp=inp.replace('hf', i)
        inp=inp.replace('ppp', i)

    with open(filename,'w') as f:
        f.write(inp)
        f.close()
