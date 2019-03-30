# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 18:35:01 2019

@author: Alfred
"""

from gaussian_intensity import gaussian_intensity

particleList= ["particle_001","particle_002","particle_003","particle_004","particle_005","particle_006"]
std=0.1
for particle in particleList:
    full_filename="/home/alfredn/scratch/test_particles/"+particle+"/particle_detected_intensity.h5" 
    full_savefile="/home/alfredn/scratch/Gaussian_test_particles/"+particle+"/particle_detected_intensity.h5"
    gaussian_intensity(full_filename,full_savefile,std)
