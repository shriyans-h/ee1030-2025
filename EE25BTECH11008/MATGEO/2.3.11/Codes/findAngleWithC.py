import ctypes
import numpy

# Load the shared library
lib = ctypes.CDLL("./computations.so")

# Define function signatures
lib.gram_matrix.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.c_int,
    ctypes.POINTER((ctypes.c_double * 2) * 2)
]

lib.normalize_gram.argtypes = [
    ctypes.POINTER((ctypes.c_double * 2) * 2),
    ctypes.POINTER((ctypes.c_double * 2) * 2)
]

lib.angle_from_normalized.argtypes = [
    ctypes.POINTER((ctypes.c_double * 2) * 2)
]
lib.angle_from_normalized.restype = ctypes.c_double

# Python wrapper
def compute_angle(u, v):
    n = len(u)
    u_arr = (ctypes.c_double * n)(*u)
    v_arr = (ctypes.c_double * n)(*v)

    G = ((ctypes.c_double * 2) * 2)()
    G_norm = ((ctypes.c_double * 2) * 2)()

    lib.gram_matrix(u_arr, v_arr, n, G)
    lib.normalize_gram(G, G_norm)
    theta = lib.angle_from_normalized(G_norm)
    return theta

# Main
u = [1, -2, -2]
v = [3, -6, 2]
theta = compute_angle(u, v)

print(f"Angle (radians): {theta}")
print(f"Angle (degrees): {theta * 180 / numpy.pi}")
