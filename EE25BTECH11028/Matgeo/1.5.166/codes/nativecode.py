import matplotlib.pyplot as plt

# Center C = (3, -1)
# B = (2, 6)
# Let A = (x, y). Midpoint formula: center = (A + B) / 2 =>
# 3 = (x + 2) / 2,  -1 = (y + 6) / 2
# Solve for (x, y):
# x = 2*3 - 2 = 4
# y = 2*(-1) - 6 = -8

A = np.array([4, -8])
B = np.array([2, 6])
C = np.array([3, -1])

# For the circle, radius = distance(center, B)
import numpy as np
def dist(P, Q):
    return np.sqrt((P[0] - Q[0])**2 + (P[1] - Q[1])**2)
radius = dist(C, B)

fig, ax = plt.subplots(figsize=(7,7))

# Plot the circle
circle = plt.Circle(C, radius, color='blue', fill=False, linestyle='dotted', label='Circle')
ax.add_patch(circle)

# Plot A, B, C
ax.scatter(*A, color='red', label='A (unknown, solved)')
ax.scatter(*B, color='green', label='B (2, 6)')
ax.scatter(*C, color='orange', label='Center (3, -1)')

# Draw diameter AB
ax.plot([A[0], B[0]], [A[1], B[1]], color='purple', linewidth=2, linestyle='--', label='Diameter AB')

# Annotate
ax.annotate('A'+str(A), (A[0], A[1]), xytext=(10, -10), textcoords='offset points')
ax.annotate('B'+str(B), (B[0], B[1]), xytext=(-40, 10), textcoords='offset points')
ax.annotate('C'+str(C), (C[0], C[1]), xytext=(5, -10), textcoords='offset points')

ax.set_xlim(C[0] - radius - 2, C[0] + radius + 2)
ax.set_ylim(C[1] - radius - 2, C[1] + radius + 2)
ax.set_aspect('equal')
ax.grid(True)
plt.legend()
plt.title('Circle with Diameter AB')
plt.xlabel('x')
plt.ylabel('y')
plt.show()