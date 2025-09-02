import numpy as np
import ctypes

p = np.array([[7], [-6]])
q = np.array([[3], [4]])

lib = ctypes.CDLL('./code.so')
lib.point_x.argtypes = [ctypes.c_double] * 4
lib.point_y.argtypes = [ctypes.c_double] * 4

lib.point_x.restype = ctypes.c_double
lib.point_y.restype = ctypes.c_double

x = lib.point_x(p[0][0], q[0][0], 1, 2)
y = lib.point_y(p[1][0], q[1][0], 1, 2)

r = np.array([[x], [y]])

points = [p, q, r]
x = [a[0] for a in points]
y = [a[1] for a in points]

if (r[0][0] > 0 and r[1][0] > 0):
    print("Q1")
if (r[0][0] > 0 and r[1][0] < 0):
    print("Q4")
if (r[0][0] < 0 and r[1][0] > 0):
    print("Q2")
if (r[0][0] < 0 and r[1][0] < 0):
    print("Q3")