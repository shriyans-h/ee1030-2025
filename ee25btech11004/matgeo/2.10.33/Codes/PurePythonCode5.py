import numpy as np
import matplotlib.pyplot as plt

vector = np.zeros(3)
vector[0] = input("Input the first entry")
vector[1] = input("Input the second entry")
vector[2] = input("Input the third entry")

print(np.linalg.norm(vector))