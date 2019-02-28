from classes import ElserParticle
from eke import elser_particles as ep
from eke import tools, spimage_tools, conversions, shell_functions
import numpy as np
import spimage
import matplotlib.pyplot as plt

# Constants
pattern_size_pixels = 1024
detector_distance = 740e-3
detector_pixel_size = 75e-6
wavelength = conversions.ev_to_m(1100)

# particle constants
particle_size = 200
feature_size = 40
array_size = particle_size + 5
n_photons = 2500000


# Generating diffraction pattern
particle = ElserParticle(array_size, particle_size, feature_size)
detected_intensity, diffracted_wave, support = particle.generate_pattern(
    pattern_size_pixels, detector_distance, detector_pixel_size, wavelength, n_photons)


# image generation
img_particle = spimage_tools.image_from_array(particle.particle)
img_detected_intensity = spimage_tools.image_from_array(detected_intensity)
img_diffracted_wave = spimage_tools.image_from_array(diffracted_wave)
img_support = spimage_tools.image_from_array(support)

output_dir = '/scratch/fhgfs/elsin/testing/'
shell_functions.mkdir_p(output_dir)

file1 = output_dir + '/particle_detected_instensity.h5'
file2 = output_dir + '/particle_diffracted_wave.h5'
file3 = output_dir + '/particle_support.h5'
file4 = output_dir + '/particle_shape.h5'

spimage.sp_image_write(img_detected_intensity, file1, 0)
spimage.sp_image_write(img_diffracted_wave, file2, 0)
spimage.sp_image_write(img_support, file3, 0)
spimage.sp_image_write(img_particle, file4, 0)

image = np.fft.fftshift(np.fft.fft2(np.fft.fftshift(diffracted_wave)))
plt.imsave(output_dir + '/p_img.png', abs(image))
