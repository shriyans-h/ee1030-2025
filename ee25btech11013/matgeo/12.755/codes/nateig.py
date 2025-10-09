import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D  # proxy objects for legend

A = np.array([
    [1, -1, 0],
    [1, -1, 1],
    [-1, 0, 1]
])

print("Matrix A:\n", A, "\n" + "-"*30)

eigenvalues, _ = np.linalg.eig(A)
print("Actual Eigenvalues of A:\n", np.real_if_close(eigenvalues))
print("\nNote: 1 is not an eigenvalue of matrix A.")
print("This indicates an error in the problem statement.", "\n" + "-"*30)

lambda_val = 1
B = A - lambda_val * np.identity(A.shape[0])
print(f"Matrix for (A - {lambda_val}I)x = 0:\n", B)
print("\nThe only solution is (0,0,0), so no non-zero eigenvector exists.", "\n" + "-"*30)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
d = np.linspace(-2, 2, 30)

# Plane 1: -y = 0
X1, Z1 = np.meshgrid(d, d); Y1 = np.zeros_like(X1)
ax.plot_surface(X1, Y1, Z1, alpha=0.5, color='r')

# Plane 2: x - 2y + z = 0
X2, Y2 = np.meshgrid(d, d); Z2 = -X2 + 2*Y2
ax.plot_surface(X2, Y2, Z2, alpha=0.5, color='g')

# Plane 3: -x = 0
Y3, Z3 = np.meshgrid(d, d); X3 = np.zeros_like(Y3)
ax.plot_surface(X3, Y3, Z3, alpha=0.5, color='b')

# Intersection point
pt = ax.scatter([0], [0], [0], color='black', s=100)

# Legend using Line2D proxies
legend_elements = [
    Line2D([0],[0], color='r', lw=4, alpha=0.5, label='-y = 0'),
    Line2D([0],[0], color='g', lw=4, alpha=0.5, label='x - 2y + z = 0'),
    Line2D([0],[0], color='b', lw=4, alpha=0.5, label='-x = 0'),
    Line2D([0],[0], marker='o', color='k', label='Intersection (0,0,0)', markersize=8, linestyle='')
]
ax.legend(handles=legend_elements)

ax.set_xlabel('X-axis'); ax.set_ylabel('Y-axis'); ax.set_zlabel('Z-axis')
ax.set_title('Intersection of Planes for (A-I)x = 0')
ax.view_init(elev=20, azim=-65)

plt.savefig("/mnt/c/Users/bharg/Documents/backupmatrix/ee25btech11013/matgeo/12.755/figs/Figure_1.png")
plt.show()
