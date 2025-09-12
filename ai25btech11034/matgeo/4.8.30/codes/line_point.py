import numpy as np
import matplotlib.pyplot as plt

# Given data
P = np.array([[-2], [3], [2]], dtype=float)   # Column vector
A = np.array([[-2], [3], [0]], dtype=float)   # Column vector
v = np.array([[2], [-3], [6]], dtype=float)   # Column vector

# Matrix method: (v^T v) t = v^T (P - A)
lhs = (v.T @ v)        # 1x1 matrix
rhs = v.T @ (P - A)    # 1x1 matrix
t = np.linalg.solve(lhs, rhs)[0, 0]

# Foot of perpendicular Q
Q = A + v * t

# Distance
distance = np.linalg.norm(P - Q)

print("Shortest distance =", distance)
print("Foot of perpendicular Q =", Q.ravel())

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Line points
k_vals = np.linspace(-2, 2, 50)
line_points = A + v * k_vals
ax.plot(line_points[0, :], line_points[1, :], line_points[2, :], 'b', label="Line")

# Plot P and Q
ax.scatter(*P.ravel(), color='r', s=60, label="Point P")
ax.scatter(*Q.ravel(), color='g', s=60, label="Foot Q")

# Perpendicular PQ
ax.plot([P[0,0], Q[0,0]], [P[1,0], Q[1,0]], [P[2,0], Q[2,0]], 'm--', label="Perpendicular")

# Labels
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.legend()
ax.set_title("Shortest Distance: Matrix Method ")

# Save figure
plt.savefig("../figures/point_to_line_distance_matrix.png", dpi=300)
plt.show()

