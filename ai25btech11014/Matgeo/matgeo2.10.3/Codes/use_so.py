import ctypes
import numpy as np

lib = ctypes.CDLL('./libnormal.so')
lib.normal_vector.argtypes = [ctypes.POINTER(ctypes.c_float),
                              ctypes.POINTER(ctypes.c_float),
                              ctypes.POINTER(ctypes.c_float)]

P = np.array([1, -1, 2], np.float32)
Q = np.array([2, 0, -1], np.float32)
R = np.array([0, 2, 1], np.float32)

PQ = Q - P
PR = R - P
out = np.zeros(3, np.float32)

lib.normal_vector(PQ.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
                  PR.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
                  out.ctypes.data_as(ctypes.POINTER(ctypes.c_float)))

print("Unit vector:", out)
