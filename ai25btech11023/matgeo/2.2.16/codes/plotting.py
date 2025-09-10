import sys                                          #for path to external scripts

import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from mpl_toolkits.mplot3d import Axes3D

#local imports
#from line.funcs import *
#from triangle.funcs import *
#from conics.funcs import circ_gen

#if using termux
import subprocess
import shlex
#end if

# Read plane data from output.data file
plane_data = np.loadtxt('output.data')

# Extract normal vectors and d constants
n1 = plane_data[0, :3]
d1 = plane_data[0, 3]
n2 = plane_data[1, :3]
d2 = plane_data[1, 3]

# Generate meshgrid for x and y
x = np.linspace(-5, 10, 50)
y = np.linspace(-5, 10, 50)
xx, yy = np.meshgrid(x, y)

def solve_for_z(normal, d, xx, yy):
    a, b, c = normal
    # Check if c != 0 to solve for z
    if c != 0:
        return (-a * xx - b * yy - d) / c
    else:
        # If c == 0, the plane is vertical, so return None here
        return None

# Calculate z for each plane
zz1 = solve_for_z(n1, d1, xx, yy)
zz2 = solve_for_z(n2, d2, xx, yy)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Plot plane 1 if z coords were found
if zz1 is not None:
    ax.plot_surface(xx, yy, zz1, alpha=0.5, color='blue', label='Plane 1')

# Plot plane 2 if z coords were found, else plot vertical plane differently
if zz2 is not None:
    ax.plot_surface(xx, yy, zz2, alpha=0.5, color='red', label='Plane 2')
else:
    # For vertical planes (c=0), solve for alternative variable (like x or y)
    # Here, if c=0 for plane 2, plot by solving for x instead: a*x + b*y = -d
    # So, x = (-b*y - d)/a (if a != 0)
    a, b, c = n2
    if a != 0:
        xx_alt = np.linspace(-5, 10, 50)
        yy_alt = np.linspace(-5, 10, 50)
        yy_alt, zz_alt = np.meshgrid(yy_alt, xx_alt)
        xx_alt = (-b * yy_alt - d2) / a
        ax.plot_surface(xx_alt, yy_alt, zz_alt, alpha=0.5, color='red', label='Plane 2 (vertical)')
    else:
        print("Plane 2 has c=0 and a=0, special handling needed")

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
plt.title('Planes from output.data')
#if using termux
plt.savefig('../figs/fig.png')
plt.show()
