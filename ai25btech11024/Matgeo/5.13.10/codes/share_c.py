import ctypes

# Load the shared library
lib = ctypes.CDLL('./libsoln.so')

# Define the function prototype
lib.find.argtypes = [ctypes.c_double] * 9
lib.find.restype = ctypes.c_double

# Example values
a00, a02, a10, a11, a12, a20, a21, a22, A = 1, 3, 1, 3, 3, 2, 4, 4, 4

# Call the function
result = lib.find(a00, a02, a10, a11, a12, a20, a21, a22, A)

print("Result:", result)

