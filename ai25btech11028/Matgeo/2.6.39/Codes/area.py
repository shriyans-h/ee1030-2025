import numpy as np
import matplotlib.pyplot as plt

# Points A, B, C, D
A = np.array([0, 4, 1])
B = np.array([2, 3, -1])
C = np.array([4, 5, 0])
D = np.array([2, 6, 2])

# Diagonals
P = C - A
Q = D - B

# Cross product & area
cross = np.cross(P, Q)
area = 0.5 * np.linalg.norm(cross)
print("Area (NumPy) =", area)

# --- Plot quadrilateral ---
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

X = [A[0], B[0], D[0], C[0], A[0]]
Y = [A[1], B[1], D[1], C[1], A[1]]
Z = [A[2], B[2], D[2], C[2], A[2]]

ax.plot(X, Y, Z, 'r-', marker='o')
ax.set_title("Quadrilateral in 3D (NumPy)")
plt.show()
