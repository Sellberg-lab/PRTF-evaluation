from particle_class import ElserParticle, settings
from eke import tools, spimage_tools, conversions, shell_functions
import numpy as np
import matplotlib.pyplot as plt
import spimage
import sys
import h5py



# command line arguments
output_dir = sys.argv[1]
particle_id = sys.argv[2]

particle_size = float(sys.argv[3]) # in meters
feature_size = float(sys.argv[4]) # as proportion of particle size
# detector settings are in the elser_particle file

# Generating diffraction pattern
particle = ElserParticle(particle_size, feature_size)
detected_intensity, diffracted_wave, support, real_space = particle.generate_pattern()


# saving data, with correct flags for further processing
img_detected_intensity = spimage_tools.image_from_array(detected_intensity)
img_detected_intensity.phased = 0
img_detected_intensity.shifted = 0
img_detected_intensity.detector.detector_distance = settings['detector_distance']
img_detected_intensity.detector.pixel_size[:] = settings['detector_pixel_size']
img_detected_intensity.detector.wavelength = settings['wavelength']

img_diffracted_wave = spimage_tools.image_from_array(diffracted_wave)
img_diffracted_wave.phased = 1
img_diffracted_wave.shifted = 0
img_diffracted_wave.detector.detector_distance = settings['detector_distance']
img_diffracted_wave.detector.pixel_size[:] = settings['detector_pixel_size']
img_diffracted_wave.detector.wavelength = settings['wavelength']

img_support = spimage_tools.image_from_array(support)
img_support.phased = 0
img_support.shifted = 0
img_support.detector.detector_distance = settings['detector_distance']
img_support.detector.pixel_size[:] = settings['detector_pixel_size']
img_support.detector.wavelength = settings['wavelength']

img_real_space = spimage_tools.image_from_array(real_space)
img_real_space.phased = 0
img_real_space.shifted = 0
img_real_space.detector.detector_distance = settings['detector_distance']
img_real_space.detector.pixel_size[:] = settings['detector_pixel_size']
img_real_space.detector.wavelength = settings['wavelength']

output_dir = output_dir + 'particle_' + particle_id
shell_functions.mkdir_p(output_dir)

file1 = output_dir + '/particle_detected_intensity.h5'
file2 = output_dir + '/particle_diffracted_wave.h5'
file3 = output_dir + '/particle_support.h5'
file4 = output_dir + '/particle_shape.hdf5'
file5 = output_dir + '/particle_real_space.h5'

spimage.sp_image_write(img_detected_intensity, file1, 0)
spimage.sp_image_write(img_diffracted_wave, file2, 0)
spimage.sp_image_write(img_support, file3, 0)
spimage.sp_image_write(img_real_space, file5, 0)

with h5py.File(file4, "w") as f:
    dset = f.create_dataset("particle_matrix", data=particle.particle)
    dset.attrs['particle_size'] = particle_size
    dset.attrs['feature_size'] = feature_size
    dset.attrs['n_photons'] = settings['number_of_photons']

image = np.fft.fftshift(np.fft.fft2(np.fft.fftshift(diffracted_wave)))
plt.imsave(output_dir + '/particle_projection_img.png', abs(image))
