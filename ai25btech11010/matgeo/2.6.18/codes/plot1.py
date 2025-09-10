import numpy as np
import matplotlib.pyplot as plt
import os

# Define the vertices of the triangle
A = np.array([-1, 0])
B = np.array([1, 3])
C = np.array([3, 2])

# Calculate area using cross product formula
area = 0.5 * np.abs(np.cross(B - A, C - A))
print(f"Area of the triangle: {area}")

# Prepare triangle points for plotting
triangle = np.array([A, B, C, A])  # repeat first point to close the triangle



# Plot the triangle
plt.plot(triangle[:, 0], triangle[:, 1], 'b-o', label='Triangle')
plt.fill(triangle[:, 0], triangle[:, 1], 'skyblue', alpha=0.3)
plt.text(A[0], A[1], 'A', fontsize=12, color='red')
plt.text(B[0], B[1], 'B', fontsize=12, color='red')
plt.text(C[0], C[1], 'C', fontsize=12, color='red')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Triangle Plot')
plt.grid(True)
plt.legend()

# Save the figure
plt.savefig('../figs/triangle_plot.png')
plt.show()

