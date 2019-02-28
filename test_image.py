from classes import ElserParticle
from eke import elser_particles as ep
#from eke import tools, spimage_tools, conversions, shell_functions
import numpy as np
#import spimage
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
np.random.seed(100)
import time

starttime=time.clock()


# Constants
pattern_size_pixels = 1024
detector_distance = 740e-3
detector_pixel_size = 75e-6
#wavelength = conversions.ev_to_m(1100)

# particle constants
particle_size = 200
feature_size = 25
array_size = particle_size + 5
n_photons = 2500000


# Generating diffraction pattern
particle = ElserParticle(array_size, particle_size, feature_size)
#print(particle.particle)

maxvalue=np.amax(particle.particle)


threshold=0.01*maxvalue
#print(maxvalue)
midval=int(array_size/2)

xlist=[]
ylist=[]
clist=[]

#for x in range (len(particle.particle[:][0][0])):
#    for y in range (len(particle.particle[:][0][0])):
#        for z in range (len(particle.particle[:][0][0])):
#            if particle.particle[x][y][z]>0:
#                xlist.append(x)
#                ylist.append(y)
#                zlist.append(z)
                
for x in range (len(particle.particle[:][0][0])):
    for y in range (len(particle.particle[:][0][0])):
        if particle.particle[x][y][midval]>threshold:
            xlist.append(x)
            ylist.append(y)
            clist.append(particle.particle[x][y][midval])


plt.scatter(xlist,ylist,c=clist)
plt.axis('equal')
plt.show()
plt.savefig('orginalbild.png')

endtime=time.clock()
print(str(endtime-starttime))