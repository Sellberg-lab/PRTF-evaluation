#!/davinci/Cellar/Python/miniconda3/envs/py2/bin/python
#SBATCH -p regular
#SBATCH -N1
#SBATCH --job-name=PRTF
#SBATCH --ntasks=1

import os
import sys
from eke import shell_functions

detector_distance = 740000
detector_pixel_size = 75
wavelength = 1.127
particle = 'particle_015/'

input_dir = '/scratch/fhgfs/elsin/test_particles/' + particle
output_dir = input_dir + 'prtf/'
input_files = input_dir + '/phasing/run_*_model.h5'

shell_functions.mkdir_p(output_dir)
os.chdir(output_dir)
os.system("prtf prtf `ls {}`".format(input_files))
os.system("eke_plot_prtf.py prtf -w {} -d {} -p {}".format(
    wavelength, detector_distance, detector_pixel_size))
