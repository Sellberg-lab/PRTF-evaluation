from eke import elser_particles as ep
from eke import conversions
from eke import tools
from eke import spimage_tools
from matplotlib import pyplot as plt
import numpy as np

class ElserParticle:
    """A class describing a Elser Particle, array_size and particle_size should be given in pixels."""
    def __str__(self):
        return 'A particle of size ' + str(self.particle_size)
    def __init__(self, array_size, particle_size, feature_size, return_blured = True):
        self.array_size = array_size
        self.particle_size = particle_size 
        self.feature_size = feature_size
        self.particle = ep.elser_particle(array_size, particle_size, feature_size, return_blured)
    def show(self,show = True):
        #"""Plots the particle, displays if show = True"""
        plt.clf()
        plt.imshow(self.particle.sum(axis = 0))
        if show:
            plt.show()

    def wave(self, show = False):
        #"""Fourier transforms the particle, displays if show = true"""
        self.wave = np.fft.fftshift(np.fft.fft2(np.fft.fftshift(self.particle.sum(axis=0))))        
        if show:
            plt.clf()
            plt.imshow(abs(self.wave))
            plt.show()
        return self.wave
    def generate_pattern(
        self, 
        pattern_size_pixels = 1024,
        detector_distance = 740e-3,
        detector_pixel_size = 75e-6,
        wavelength = conversions.ev_to_m(1100),
        number_of_scattered_photons = 1e9):
        
        #Method for simulating a diffraction pattern, based on generate_single.py by Tomas Ekeberg. Wavelength in meters.
        
        # Small angle approximation    
        max_scattering_angle = pattern_size_pixels * detector_pixel_size / (2 * detector_distance)
        real_space_pixel_size = wavelength / (max_scattering_angle * 2)
        # Sample is self 
        real_space = np.zeros((pattern_size_pixels, ) *2)
        support = tools.circular_mask(pattern_size_pixels, self.particle_size/2)
        
        # Use FFT to simulate diffraction pattern
        tools.insert_array_at_center(real_space, self.particle.sum(axis=0))
        diffracted_wave = np.fft.fftshift(np.fft.fft2(np.fft.fftshift(real_space)))
        rescale_factor = np.sqrt(number_of_scattered_photons / (abs(diffracted_wave)**2).sum())
        diffracted_wave *= rescale_factor 
        real_space *= rescale_factor

        detected_intensity = np.random.poisson(abs(diffracted_wave)**2)
        
        #Utput
        return detected_intensity, diffracted_wave, support
