    import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define vectors
a = np.array([3, 0, 0])   # vector a
b = np.array([0, 4, 0])   # vector b
c = np.array([0, 0, 5])   # vector c

# Origin
O = np.array([0, 0, 0])

# Resultant
R = a + b + c
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot coordinate axes
ax.quiver(0, 0, 0, 6, 0, 0, arrow_length_ratio=0.1, color='k')
ax.quiver(0, 0, 0, 0, 6, 0, arrow_length_ratio=0.1, color='k')
ax.quiver(0, 0, 0, 0, 0, 6, arrow_length_ratio=0.1, color='k')

# Plot vectors a, b, c
ax.quiver(*O, *a, color='black', linewidth=2)
ax.text(*a, r'$\vec{a}$', color='black')

ax.quiver(*O, *b, color='black', linewidth=2)
ax.text(*b, r'$\vec{b}$', color='black')

ax.quiver(*O, *c, color='black', linewidth=2)
ax.text(*c, r'$\vec{c}$', color='black')
# Plot resultant vector
ax.quiver(*O, *R, color='red', linewidth=2)
ax.text(*R, r'$\vec{a}+\vec{b}+\vec{c}$', color='red')

# Dashed parallelepiped edges
ax.plot([a[0], R[0]], [a[1], R[1]], [a[2], R[2]], 'k--')
ax.plot([b[0], R[0]], [b[1], R[1]], [b[2], R[2]], 'k--')
ax.plot([c[0], R[0]], [c[1], R[1]], [c[2], R[2]], 'k--')

# Labels and limits
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title("Fig. 4")

ax.set_xlim([0, 6])
ax.set_ylim([0, 6])
ax.set_zlim([0, 6])

plt.show()