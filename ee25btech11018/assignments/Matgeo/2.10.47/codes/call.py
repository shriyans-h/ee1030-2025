
import ctypes
import numpy as np

lib = ctypes.CDLL('./volume.so')

lib.volume.argtypes = [ctypes.c_double]
lib.volume.restype = ctypes.c_double

a_values = np.array([-3, 3, 1.0 / np.sqrt(3), np.sqrt(3)])

min_volume = float('inf')
min_a = None

for a in a_values:
    vol = lib.volume(a)
    if vol < min_volume:
        min_volume = vol
        min_a = a

print(f"The value of a for which the volume is minimum: {min_a:.6f}")
