# PRTF-evaluation
Scripts to evaluate the correctness of the phase-retrieval transfer function

## Example
### Create particle
To change detector settings and photon count, edit the file particle_class.py. Class is imported by create_elser_particle.py and used to create test particles and save the data.

python create_elser_particle.py {output directory} {particle id} {particle size in m} {feature size as decimal}

```python create_elser_particle.py /home/elsin/scratch/particles/ 001 450e-9 0.2```

Creates a test particle in the folder /home/elsin/scrath/particles/particle_001/

### Iterative phase retrieval
Edit the file multi_phase_particle.py to set the number of independant retrievals, target particle, input and output directories.

```sbatch multi_phase_particle.py```

### Phase retrieval transfer function 
Edit the file prtf.py to change input and output directories.

```sbatch prtf.py```

Plots of the PRTF were done using Tomas Ekeberg's Python Tools library.
While in the output directory of the prtf.py file:

```eke_plot_prtf.py prtf -w 1.127 -d 400000 -p 75```

### True vs reconstructed PRTF
Uses the prtf function from Hawk.

prtf {output name} {target files}

example from a subdirectory in the particle folder:

```prtf prtf_true_vs_rec prtf-avg_image.h5 ../particle_real_space.h5```

### Plotting
To create the images used in the report, run the script master_plotter.py on a target test partcicle directory.

example:

```python master_plotter.py /home/elsin/scratch/particles/particle_001/```




