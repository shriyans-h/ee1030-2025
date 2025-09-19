import matplotlib.pyplot as plt
import numpy as np

# Points based on the vector solution
A = np.array([1.5625, 2.705])  # approx coordinates
B = np.array([0.0, 0.0])
C = np.array([5.0, 0.0])

# Create the figure and axis
fig, ax = plt.subplots()

# Plot the triangle edges
triangle_points = np.array([A, B, C, A])  # back to A to close the triangle
ax.plot(triangle_points[:, 0], triangle_points[:, 1], 'b-', marker='o')

# Annotate points
ax.text(A[0], A[1], 'A', fontsize=12, ha='right', va='bottom')
ax.text(B[0], B[1], 'B', fontsize=12, ha='right', va='top')
ax.text(C[0], C[1], 'C', fontsize=12, ha='left', va='top')

# Set equal aspect ratio
ax.set_aspect('equal', 'box')

# Add grid, labels, and title
ax.grid(True, linestyle='--', alpha=0.6)
ax.set_xlabel('x (cm)')
ax.set_ylabel('y (cm)')
ax.set_title('Triangle ABC: BC=5 cm, ∠B=60°, AB+AC=7.5 cm')

# Add side lengths as annotations
AB_len = np.linalg.norm(A - B)
AC_len = np.linalg.norm(A - C)
BC_len = np.linalg.norm(B - C)

ax.text((A[0] + B[0]) / 2 - 0.3, (A[1] + B[1]) / 2, f"{AB_len:.3f} cm", color="red")
ax.text((A[0] + C[0]) / 2 + 0.2, (A[1] + C[1]) / 2, f"{AC_len:.3f} cm", color="red")
ax.text((B[0] + C[0]) / 2, (B[1] + C[1]) / 2 - 0.3, f"{BC_len:.1f} cm", color="red")

# Set limits for better visualization
padding = 1
min_x, max_x = min(A[0], B[0], C[0]) - padding, max(A[0], B[0], C[0]) + padding
min_y, max_y = min(A[1], B[1], C[1]) - padding, max(A[1], B[1], C[1]) + padding
ax.set_xlim(min_x, max_x)
ax.set_ylim(min_y, max_y)

# Save the plot as 'triangle_plot.png'
plt.savefig('triangle_plot.png', dpi=300)

# Show the plot
plt.show()
