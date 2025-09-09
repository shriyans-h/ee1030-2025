import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define vectors
u = np.array([1, 2, 3])
v = np.array([4, 5, 6])
w = np.array([7, 8, 9])

# Cross product v × w
cross_vw = np.cross(v, w)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot vectors
ax.quiver(0, 0, 0, u[0], u[1], u[2], color='r', label='u')
ax.quiver(0, 0, 0, v[0], v[1], v[2], color='g', label='v')
ax.quiver(0, 0, 0, w[0], w[1], w[2], color='b', label='w')
ax.quiver(0, 0, 0, cross_vw[0], cross_vw[1], cross_vw[2], color='m', label='v×w')

ax.set_xlim([0, 10])
ax.set_ylim([0, 10])
ax.set_zlim([0, 10])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.title('Vector visualization')

# Optional: save the figure as an image
plt.savefig('vector_plot.png')

plt.show()

