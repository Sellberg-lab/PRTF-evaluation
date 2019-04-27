# plot the real_space.h5 contents of a test particles and saves a high quality image

import numpy as np
import h5py
import matplotlib.pyplot as plt
import sys

target_dir = str(sys.argv[1])
filename = target_dir + 'particle_real_space.h5'

f = h5py.File(filename, 'r')

real = f['real'][:].reshape((1024,1024))

plt.imshow(real)

plt.savefig(target_dir + 'particle_real_space.svg', dpi=1000)



