# PRTF-evaluation
Scripts to evaluate the correctness of the phase-retrieval transfer function


## How to use
###Create a test particle:
Use the script test_particles.py to create a binary contrast test particle.
The parameters of the particle and imaging conditions are set inside the script,
such as particle size, feature size, detector settings. Run the script with the 
output directory as a command line argument. A folder will be created based on
the particle id specified in script. The outputs are in the form of hdf5 files 
containing the relevant particle data:

particle_diffracted_wave.h5	 Fourier transform of the binary contrast matrix
particle_detected_intensity.h5	 Poisson distribution using fourier amplitudes squared as lambda
particle_support.h5		 A circular mask showing location of the particle
particle_shape.hdf5		 Contains the binary contrast matrix, parameters

example:

python test_particles.py /home/elsin/scratch/test_particles/

Will result in a test particle at:

/home/elsin/scratch/test_particles/particle_{particle_id}/

