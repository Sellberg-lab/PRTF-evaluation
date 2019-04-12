from classes import ElserParticle
from eke import elser_particles as ep
from eke import tools, spimage_tools, conversions, shell_functions
import numpy as np
import spimage
import matplotlib.pyplot as plt
import sys
import h5py

# experimental constants
pattern_size_pixels = 1024
detector_distance = 740e-3
detector_pixel_size = 75e-6
wavelength = conversions.ev_to_m(1100)

#n_photons = 2500000

n_photons = 2500000

# command line arguments
output_dir = sys.argv[1]
particle_id = sys.argv[2]
particle_size = int(sys.argv[3])
feature_size = int(sys.argv[4])
array_size = particle_size + 5

# Generate particle
particle = ElserParticle(array_size, particle_size, feature_size)

output_dir = output_dir + 'particle_' + particle_id
shell_functions.mkdir_p(output_dir)

file1 = output_dir + '/map3d.h5'

with h5py.File(file1, "w") as f:
    dset = f.create_dataset("data", data=particle.particle)
    dset.attrs['particle_size'] = particle_size
    dset.attrs['feature_size'] = feature_size
    dset.attrs['array_size'] = array_size
    dset.attrs['n_photons'] = n_photons

