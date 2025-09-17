#code by Pratik R
#plot line
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from line.funcs import *

#if using termux
import subprocess
import shlex
#end if

#from Given line
A = np.array(([0,2])).reshape(-1,1)
B = np.array(([4/3,0])).reshape(-1,1)

#generating line
AB = line_gen(A,B)

plt.plot(AB[0,:],AB[1,:], label='3x+2y=4')

tri_coords = np.block([[A,B]])
plt.scatter(tri_coords[0,:],tri_coords[1,:])
vert_labels = ['A','B']
for i, txt in enumerate(vert_labels):
    plt.annotate(f'{txt}\n({tri_coords[0,i]:.0f}, {tri_coords[1,i]:.0f})',
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(20,-10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid() # minor
plt.axis('equal')


plt.savefig('../figs/fig.png')
