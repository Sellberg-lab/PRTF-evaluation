#!/davinci/bin/python
import numpy
import spimage
import sys
import os
from eke import spimage_tools
import h5py 
index = int(sys.argv[1])
run = int(sys.argv[2])
INPUT_DIR = sys.argv[3]
OUTPUT_DIR = sys.argv[4]   
numpy.random.seed()
spimage.sp_srand(numpy.random.randint(1e6))

NUMBER_OF_ITERATIONS = 10000
NUMBER_OF_REFINE_ITERATIONS = 1000

# Amplitudes
diffraction_pattern_file = os.path.join(INPUT_DIR,'p{0:06d}_detected_intensity.h5'.format(index))
diffraction_pattern_raw = spimage.sp_image_read(diffraction_pattern_file, 0)
amplitudes = spimage.sp_image_shift(diffraction_pattern_raw)
amplitudes.image[:] = numpy.sqrt(abs(amplitudes.image))
    #amplitudes.scaled = 1
    #amplitudes.phased = 0
    #amplitudes.shifted = 1

support_file = os.path.join(INPUT_DIR,'p{0:06d}_support.h5'.format(index))
support_raw = spimage.sp_image_read(support_file, 0)
support = spimage.sp_image_shift(support_raw)

sup_alg_static = spimage_tools.support_static()    #Our support is static

# phasing algorithm
beta = spimage_tools.smap(0.9)  #beta is a constant, 0.9, but in a format that spimage can read

    #constraints = spimage.SpNoConstraints
    #constraints = spimage.SpPositiveComplexObject 
constraints = spimage.SpPositiveRealObject   #Additional constraints, other than Fourier-constraint or Real-constraint.

phase_alg_main = spimage.sp_phasing_hio_alloc(beta, constraints) 
phase_alg_refine = spimage.sp_phasing_er_alloc(constraints)

# create phaser
phaser = spimage.sp_phaser_alloc()
spimage.sp_phaser_init(phaser, phase_alg_main, sup_alg_static, spimage.SpEngineCUDA)
spimage.sp_phaser_set_amplitudes(phaser, amplitudes)
spimage.sp_phaser_init_model(phaser, None, spimage.SpModelRandomPhases)
spimage.sp_phaser_init_support(phaser, support, 0, 0)

def run_it(number_of_iterations):
    spimage.sp_phaser_iterate(phaser, number_of_iterations)
    
run_it(NUMBER_OF_ITERATIONS)
    
phaser.algorithm = phase_alg_refine
run_it(NUMBER_OF_REFINE_ITERATIONS)
    #Output data
model = spimage.sp_phaser_model(phaser)
support = spimage.sp_phaser_support(phaser)
fmodel = spimage.sp_phaser_fmodel(phaser)
spimage.sp_image_write(model, OUTPUT_DIR + "index{0:06d}".format(index)+"run{0:06d}model.h5".format(run), 0)
spimage.sp_image_write(support, OUTPUT_DIR + "index{0:06d}".format(index)+"run{0:06d}support.h5".format(run), 0)
spimage.sp_image_write(fmodel, OUTPUT_DIR + "index{0:06d}".format(index)+"run{0:06d}fmodel.h5".format(run), 0)

ereal = spimage.sp_phaser_ereal(phaser)
efourier = spimage.sp_phaser_efourier(phaser)

filename = OUTPUT_DIR + 'index{0:06d}'.format(index) + 'run{0:06d}error.h5'.format(run)

with h5py.File(filename,'w') as file_handle:
    file_handle.create_dataset('ereal', data=ereal)
    file_handle.create_dataset('efourier', data=efourier)
    

