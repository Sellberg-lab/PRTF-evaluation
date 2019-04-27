# Script to plot a phase diagram of particle, with optional
# fft shift if necessary

import numpy as np
import h5py as h5
import matplotlib.pyplot as plt
import sys

target_dir = str(sys.argv[1])
filename = target_dir + 'particle_diffracted_wave.h5'
shift = False
if len(sys.argv) == 3:
    if sys.argv[2] == 'shift':
        shift = True

f = h5.File(filename, 'r')

# retrieve from h5 and remove useless 3rd dimension
imag = f['imag'][:].reshape((1024,1024))
real = f['real'][:].reshape((1024,1024))

# shifting
if shift:
    imag = np.fft.fftshift(imag)
    real = np.fft.fftshift(real)

phase = np.angle(real + imag*1j)

plt.imshow(phase)
plt.savefig(target_dir + 'particle_phase_true.svg', dpi=1000)
#plt.show()
