import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Points
x1, y1 = 5, 4
x2, y2 = 7, 1  # k = 1 (solution)
x3, y3 = 9, -2

# Create figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the points in 3D (z = 0 for 2D points)
ax.scatter([x1, x2, x3], [y1, y2, y3], [0, 0, 0], c='r', s=100, label='Points')

# Draw line through the points
xs = np.array([x1, x2, x3])
ys = np.array([y1, y2, y3])
zs = np.array([0, 0, 0])
ax.plot(xs, ys, zs, label='Collinear Line')

# Labels and title
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('3D Visualization of Collinear Points')
ax.legend()

# Save plot as picture
plt.savefig("collinear_points.png", dpi=300)

# Show the plot
plt.show()

print("Graph saved as collinear_points.png")