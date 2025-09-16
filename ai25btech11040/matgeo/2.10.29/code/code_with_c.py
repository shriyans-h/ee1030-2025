import numpy as np
from ctypes import *

a = np.array([2, -2, 0])
b = np.array([1, 1, -1])
c = np.array([3, 0, -1])

lib = CDLL("./code.so")
lib.cross_product_x.argtypes = [c_double] * 6
lib.cross_product_y.argtypes = [c_double] * 6
lib.cross_product_z.argtypes = [c_double] * 6
lib.dot_product.argtypes = [c_double] * 6


lib.cross_product_x.restype = c_double
lib.cross_product_y.restype = c_double
lib.cross_product_z.restype = c_double
lib.dot_product.restype = c_double

b_cross_c = np.array(
    [
        lib.cross_product_x(*b, *c),
        lib.cross_product_y(*b, *c),
        lib.cross_product_z(*b, *c),
    ]
)

volume = abs(
    lib.dot_product(*a, *b_cross_c)
)

print(f"Volume of the parallelopiped is {volume}")