# Master script to run all the individual plotting scripts for a single test
# particle. Point it at the main particle directory

import os
import sys

target_dir = sys.argv[1]

os.system('python plot_diffraction_pattern.py {}'.format(target_dir))
os.system('python plot_phase_diagram.py {}'.format(target_dir))
os.system('python plot_real_space.py {}'.format(target_dir))
os.system('python plot_particle_projection.py {}'.format(target_dir))
os.system('python plot_prtf_results.py {}'.format(target_dir))
