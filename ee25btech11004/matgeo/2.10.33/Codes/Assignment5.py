import numpy as np
import ctypes

c_lib=ctypes.CDLL('./5c.so')

c_lib.norm.argtypes = [ctypes.c_float, ctypes.c_float, ctypes.c_float]
c_lib.norm.restype = ctypes.c_float

vector = np.zeros(3)
vector[0] = input("Input the first entry")
vector[1] = input("Input the second entry")
vector[2] = input("Input the third entry")

answer = c_lib.norm(
    ctypes.c_float(vector[0]),
    ctypes.c_float(vector[1]), 
    ctypes.c_float(vector[2]),
)

print(answer)