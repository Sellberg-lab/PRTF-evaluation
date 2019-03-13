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
array_size = dset.attrs.get('array_size')


maxvalue = np.max(dset)


threshold = 0.01*maxvalue
# print(maxvalue)
midval = int(array_size/2)

xlist = []
ylist = []
clist = []

# for x in range (len(particle.particle[:][0][0])):
#    for y in range (len(particle.particle[:][0][0])):
#        for z in range (len(particle.particle[:][0][0])):
#            if particle.particle[x][y][z]>0:
#                xlist.append(x)
#                ylist.append(y)
#                zlist.append(z)

for x in range(len(dset[:][0][0])):
    for y in range(len(dset[:][0][0])):
        if dset[x][y][midval] > threshold:
            xlist.append(x)
            ylist.append(y)
            clist.append(dset[x][y][midval])


plt.scatter(xlist, ylist, c=clist)
plt.axis('equal')
# plt.show()
plt.savefig(input_dir + 'particle_slice.png')
