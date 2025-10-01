import ctypes
import numpy as np

lib = ctypes.CDLL("./libcode.so")

lib.determinant.argtypes = [np.ctypeslib.ndpointer(dtype=np.int32, shape=(3,3))]
lib.determinant.restype = ctypes.c_int

A = np.array([[1, -1, 2],
              [2,  1, 4],
              [1,  3, 1]], dtype=np.int32)

det = lib.determinant(A)

if det != 0:
    print("Unique solution exists and consistent system of equations")
else:
    print("Inconsistent system of equations")