#!/davinci/bin/python
#SBATCH --array=0-26
#SBATCH --gres=gpu:1
#SBATCH -p a
#SBATCH --job-name=PrtclMkr
#SBATCH --ntasks=1
import os
from classes import ElserParticle 
from eke import tools, spimage_tools, conversions, shell_functions
import numpy as np
import spimage
import matplotlib.pyplot as plt
"""
1. Create the particle
2. Generate the diffraction pattern
3. Multiple phase retrieveal (PRTF)
4. Output relevant data (What data is relevant?)

This should happen for each particle, with parameters size and photon intensity (logrange)( Feature size?).
"""
#Setup values
pattern_size_pixels = 1024
detector_distance = 740e-3
detector_pixel_size = 75e-6
wavelength = conversions.ev_to_m(1100)

#Iteration process
f_len = int(3)
p_len = int(3)
np_len = int(3)
index = int(os.environ["SLURM_ARRAY_TASK_ID"])

ps1 = np.linspace(20,200,p_len)
a = np.zeros((f_len,p_len,np_len))
ps3 = ps1[np.newaxis,:,np.newaxis] + a
particle_size = int(ps3.flatten()[index])

fs1 = np.linspace(particle_size/10,particle_size/5,f_len)
fs3 = fs1[:,np.newaxis,np.newaxis] + a
feature_size = int(fs3.flatten()[index])

np1 = np.linspace(3,5,np_len)
np3 = np1[np.newaxis,np.newaxis,:] + a
number_of_scattered_photons = 10**int(np3.flatten()[index])*(particle_size/20)**2 #10 is smallest radius

array_size = particle_size + 5
#Generate diffraction pattern
particle = ElserParticle(array_size, particle_size, feature_size)
detected_intensity, diffracted_wave, support  = particle.generate_pattern(pattern_size_pixels, detector_distance, detector_pixel_size, wavelength, number_of_scattered_photons)


#Write to file
img_detected_intensity = spimage_tools.image_from_array(detected_intensity)
img_diffracted_wave = spimage_tools.image_from_array(diffracted_wave)
img_support = spimage_tools.image_from_array(support)

version = 'testrun'

output_dir = '/scratch/fhgfs/elsin/' + version + '/particles/'
shell_functions.mkdir_p(output_dir)

filename1 = output_dir + '/p{0:06d}'.format(index) + '_detected_intensity.h5'
filename2 = output_dir + '/p{0:06d}'.format(index) + '_diffracted_wave.h5'
filename3 = output_dir + '/p{0:06d}'.format(index) + '_support.h5'
spimage.sp_image_write(img_detected_intensity,filename1,0)
spimage.sp_image_write(img_diffracted_wave,filename2,0)
spimage.sp_image_write(img_support,filename3,0)

image = np.fft.fftshift(np.fft.fft2(np.fft.fftshift(diffracted_wave)))
plt.imsave(output_dir + '/p{0:06d}'.format(index) + 'img.png', abs(image))
