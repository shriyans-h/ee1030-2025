import sys
sys.path.insert(0, '/home/dhanush-sagar/matgeo/codes/CoordGeo')
import numpy as np
import matplotlib.pyplot as plt

# Local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

# Load points
points = np.loadtxt("points.dat")
A, B, C = points

# Plot triangle
tri_coords = np.vstack((A, B, C, A))  # close loop
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(tri_coords[:,0], tri_coords[:,1], tri_coords[:,2], 'b-o', label='Triangle ABC')

# Mark points
ax.text(A[0], A[1], A[2], "A", color='red')
ax.text(B[0], B[1], B[2], "B", color='red')
ax.text(C[0], C[1], C[2], "C", color='red')

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.legend()
plt.savefig("triangle_plot.png")
plt.show()

