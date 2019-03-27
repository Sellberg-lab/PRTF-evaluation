# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:40:07 2019

@author: Alfred
"""
import h5py
import numpy as np
from random import gauss
import time
timestr = time.strftime("%Y%m%d_%H%M%S")

#copies the input h5 file and creates a new h5 file only modifying the dataset 'real' with random gaussian values
def gaussian_intensity(file_name,save_file,std):
    std= std #standard dev = some % of detected intensity
    detected_intensity=file_name
    full_save_file= save_file + "_"+ timestr +".h5"
    
    f = h5py.File(detected_intensity,"r")
    real_intensity=f['real']
    setList=list(f.keys())
    
    d2=np.reshape(real_intensity,[real_intensity.shape[0],real_intensity.shape[1]])
    for x in range(d2.shape[0]):
        for y in range (d2.shape[1]):
            d2[x][y]= gauss(d2[x][y],d2[x][y]*std)
    
    d2=np.reshape(d2,real_intensity.shape)
    
    f2= h5py.File(full_save_file,"w")
    
    for i,dataset in enumerate(setList):
        if i==7:
            f2.create_dataset(dataset,data=d2)
        else:
            f2.create_dataset(dataset,data=f[dataset])
    print("File saved to "+full_save_file)

#test run
#gaussian_intensity("particle_detected_instensity.h5","gauss_intensity",0.1)