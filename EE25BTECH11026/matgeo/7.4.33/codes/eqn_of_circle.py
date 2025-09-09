import ctypes
import numpy as np
import math as m
import matplotlib.pyplot as plt

# load shared library
lib = ctypes.CDLL("./libcircle_solver.so")

# prepare result array (14 doubles: O,D,E,F,P,Q,R)
results = (ctypes.c_double * 14)()
lib.solve_geometry(results)

# unpack into numpy
vals = np.array(results)
O = vals[0:2]
D = vals[2:4]
E = vals[4:6]
F = vals[6:8]
P = vals[8:10]
Q = vals[10:12]
R = vals[12:14]

h,k,r=  O[0],O[1],1
print("Equation of circle:")
print(f"(x-{h:.2f})^2+(y-{k:.2f})^2={r}")
# --- Plot same as Python code ---
r = 1.0
theta = np.linspace(0, 2*np.pi, 400)
xc = O[0] + r*np.cos(theta)
yc = O[1] + r*np.sin(theta)

plt.figure(figsize=(7,7))
plt.plot(xc, yc, 'b-', label="Incircle (r=1)")
plt.plot([P[0],Q[0],R[0],P[0]], [P[1],Q[1],R[1],P[1]], 'm--', label="Equilateral Triangle")

plt.scatter([D[0],E[0],F[0]], [D[1],E[1],F[1]], c=['red','orange','purple'], label="Tangency D,E,F")
plt.scatter(O[0], O[1], c='black', s=40, label="Center O")
plt.scatter([P[0],Q[0],R[0]], [P[1],Q[1],R[1]], c='blue', s=30, label="Vertices P,Q,R")

plt.gca().set_aspect("equal")
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.title("Equilateral triangle PQR with incircle C (C computed in C)")
plt.show()

