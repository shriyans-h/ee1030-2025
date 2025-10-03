import ctypes
import numpy as np

# Load shared library
lib = ctypes.CDLL("./libchar.so")

# Define function prototype: void solve(double arr[2][2])
lib.solve.argtypes = [((ctypes.c_double * 2) * 2)]
lib.solve.restype = None

# Prepare 2x2 matrix
arr = np.array([[3.0, 1.0],
                [-1.0, 2.0]], dtype=np.double)

# Convert numpy to ctypes 2D array
c_arr = ((ctypes.c_double * 2) * 2)()
for i in range(2):
    for j in range(2):
        c_arr[i][j] = arr[i][j]

# Call C function
lib.solve(c_arr)

