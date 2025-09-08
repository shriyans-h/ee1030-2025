import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load compiled C library
lib = ctypes.CDLL('./libvecops.so')   # use "vecops.dll" on Windows

# Argument/return types
lib.cross_product.argtypes = [ctypes.POINTER(ctypes.c_double),
                              ctypes.POINTER(ctypes.c_double),
                              ctypes.POINTER(ctypes.c_double)]
lib.dot_product.argtypes = [ctypes.POINTER(ctypes.c_double),
                            ctypes.POINTER(ctypes.c_double)]
lib.dot_product.restype = ctypes.c_double

# Helper type
DoubleArray3 = ctypes.c_double * 3

# Define vectors
a = np.array([2.0, 1.0, 3.0])
b = np.array([-1.0, 2.0, 1.0])
c = np.array([3.0, 1.0, 2.0])

# Cross product (via C)
cross_res = DoubleArray3()
lib.cross_product(DoubleArray3(*b), DoubleArray3(*c), cross_res)
bx_c = np.array([cross_res[i] for i in range(3)])

# Dot product (via C)
scalar_triple = lib.dot_product(DoubleArray3(*a), cross_res)

print("b x c =", bx_c)
print("a · (b x c) =", scalar_triple)

# ---------- Image Generation ----------
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def draw_vec(v, color, label):
    ax.quiver(0, 0, 0, v[0], v[1], v[2],
              color=color, arrow_length_ratio=0.1, label=label)

draw_vec(a, 'r', 'a')
draw_vec(b, 'g', 'b')
draw_vec(c, 'b', 'c')
draw_vec(bx_c, 'm', 'b × c')

lim = 4
ax.set_xlim([-lim, lim])
ax.set_ylim([-lim, lim])
ax.set_zlim([-lim, lim])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

plt.title(f"Scalar triple product = {scalar_triple}")

# Save the image instead of just showing
plt.savefig("/sdcard/ee1030-2025/ai25btech11032/Matgeo/2.7.4/figs/triple_product.png", dpi=300)
plt.show()
