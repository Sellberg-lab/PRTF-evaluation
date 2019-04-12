# Script to convert the create_test_particle.py particle data file into
# the format required for condor

import h5py
import sys

input_dir = sys.argv[1]
output_dir = sys.argv[2]

input_file = input_dir + 'particle_shape.hdf5'

with h5py.File(input_file, 'r') as f:
    data = f['particle_matrix'][:]

output_file = output_dir + 'map3d.h5'

with h5py.File(output_file, 'w') as f:
    dset = f.create_dataset('data', data=data)

