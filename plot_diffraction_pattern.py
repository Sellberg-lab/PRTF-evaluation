# Visualizes the diffraction pattern of a particle from
# an h5 file of the fft

import numpy as np
import h5py
import matplotlib.pyplot as plt
import matplotlib
import sys

filename = str(sys.argv[1])
shift = False
if len(sys.argv) == 3:
    if sys.argv[2] == 'shift':
        shift = True

f = h5py.File(filename, 'r')

real = f['real'][:].reshape((1024,1024))

if 'imag' in f.keys():
    imag = f['imag'][:].reshape((1024,1024))

if shift:
    real = np.fft.fftshift(real)
    imag = np.fft.fftshift(imag)

if 'imag' in f.keys():
    intensity = np.abs(real + imag*1j)**2
else:
    intensity = real


#plot with 'background' removed
plt.imshow(intensity, vmin=20/1000., vmax=8900/1000., cmap='viridis')
cmap = matplotlib.cm.viridis
cmap.set_bad('grey',1.)
cmap.set_under('white',1.)




plt.show()
