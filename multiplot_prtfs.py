# -*- coding: utf-8 -*-
"""
Created on Thu May 16 11:27:35 2019

@author: Alfred
"""

import os
input_folder=/home/elsin/scratch/test_particles/

output_loc=/home/alfredn/scratch/PRTFS/

particleList= ["particle_001","particle_002","particle_003","particle_004","particle_005","particle_006","particle_007","particle_008","particle_009"]

for i,particle in enumerate(particleList):

    command1="python eke_plot_prtf_labeled.py "+ input_folder +particle+"/prtf/prtf -w 1.127 -d 400000 -p 75 -ol "+output_loc+particle
    
    os.system(command1)
    