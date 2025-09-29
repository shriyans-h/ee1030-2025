import numpy as np
import ctypes


lib_path = "./libcode.so" 
c_lib = ctypes.CDLL(lib_path)
c_lib.mat_vec_mult.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double)
]
c_lib.mat_vec_mult.restype = None

a = np.array([[1200, 500], [900, 250]], dtype=np.float64)
b = np.array([[1/2], [1/3]], dtype=np.float64)

x = np.linalg.solve(a, b)
result_from_c = np.zeros_like(b)
a_ptr = a.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
x_ptr = x.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
result_ptr = result_from_c.ctypes.data_as(ctypes.POINTER(ctypes.c_double))

c_lib.mat_vec_mult(a_ptr, x_ptr, result_ptr)

print("Numpy result:")
print(1/x[0])
print(1/x[1])
print("\nResult of A*x from C code (for verification):")
print(result_from_c[0])
print(result_from_c[1])
if np.allclose(result_from_c, b):
    print("\nVerification successful: The C result matches 'b'.")

