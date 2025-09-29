import numpy as np
import matplotlib.pyplot as plt

a = np.array([[1200, 500], [900, 250]])
b = np.array([[1/2], [1/3]])
x = np.linalg.solve(a, b)
print("Man can finish the task in ", 1/x[0], " weeks")
print("Woman can finish the task in ", 1/x[1], " weeks")
