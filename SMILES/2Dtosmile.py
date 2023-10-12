#!/bin/python3
import subprocess
import os

mols_2D = list(os.listdir('2D_structures'))

for mol in mols_2D:
    subprocess.run(['osra','2D_structures/'+mol,'-w','molecules/'+mol+'.txt'])
