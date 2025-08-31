import numpy as np
import ctypes
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load C library
libmid = ctypes.CDLL('./plane.so')

# Define arrays (float32)
A = np.array([2.0, 3.0, 4.0], dtype=np.float32)
B = np.array([4.0, 5.0, 8.0], dtype=np.float32)
M = np.zeros(3, dtype=np.float32)

# Set argtypes/restype for C function
libmid.midpoint.argtypes = [ctypes.POINTER(ctypes.c_float),
                            ctypes.POINTER(ctypes.c_float),
                            ctypes.POINTER(ctypes.c_float)]
libmid.midpoint.restype = None

# Call C function to compute midpoint
libmid.midpoint(M.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
                A.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
                B.ctypes.data_as(ctypes.POINTER(ctypes.c_float)))

print("Midpoint:", M)

# Prepare plane x + y + z = 10
xx, yy = np.meshgrid(np.linspace(0, 6, 20), np.linspace(0, 8, 20))
zz = 10 - xx - yy

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plane
ax.plot_surface(xx, yy, zz, alpha=0.3, color='cyan')

# Points and line
ax.scatter(*A, color='red', s=60, label='A(2,3,4)')
ax.scatter(*B, color='green', s=60, label='B(4,5,8)')
ax.scatter(*M, color='purple', s=100, marker='*', label='M(3,4,6)')
ax.plot([A[0], B[0]],    # x coordinates
        [A[1], B[1]],    # y coordinates
        [A[2], B[2]],    # z coordinates
        color='blue', linewidth=2, label='Line AB')
ax.text(*A, 'A(2,3,4)', fontsize=9, color='red')
ax.text(*B, 'B(4,5,8)', fontsize=9, color='green')
ax.text(*M, 'M(3,4,6)', fontsize=9, color='purple')

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.legend()
plt.title('Midpoint using C + Python')
plt.savefig("/media/indhiresh-s/New Volume/Matrix/ee1030-2025/ee25btech11027/MATGEO/2.4.22/figs/figure1.png")
plt.show()
