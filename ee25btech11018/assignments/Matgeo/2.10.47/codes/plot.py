import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.patches as mpatches

a_val = 1 / np.sqrt(3)

p = np.array([1, a_val, 1])
q = np.array([0, 1, a_val])
r = np.array([a_val, 0, 1])
origin = np.array([0, 0, 0])

vertices = [
    origin, p, q, r, p + q, q + r, r + p, p + q + r
]

faces = [
    [vertices[0], vertices[1], vertices[4], vertices[2]],
    [vertices[0], vertices[1], vertices[6], vertices[3]],
    [vertices[0], vertices[2], vertices[5], vertices[3]],
    [vertices[7], vertices[5], vertices[4], vertices[6]],
    [vertices[7], vertices[6], vertices[1], vertices[3]],
    [vertices[7], vertices[5], vertices[2], vertices[4]]
]

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

color_p = '#FF7F0E'  # orange
color_q = '#9467BD'  # purple
color_r = '#17BECF'  # teal
shaded_color = '#ffc0cb'  # pink

# Plot vectors
ax.quiver(*origin, *p, color=color_p, linewidth=3, arrow_length_ratio=0.15)
ax.quiver(*origin, *q, color=color_q, linewidth=3, arrow_length_ratio=0.15)
ax.quiver(*origin, *r, color=color_r, linewidth=3, arrow_length_ratio=0.15)

# Plot shaded volume - no automatic label, so use patch for legend
poly3d = Poly3DCollection(faces, facecolors=shaded_color,
                         edgecolors='gray', linewidths=1.2, alpha=0.7)
ax.add_collection3d(poly3d)

# Create custom legend handles
p_patch = mpatches.Patch(color=color_p, label='p')
q_patch = mpatches.Patch(color=color_q, label='q')
r_patch = mpatches.Patch(color=color_r, label='r')
vol_patch = mpatches.Patch(color=shaded_color, label='Volume', alpha=0.7)

ax.set_xlim([-0.5, 2.5])
ax.set_ylim([-0.5, 2.5])
ax.set_zlim([-0.5, 2.5])

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('3D Parallelepiped and Vectors for a=1/sqrt(3)')

# Add legend with custom patches
ax.legend(handles=[p_patch, q_patch, r_patch, vol_patch])

plt.show()

