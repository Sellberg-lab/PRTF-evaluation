# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 23:39:49 2019

@author: Alfred
"""
import os


particleList= ["particle_001","particle_002","particle_003","particle_004","particle_005","particle_006"]

for i,particle in enumerate(particleList):
    command1="cp ../elsin/scratch/test_particles/"+particle+"/particle_diffracted_wave.h5"
    command2="cp ../elsin/scratch/test_particles/"+particle+"/particle_shape.hdf5"
    command3="cp ../elsin/scratch/test_particles/"+particle+"/particle_support.h5"
    dest = " /home/alfredn/scratch/Gaussian_test_particlesv2/"+particle
    
    os.system(command1+dest)
    os.system(command2+dest)
    os.system(command3+dest)
    