#!/davinci/Cellar/Python/miniconda3/envs/py2/bin/python
#SBATCH -p regular
#SBATCH -N8
#SBATCH --gres=gpu:1
#SBATCH --job-name=Phasing
#SBATCH --ntasks=1

import os
import sys
from eke import tools, shell_functions

number_of_runs = 100
particle = 'particle_001/'
input_dir = '/scratch/fhgfs/elsin/test_particles/' + particle
output_dir = input_dir + 'phasing_test/'

shell_functions.mkdir_p(output_dir)

for n in range(number_of_runs):
    os.system("python phase_particle.py {} {} {}".format(
        n, input_dir, output_dir))
