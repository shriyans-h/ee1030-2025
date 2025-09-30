import ctypes

# Load shared library
lib = ctypes.CDLL("./libdist.so")

# Define dot function
lib.dot.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
lib.dot.restype = ctypes.c_double

# Define dist function
lib.dist.argtypes = [ctypes.POINTER(ctypes.c_double)]
lib.dist.restype = ctypes.c_double

# Call dist
arr = (ctypes.c_double * 3)(2.0, 3.0, 4.0)
print("distance =", lib.dist(arr))
