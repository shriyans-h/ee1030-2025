import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load shared library
lib = ctypes.CDLL("./function.so")
lib.compute_t.restype = ctypes.c_double
lib.compute_t.argtypes = [ctypes.POINTER(ctypes.c_double),
                          ctypes.POINTER(ctypes.c_double),
                          ctypes.POINTER(ctypes.c_double)]

def compute_t(P, A, v):
    # Convert numpy arrays to ctypes
    P_arr = (ctypes.c_double * 3)(*P)
    A_arr = (ctypes.c_double * 3)(*A)
    v_arr = (ctypes.c_double * 3)(*v)

    return lib.compute_t(P_arr, A_arr, v_arr)

# --- Given values ---
P = np.array([-2.0, 3.0, 2.0])   # Point
A = np.array([-2.0, 3.0, 0.0])   # Point on line
v = np.array([2.0, -3.0, 6.0])   # Direction vector

# Compute t using C function
t = compute_t(P, A, v)

# Foot of perpendicular Q
Q = A + t * v

# Distance
distance = np.linalg.norm(P - Q)

print("t =", t)
print("Foot of perpendicular Q =", Q)
print("Shortest distance =", distance)

# --- Plotting ---
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Line points
k_vals = np.linspace(-2, 2, 50)
line_points = A.reshape(3,1) + v.reshape(3,1) * k_vals
ax.plot(line_points[0, :], line_points[1, :], line_points[2, :], 'b', label="Line")

# Plot P and Q
ax.scatter(*P, color='r', s=60, label="Point P")
ax.scatter(*Q, color='g', s=60, label="Foot Q")

# Perpendicular PQ
ax.plot([P[0], Q[0]], [P[1], Q[1]], [P[2], Q[2]], 'm--', label="Perpendicular")

# Labels
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.legend()
ax.set_title("Shortest Distance from Point to Line ")

# Save figure
plt.savefig("../figures/point_to_line_with_c.png", dpi=300)
plt.show()

