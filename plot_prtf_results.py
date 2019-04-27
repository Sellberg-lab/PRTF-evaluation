# Short script to plot the data from particle PRTF in a format
# comparable to other outputs, ie shifted, phase plot

import h5py
import numpy as np
import sys
import matplotlib.pyplot as plt

target_dir = sys.argv[1] + 'prtf/'

f1 = h5py.File(target_dir + 'prtf-avg_fft.h5', 'r')
f2 = h5py.File(target_dir + 'prtf-avg_image.h5', 'r')

fft_real = np.fft.fftshift(f1['real'][:].reshape((1024,1024)))
fft_imag = np.fft.fftshift(f1['imag'][:].reshape((1024,1024)))

phase = np.angle(fft_real + fft_imag*1j)

plt.imshow(phase)
plt.savefig(target_dir + 'particle_phase_reconstructed.svg', dpi=1000)

image = np.fft.fftshift(f2['real'][:].reshape((1024,1024)))

plt.imshow(image)
plt.savefig(target_dir + 'particle_image_reconstructed.svg', dpi=1000)


