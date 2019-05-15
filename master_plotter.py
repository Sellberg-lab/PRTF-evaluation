
# Master script to plot all important plots for a test particle
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import h5py
import sys

mpl.rcParams.update({'font.size':14})

# cl args
input_dir = sys.argv[1]

# file imports
shape_file = input_dir + 'particle_shape.hdf5'
intensity_file = input_dir + 'particle_detected_intensity.h5'
phase_file = input_dir + 'particle_diffracted_wave.h5'
rec_fft_file = input_dir + 'prtf/prtf-avg_fft.h5'
rec_img_file = input_dir + 'prtf/prtf-avg_image.h5'

# image configs
xpixels = 1024
ypixels = 1024
dpi = 128

########### TRUE PROJECTION PLOT

with h5py.File(shape_file, 'r') as f:
    particle = f['particle_matrix'][:].sum(axis=0)
    fs = int(f['particle_matrix'].attrs.get('feature_size')*100)
    photons = int(f['particle_matrix'].attrs.get('n_photons')/1000)

particle = particle/particle.max()

plt.imshow(particle, cmap='viridis', norm = mpl.colors.Normalize(vmin=particle.min(), vmax=particle.max()), interpolation='none')
plt.colorbar()
plt.clim(0,1)
plt.xlabel('x [pixel]')
plt.ylabel('y [pixel]')
# plt.show()
plt.savefig(
    input_dir + 'particle_projection_fs{}_p{}.eps'.format(fs, photons))

########## DIFFRACTION PATTERN PLOT

with h5py.File(intensity_file, 'r') as f:
    intensity = f['real'][:].reshape((1024,1024))

# plot log plots without background
intensity = np.log(intensity)
#normalize
intensity = intensity/intensity.max()

plt.imshow(intensity, vmin=0.001, vmax=1, cmap='viridis', interpolation='none')
cmap = mpl.cm.viridis
cmap.set_under('white', 1.)
cmap.set_bad('white',1.)
plt.colorbar()
plt.xlabel('x [pixel]')
plt.ylabel('y [pixel]')

plt.savefig(
    input_dir + 'diffraction_pattern_log_fs{}_p{}.eps'.format(fs, photons))
plt.clf()
#plt.show()


########## TRUE PHASE PLOT

with h5py.File(phase_file, 'r') as f:
    imag = f['imag'][:].reshape((1024,1024))
    real = f['real'][:].reshape((1024,1024))

phase = np.angle(real + imag*1j)
plt.imshow(phase, interpolation='none')
plt.xlabel('x [pixel]')
plt.ylabel('y [pixel]')
plt.colorbar()

plt.savefig(input_dir + 'phase_true_fs{}_p{}.eps'.format(fs, photons))
plt.clf()
#plt.show()

########## RECONSTRUCTED PROJECTION PLOT CROPPED

with h5py.File(rec_img_file, 'r') as f:
    image = np.fft.fftshift(f2['real'][:].reshape((1024,1024)))

image_cropped = image[486:538,486:538]
# normalize
image_cropped = image_cropped / image_cropped.max()

plt.imshow(image_cropped, interpolation='none')
plt.colorbar()
plt.xlabel('x [pixel]')
plt.ylabel('y [pixel]')
plt.savefig(input_dir + 'particle_image_rec_cropped_fs{}_p{}.eps'.format(fs, photons))
plt.clf()

########## RECONSTRUCTED PHASE PLOT

with h5py.File(rec_fft_file, 'r') as f:
    fft_real = np.fft.fftshift(f1['real'][:].reshape((1024,1024)))
    fft_imag = np.fft.fftshift(f1['imag'][:].reshape((1024,1024)))

phase_rec = np.angle(fft_real + fft_imag*1j)

plt.imshow(phase_rec, interpolation='none')
plt.colorbar()
plt.xlabel('x [pixel]')
plt.ylabel('y [pixel]')
plt.savefig(target_dir + 'particle_phase_reconstructed_fs{}_p{}.eps'.format(fs, photons))
plt.clf()
