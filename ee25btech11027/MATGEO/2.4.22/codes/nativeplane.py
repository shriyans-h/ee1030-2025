import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Points
A = np.array([2, 3, 4])
B = np.array([4, 5, 8])
M = (A + B) / 2

# Plane x + y + z = 10
xx, yy = np.meshgrid(np.linspace(0,6,20), np.linspace(0,8,20))
zz = 10 - xx - yy

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot plane
ax.plot_surface(xx, yy, zz, alpha=0.3, color='cyan')

# Points and line
ax.scatter(*A, color='red', s=60, label='A(2,3,4)')
ax.scatter(*B, color='green', s=60, label='B(4,5,8)')
ax.scatter(*M, color='purple', s=100, marker='*', label='M(3,4,6)')
ax.plot([A[0], B[0]],    # x coordinates
        [A[1], B[1]],    # y coordinates
        [A[2], B[2]],    # z coordinates
        color='blue', linewidth=2, label='Line AB')
ax.text(*A, 'A(2,3,4)', fontsize=9, color='red')
ax.text(*B, 'B(4,5,8)', fontsize=9, color='green')
ax.text(*M, 'M(3,4,6)', fontsize=9, color='purple')

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.legend()
plt.title('Midpoint using C + Python')
plt.savefig("/media/indhiresh-s/New Volume/Matrix/ee1030-2025/ee25btech11027/MATGEO/2.4.22/figs/figure1.png")
plt.show()
