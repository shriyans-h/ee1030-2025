
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Read coefficients and constants from output.dat
with open('output.dat', 'r') as f:
    vals = [float(x) for x in f.read().split()]
n1_x, n1_y, n1_z, d1 = vals[0], vals[1], vals[2], vals[3]
n2_x, n2_y, n2_z, d2 = vals[4], vals[5], vals[6], vals[7]

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-4, 4, 50)
y = np.linspace(-4, 4, 50)
X, Y = np.meshgrid(x, y)

# Plane 1: n1_x*x + n1_y*y + n1_z*z = d1 --> z = (d1 - n1_x*X - n1_y*Y)/n1_z
Z1 = (d1 - n1_x*X - n1_y*Y) / n1_z
ax.plot_surface(X, Y, Z1, alpha=0.5, color="blue")

# Plane 2: n2_x*x + n2_y*y + n2_z*z = d2
if abs(n2_z) < 1e-8:
    x2 = np.linspace(-4, 4, 50)
    y2 = (d2 - n2_x*x2) / n2_y
    z2 = np.zeros_like(x2)
    ax.plot3D(x2, y2, z2, color="red", linewidth=3)
else:
    Z2 = (d2 - n2_x*X - n2_y*Y)/n2_z
    ax.plot_surface(X, Y, Z2, alpha=0.5, color="red")

# Optional: Points and labels as in original code
A = np.array(([1, 1,0])).reshape(-1,1)
B = np.array(([1,2, 1])).reshape(-1,1)
C = np.array(([-2,2, 1])).reshape(-1,1)
tri_coords = np.block([A, B, C])
ax.scatter(tri_coords[0, :], tri_coords[1, :], tri_coords[2, :], c='black')
vert_labels = ['A', 'B', 'C']
for i, txt in enumerate(vert_labels):
    ax.text(tri_coords[0, i], tri_coords[1, i], tri_coords[2, i],f'{txt}',fontsize=12, ha='center', va='bottom')

ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.set_zlim(-4, 4)
ax.set_box_aspect([1,1,1])
plt.grid()
plt.savefig('../figs/fig.png')
plt.show()
