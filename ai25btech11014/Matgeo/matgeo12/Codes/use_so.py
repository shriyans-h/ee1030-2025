import ctypes
import numpy as np

lib = ctypes.CDLL('./libsystem.so')
lib.solve_system.argtypes = [
    ctypes.POINTER(ctypes.c_float),
    ctypes.POINTER(ctypes.c_float),
    ctypes.POINTER(ctypes.c_float)
]
lib.solve_system.restype = None

A = np.array([
    [2, 3, 10],
    [4, 6, 5],
    [6, 9, 20]
], dtype=np.float32).flatten()

B = np.array([4, 1, 2], dtype=np.float32)
U = np.zeros(3, dtype=np.float32)

lib.solve_system(
    A.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
    B.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
    U.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
)

def check_inconsistency(A, B, U):
    A = A.reshape(3, 3)
    residuals = A @ U - B
    return np.any(np.abs(residuals) > 1e-3)

if check_inconsistency(A, B, U):
    print("System is inconsistent. No exact solution exists.")
else:
    x, y, z = 1/U[0], 1/U[1], 1/U[2]
    print(f"x = {x:.3f}, y = {y:.3f}, z = {z:.3f}")

