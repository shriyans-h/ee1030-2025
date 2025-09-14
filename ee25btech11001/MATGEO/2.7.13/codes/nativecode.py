import ctypes
import numpy as np
import matplotlib.pyplot as plt

lib = ctypes.CDLL("./code.so")
lib.area_of_quadrilateral.argtypes = [ctypes.c_double, ctypes.c_double,
                                      ctypes.c_double, ctypes.c_double,
                                      ctypes.c_double, ctypes.c_double,
                                      ctypes.c_double, ctypes.c_double]
lib.area_of_quadrilateral.restype = ctypes.c_double

x1, y1 = -4, -5
x2, y2 = -1, -6
x3, y3 = -5, 7
x4, y4 = 4, 5

area = lib.area_of_quadrilateral(x1, y1, x2, y2, x3, y3, x4, y4)
print("Area:", area)

xs = [x1, x2, x4, x3, x1]
ys = [y1, y2, y4, y3, y1]

plt.fill(xs, ys, alpha=0.3, edgecolor='black')
plt.scatter([x1, x2, x3, x4], [y1, y2, y3, y4], color='red')

points = {"A": (x1, y1), "B": (x2, y2), "C": (x3, y3), "D": (x4, y4)}
for p, (x, y) in points.items():
    plt.text(x, y, f"{p}{(x,y)}")

plt.title(f"Quadrilateral ABCD, Area={area}")
plt.show()
