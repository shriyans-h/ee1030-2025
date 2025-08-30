import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Triangle vertices
A = np.array([0, 4, 0])
B = np.array([0, 0, 0])
C = np.array([3, 0, 0])

# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the triangle edges
triangle_edges = np.array([A, B, C, A])  # Loop back to A
ax.plot(triangle_edges[:,0], triangle_edges[:,1], triangle_edges[:,2], 'b', marker='o')

# Annotate points
ax.text(A[0], A[1], A[2], 'A', color='red')
ax.text(B[0], B[1], B[2], 'B', color='red')
ax.text(C[0], C[1], C[2], 'C', color='red')

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Triangle Diagram')

# Set equal aspect ratio for all axes
ax.set_box_aspect([1,1,0.5])

plt.show()
