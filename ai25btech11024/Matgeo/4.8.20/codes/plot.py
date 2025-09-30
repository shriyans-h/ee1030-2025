import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from mpl_toolkits.mplot3d import Axes3D

#local imports
from line.funcs import * 

#Given points
A = np.array(([2,3,4])).reshape(-1,1)
B = np.array(([-1,-3,2])).reshape(-1,1)

# Create a figure and a 3D Axes
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

a, b, c, d = 3, 2, 2, 5  # coefficients of the plane equation: ax + by + cz + d = 0

# Generate grid points for x and y
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)

# Calculate corresponding z values for each (x, y) pair to satisfy the plane equation
Z = (-a*X - b*Y - d) / c

# Plot the plane
ax.plot_surface(X, Y, Z, alpha=0.5)

#plot the line
ax.plot([A[0],B[0]],[A[1],B[1]],[A[2],B[2]],color='r') #label

# Scatter plot
tri_coords = np.block([A, B])  # Stack A, B vertically
ax.scatter(tri_coords[0, :], tri_coords[1, :], tri_coords[2, :], c='g')

ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

# Set limits and aspect ratio to magnify the plane
ax.set_xlim(-4, 4)  # Adjust limits based on your data
ax.set_ylim(-4, 4)  # Adjust limits based on your data
ax.set_zlim(-4, 4)  # Adjust limits based on your data
ax.set_box_aspect([1,1,1])  # Equal aspect ratio for x, y, and z axes

plt.grid() # minor
plt.axis('equal')

plt.savefig('../figs/img.png')
plt.show()
