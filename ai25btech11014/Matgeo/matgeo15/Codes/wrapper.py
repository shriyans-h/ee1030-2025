import ctypes

lib = ctypes.CDLL('./libellipse.so')
lib.solve_matrix.argtypes = [ctypes.POINTER(ctypes.c_float)]
lib.solve_matrix.restype = None

V = (ctypes.c_float * 2)()
lib.solve_matrix(V)

print("Ellipse equation: xᵀ V x = 1")
print(f"V = [[{V[0]:.6f}, 0], [0, {V[1]:.6f}]]")
