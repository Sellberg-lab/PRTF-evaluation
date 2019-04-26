# Class for generating an Elser Particle for testing diffraction patterns
# Takes inputs for particle and detector in SI units
# By Vidar Elsin, based on generate_single by Tomas Ekeberg and classes.py by August Wolter

from eke import elser_particles
from eke import conversions
from eke import tools
import numpy as np

# SETUP AND DETECTOR SETTINGS

pattern_size_pixels = 1024
detector_distance = 400.e-3 
detector_pixel_size = 75e-6
wavelength = conversions.ev_to_m(1100) # ca 1.127 nm
#number_of_photons = 2.5e6
number_of_photons = 1e9 #high
#number_of_photons = 2.5e4 #low


# Small angle approximation
max_scattering_angle = (pattern_size_pixels*detector_pixel_size)/(2*detector_distance)
real_space_pixel_size = wavelength / max_scattering_angle

settings = {'pattern_size_pixels': pattern_size_pixels,
            'detector_distance': detector_distance,
            'detector_pixel_size': detector_pixel_size,
            'wavelength': wavelength,
            'number_of_photons': number_of_photons,
            'real_space_pixel_size': real_space_pixel_size,
            }


class ElserParticle:
    """Elser Particle class, particle size should be given in meters, feature size 
should be relative to particle size (ie 0.2)
"""
    def __init__(self, particle_size, feature_size, return_blurred=True):
        self.particle_size = particle_size
        self.feature_size = feature_size
        self.particle_size_pixels = int(particle_size/real_space_pixel_size)
        self.particle_feature_size_pixels = int(self.feature_size*self.particle_size_pixels)
        self.array_size = self.particle_size_pixels + 2
        self.particle = elser_particles.elser_particle(self.array_size, self.particle_size_pixels, self.particle_feature_size_pixels, return_blured=True)
        self.settings = settings

    def generate_pattern(self):
        real_space = np.zeros((pattern_size_pixels, )*2)
        support = tools.circular_mask(pattern_size_pixels, self.particle_size_pixels/2)

        # Project particle and FFT to simulate diffraction
        tools.insert_array_at_center(real_space, self.particle.sum(axis=0))
        diffracted_wave = np.fft.fftshift(np.fft.fft2(np.fft.fftshift(real_space)))
        rescale_factor = np.sqrt(number_of_photons/ (abs(diffracted_wave)**2).sum())
        diffracted_wave *= rescale_factor
        real_space *= rescale_factor

        detected_intensity = np.random.poisson(abs(diffracted_wave)**2)

        return detected_intensity, diffracted_wave, support, real_space
