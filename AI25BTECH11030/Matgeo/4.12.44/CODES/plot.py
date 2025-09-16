import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create grid for b and c
b_vals = np.linspace(-10, 10, 100)
c_vals = np.linspace(-10, 10, 100)
b_grid, c_grid = np.meshgrid(b_vals, c_vals)

# Calculate corresponding a using the plane equation a = 2c
a_grid = 2 * c_grid

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the plane
ax.plot_surface(a_grid, b_grid, c_grid, alpha=0.5, color='cyan', edgecolor='k')

ax.set_xlabel('a')
ax.set_ylabel('b')
ax.set_zlabel('c')
ax.set_title('3D Plot of plane: a - 2c = 0')

plt.show()
