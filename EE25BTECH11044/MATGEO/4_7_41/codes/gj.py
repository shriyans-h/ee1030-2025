import numpy as np
import matplotlib.pyplot as plt

# Step 1: Define the augmented matrix (x, y, z, λ)
A = np.array([
    [ 1,  0,  0, -1, -5],   # x - λ = -5
    [ 0,  1,  0, -4, -3],   # y - 4λ = -3
    [ 0,  0,  1,  9,  6],   # z + 9λ = 6
    [-1, -4,  9,  0, -27]   # -x - 4y + 9z = -27
], dtype=float)

# Step 2: Gaussian elimination (to RREF)
def gauss_jordan(mat):
    rows, cols = mat.shape
    for i in range(rows):
        # Make pivot = 1
        pivot = mat[i, i]
        if pivot != 0:
            mat[i] = mat[i] / pivot
        # Eliminate other entries in column i
        for k in range(rows):
            if k != i:
                factor = mat[k, i]
                mat[k] = mat[k] - factor * mat[i]
    return mat

rref = gauss_jordan(A.copy())

# Extract solution (x,y,z,λ)
x, y, z, lam = rref[:, -1]
print(f"Solution: x = {x}, y = {y}, z = {z}, λ = {lam}")

# Step 3: Distance between P and Q
P = np.array([2, 4, -1])
Q = np.array([x, y, z])
dist = np.linalg.norm(P - Q)
print(f"Distance = {dist}")

# Step 4: Plot line, point, foot of perpendicular
# Line point A and direction vector d
A_line = np.array([-5, -3, 6])
d = np.array([1, 4, -9])

# Generate points on the line
t_vals = np.linspace(-2, 3, 100)
line_points = A_line.reshape(3,1) + d.reshape(3,1)*t_vals

# Plot
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

# Line
ax.plot(line_points[0], line_points[1], line_points[2], 'b-', label="Line")

# Point P
ax.scatter(P[0], P[1], P[2], color='r', s=60, label="Point P(2,4,-1)")

# Foot of perpendicular Q
ax.scatter(Q[0], Q[1], Q[2], color='g', s=60, label=f"Foot Q({x:.0f},{y:.0f},{z:.0f})")

# Perpendicular segment PQ
ax.plot([P[0], Q[0]], [P[1], Q[1]], [P[2], Q[2]], 'k--', label="Perpendicular")

# Labels and limits
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.legend()
ax.set_title("Distance of Point from Line in 3D")

ax.set_xlim(-6, 4)
ax.set_ylim(-5, 6)
ax.set_zlim(-10, 8)

plt.show()
