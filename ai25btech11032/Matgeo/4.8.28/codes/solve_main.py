import ctypes
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------
# Load C shared library
# ---------------------------------------
lib = ctypes.CDLL("./librowreduce.so")
lib.row_reduce.argtypes = (ctypes.c_int, ctypes.c_int,
                           ctypes.POINTER(ctypes.c_double))
lib.row_reduce.restype = None

def row_reduce_numpy(A):
    """Run row_reduce from C on numpy array A (augmented matrix)."""
    rows, cols = A.shape
    A_flat = (ctypes.c_double * (rows*cols))(*A.flatten())
    lib.row_reduce(rows, cols, A_flat)
    return np.array(A_flat).reshape(rows, cols)

# ---------------------------------------
# Problem setup
# ---------------------------------------
n1 = np.array([1,1,1], dtype=float)
b1 = 1.0
n2 = np.array([2,3,-1], dtype=float)
b2 = -4.0
e1 = np.array([1,0,0], dtype=float)

# ---------------------------------------
# Step 1: Line of intersection
# ---------------------------------------
M_line = np.array([[*n1, b1],
                   [*n2, b2]], dtype=float)
R_line = row_reduce_numpy(M_line)

# Particular point rp and direction d
rp = np.array([R_line[0,3], R_line[1,3], 0])   # set z=0 for particular solution
d  = np.array([-R_line[0,2], -R_line[1,2], 1]) # free variable = z

print("Particular point r_p =", rp)
print("Direction d =", d)

# ---------------------------------------
# Step 2: Normal vector
# ---------------------------------------
M_normal = np.array([[*e1, 0],
                     [*d,  0]], dtype=float)
R_normal = row_reduce_numpy(M_normal)

# Extract n: last variable free = 1
n = np.array([-R_normal[0,2], -R_normal[1,2], 1])
c = np.dot(n, rp)

print("Normal vector n =", n)
print("Plane constant c =", c)

# ---------------------------------------
# Step 3: Distance from x-axis
# ---------------------------------------
p = np.array([0.0,0.0,0.0])  # any point on x-axis
dist = abs(np.dot(n,p) - c) / np.linalg.norm(n)
print("Distance from x-axis =", dist)

# ---------------------------------------
# Step 4: Plot figure
# ---------------------------------------
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

# Line of intersection
t_vals = np.linspace(-5, 5, 100)
line_pts = np.array([rp + t*d for t in t_vals])
ax.plot(line_pts[:,0], line_pts[:,1], line_pts[:,2],
        color="red", lw=2, label="Line of intersection")

# Plane surface (n = [0,-1,1] → solve for Y in terms of X,Z)
x_vals = np.linspace(-5, 10, 30)
z_vals = np.linspace(-6, 6, 30)
X, Z = np.meshgrid(x_vals, z_vals)
Y = (c - n[0]*X - n[2]*Z)/n[1]
ax.plot_surface(X, Y, Z, alpha=0.5, color="blue")

# X-axis
ax.plot([-10, 10], [0, 0], [0, 0], 'k-', lw=3, label="X-axis")

# Formatting
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_zlim(-6, 6)
ax.view_init(elev=20, azim=45)  # adjust angle to see parallelism
ax.legend()
plt.savefig("plane.png")
plt.show()

