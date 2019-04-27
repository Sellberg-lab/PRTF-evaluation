import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import h5py
import sys

# command line arguments
input_dir = sys.argv[1]

# file import
filename = input_dir + 'particle_shape.hdf5'

f = h5py.File(filename, 'r')
dset = f['particle_matrix']
particle_size = dset.attrs.get('particle_size')
feature_size = dset.attrs.get('feature_size')


particle = dset[:].sum(axis=0)
plt.imshow(particle)
# plt.show()
plt.savefig(
    input_dir + 'particle_projection_ps{}_fs{}.svg'.format(particle_size, feature_size), dpi=1000)
