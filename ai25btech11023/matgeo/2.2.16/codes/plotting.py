
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Read values from output.dat (space-separated)
with open('output.dat', 'r') as f:
    vals = [float(x) for x in f.read().split()]

# First plane coefficients and constant
n1_x, n1_y, n1_z, d1 = vals[0], vals[1], vals[2], vals[3]
# Second plane coefficients and constant
n2_x, n2_y, n2_z, d2 = vals[4], vals[5], vals[6], vals[7]
# cos_theta = vals[8]  # Not used for plotting

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Create grid for surface plot
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)

# Plane 1: n1_x*x + n1_y*y + n1_z*z = d1 -> z = (d1 - n1_x*X - n1_y*Y) / n1_z
Z1 = (d1 - n1_x*X - n1_y*Y) / n1_z
ax.plot_surface(X, Y, Z1, alpha=0.5, color="blue", label="Plane 1")

# Plane 2: n2_x*x + n2_y*y + n2_z*z = d2
if abs(n2_z) > 1e-8:
    Z2 = (d2 - n2_x*X - n2_y*Y) / n2_z
    ax.plot_surface(X, Y, Z2, alpha=0.5, color="red", label="Plane 2")
else:
    # For n2_z == 0, plane is vertical; draw as a 3D line where x - y = -4 (y = x + 4, z=0)
    x_line = np.linspace(-5, 5, 50)
    y_line = (d2 - n2_x*x_line) / n2_y
    z_line = np.zeros_like(x_line)
    ax.plot3D(x_line, y_line, z_line, color="red", linewidth=3, label="Plane 2")

# Scatter plot for example points - can be customized or removed
A = np.array([1, 1, 0])
B = np.array([1, 2, 1])
C = np.array([-2, 2, 1])
tri_coords = np.vstack([A, B, C])
ax.scatter(tri_coords[:,0], tri_coords[:,1], tri_coords[:,2], c='black')
for i, txt in enumerate(['A', 'B', 'C']):
    ax.text(tri_coords[i,0], tri_coords[i,1], tri_coords[i,2], f'{txt}', fontsize=12, ha='center', va='bottom')

# Set limits and aspect ratio
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_zlim(-5, 5)
ax.set_box_aspect([1,1,1])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Plot of Two Planes from output.dat')

# For legend with surface and line
from matplotlib.lines import Line2D
legend_elements = [Line2D([0], [0], color='blue', lw=4, label='Plane 1'),
                   Line2D([0], [0], color='red', lw=4, label='Plane 2')]
ax.legend(handles=legend_elements)

plt.grid()
plt.title('A,B and C are collinear')
plt.savefig('../figs/fig.png')
plt.show()
