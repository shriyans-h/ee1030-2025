import ctypes

# Load the shared library
lib = ctypes.CDLL('./libverify.so')

# Define argument types
lib.verify_condition.argtypes = [
    ctypes.c_float, ctypes.c_float, ctypes.c_float,
    ctypes.POINTER(ctypes.c_float)
]
lib.verify_condition.restype = None

# Inputs (H.P. values)
a = ctypes.c_float(1.0)
b = ctypes.c_float(2.0)
c = ctypes.c_float(0.5)
result = ctypes.c_float()

# Call the C function
lib.verify_condition(a, b, c, ctypes.byref(result))

# Output
if result.value == 1.0:
    print("Verified: ab + bc = 2ac")
else:
    print("Condition fails")
