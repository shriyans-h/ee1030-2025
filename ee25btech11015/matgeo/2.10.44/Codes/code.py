import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import ctypes
import os

# --- Load the C library ---
try:
    c_lib = ctypes.CDLL('./code.so')
except OSError:
    print("❌ Error: 'code.so' not found. Compile with:")
    print("   gcc -shared -o code.so -fPIC inequality.c -lm")
    exit()

# Define argument and return types
c_lib.is_within_bound.argtypes = [
    ctypes.c_float, ctypes.c_float, ctypes.c_float,
    ctypes.c_float, ctypes.c_float, ctypes.c_float,
    ctypes.c_float, ctypes.c_float, ctypes.c_float
]
c_lib.is_within_bound.restype = ctypes.c_int

# --- Function to generate random unit vector ---
def random_unit_vector():
    vec = np.random.randn(3)
    return vec / np.linalg.norm(vec)

# --- Generate unit vectors a, b, c ---
a = random_unit_vector()
b = random_unit_vector()
c = random_unit_vector()

# --- Call C function ---
result = c_lib.is_within_bound(a[0], a[1], a[2],
                               b[0], b[1], b[2],
                               c[0], c[1], c[2])

if result == 1:
    print("✅ The inequality holds (sum ≤ 9).")
else:
    print("❌ The inequality is violated.")

# --- Plotting ---
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

# Plot points
ax.scatter(*a, color="red", s=50)
ax.scatter(*b, color="blue", s=50)
ax.scatter(*c, color="green", s=50)

# Draw triangle
triangle = np.array([a, b, c])
ax.add_collection3d(Poly3DCollection([triangle], alpha=0.2, facecolor='cyan'))

# Edges
ax.plot(*zip(a,b), color="black")
ax.plot(*zip(b,c), color="black")
ax.plot(*zip(c,a), color="black")

# Labels
ax.text(*a, "a", color="red")
ax.text(*b, "b", color="blue")
ax.text(*c, "c", color="green")

# Axes labels
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("Triangle formed by unit vectors a, b, c")

plt.show()
