import ctypes
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the shared library
matfun = ctypes.CDLL('./matfun.so')

# Define argument and return types
matfun.vector_subtract.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.float64),
    np.ctypeslib.ndpointer(dtype=np.float64),
    np.ctypeslib.ndpointer(dtype=np.float64),
    ctypes.c_int
]
matfun.dot_product.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.float64),
    np.ctypeslib.ndpointer(dtype=np.float64),
    ctypes.c_int
]
matfun.dot_product.restype = ctypes.c_double
matfun.scalar_multiply.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.float64),
    np.ctypeslib.ndpointer(dtype=np.float64),
    ctypes.c_double,
    ctypes.c_int
]

# Define points A and B
A = np.array([1.0, 2.0, 3.0])
B = np.array([3.0, 2.0, -1.0])

BA = np.zeros(3)
rhs = 0.0

# Compute B - A using shared lib
matfun.vector_subtract(B, A, BA, 3)

# Compute dot products B.B and A.A using shared lib
rhs = matfun.dot_product(B, B, 3) - matfun.dot_product(A, A, 3)

# Calculate 2*(B - A)
BA2 = np.zeros(3)
matfun.scalar_multiply(BA, BA2, 2, 3)

print(f"Vector 2(B - A): {BA2}")
print(f"RHS (B.B - A.A): {rhs}")

# Create grid for b and c
b_vals = np.linspace(-10, 10, 100)
c_vals = np.linspace(-10, 10, 100)
b_grid, c_grid = np.meshgrid(b_vals, c_vals)

# From plane equation 2(B - A)^T X = rhs
# Which is BA2^T * X = rhs
# BA2 = [4, 0, -8], so the equation is 4a - 8c = rhs = 0
# => a = 2c

# Calculate corresponding a using a = 2c
a_grid = 2 * c_grid

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the plane surface
ax.plot_surface(a_grid, b_grid, c_grid, alpha=0.5, color='cyan', edgecolor='k')

ax.set_xlabel('a')
ax.set_ylabel('b')
ax.set_zlabel('c')
ax.set_title('3D Plot of plane: a - 2c = 0 (from shared library)')

plt.show()
