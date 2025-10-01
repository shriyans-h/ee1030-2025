import ctypes

lib = ctypes.CDLL('./libksolver.so')
lib.solve_k.restype = ctypes.c_double
lib.solve_k.argtypes = [ctypes.c_double] * 6

A_x, A_y, B_y = 2.0, 1.0, 8.0
m, n, rhs = 1.0, 3.0, -1.0

k = lib.solve_k(A_x, A_y, B_y, m, n, rhs)
print(k)
