import numpy as np
import matplotlib.pyplot as plt

# -----------------------
# Gauss-Jordan row reduction with partial pivoting (returns RREF)
# A is a numpy array (rows x cols), operates on a copy
# -----------------------
def row_reduce(A_in, eps=1e-12):
    A = A_in.astype(float).copy()
    rows, cols = A.shape
    r = 0
    for c in range(cols - 1):  # last column is RHS
        if r >= rows:
            break
        # partial pivot: find row with max abs in column c at or below r
        pivot = r
        maxv = abs(A[pivot, c])
        for i in range(r+1, rows):
            v = abs(A[i, c])
            if v > maxv:
                maxv = v
                pivot = i
        if maxv < eps:
            # no pivot in this column
            continue
        # swap if needed
        if pivot != r:
            A[[r, pivot], :] = A[[pivot, r], :]
        # normalize pivot row
        div = A[r, c]
        A[r, c:] = A[r, c:] / div
        # eliminate in all other rows
        for i in range(rows):
            if i == r:
                continue
            factor = A[i, c]
            if abs(factor) > eps:
                A[i, c:] = A[i, c:] - factor * A[r, c:]
        r += 1
    # zero-out tiny values for neatness
    A[np.abs(A) < 1e-12] = 0.0
    return A

# -----------------------
# Problem data
# -----------------------
n1 = np.array([1.0, 1.0, 1.0])
b1 = 1.0
n2 = np.array([2.0, 3.0, -1.0])
b2 = -4.0
e1 = np.array([1.0, 0.0, 0.0])  # x-axis direction

# -----------------------
# Step 1: line of intersection [A|b]
# -----------------------
M_line = np.vstack([np.hstack([n1, b1]), np.hstack([n2, b2])])
R_line = row_reduce(M_line)
print("RREF (line system):\n", R_line)

# Interpret RREF: assume last variable (z) free -> set z = t
# Row form: row0: x + a z = r0  => x = r0 - a t
#           row1: y + b z = r1  => y = r1 - b t
rp = np.array([R_line[0,3], R_line[1,3], 0.0])      # t=0
d  = np.array([-R_line[0,2], -R_line[1,2], 1.0])   # coefficients of t
print("\nParticular point r_p =", rp)
print("Direction d =", d)

# -----------------------
# Step 2: plane normal: solve [e1^T; d^T] n = 0
# -----------------------
M_norm = np.vstack([np.hstack([e1, 0.0]), np.hstack([d, 0.0])])
R_norm = row_reduce(M_norm)
print("\nRREF (normal system):\n", R_norm)

# choose last variable free = 1 -> n = [-R[0,2], -R[1,2], 1]
n = np.array([-R_norm[0,2], -R_norm[1,2], 1.0])
# scale normal to an integer-like/clean vector for nicer printing (optional)
# avoid scaling if zero
if np.linalg.norm(n) > 1e-12:
    # scale to make components integers if possible (here we know integers)
    # but we won't force scale; keep as computed
    pass

c = float(np.dot(n, rp))
print("\nNormal n =", n)
print("Plane constant c =", c)

# -----------------------
# Step 3: distance from x-axis
# Choose a convenient point on x-axis p0 = (0,0,0)
# distance = | n·p0 - c | / ||n|| = | -c | / ||n||
# Also compute the perpendicular foot point from p0 onto plane:
# foot = p0 + ((c - n·p0)/||n||^2) * n
# -----------------------
p0 = np.array([0.0, 0.0, 0.0])
n_norm = np.linalg.norm(n)
if n_norm < 1e-12:
    dist = float('nan')
    foot = None
else:
    dist = abs(np.dot(n, p0) - c) / n_norm
    foot = p0 + ((c - np.dot(n, p0)) / (n_norm**2)) * n

print("\nDistance from x-axis =", dist)
print("Perpendicular foot on plane from origin (x-axis point) =", foot)

# -----------------------
# Step 4: Plot everything clearly showing plane parallel to x-axis
# -----------------------
fig = plt.figure(figsize=(9,7))
ax = fig.add_subplot(111, projection='3d')

# plot line of intersection (parametric)
t_vals = np.linspace(-6, 6, 201)
line_pts = np.array([rp + t*d for t in t_vals])
ax.plot(line_pts[:,0], line_pts[:,1], line_pts[:,2], color='red', lw=2, label='Intersection line')

# Create plane grid such that plane visibly looks parallel to x-axis:
# Because plane has no x-component in normal (n[0] == 0) for this problem,
# plane equation is -y + z = c  => y = z - c (or adjust signs) .
# In general solve for the variable with a non-zero normal coefficient.
# We'll solve for Y (index 1) unless n[1] ~ 0; choose fallback if needed.
if abs(n[1]) > 1e-9:
    # make grid in X and Z (X free direction shows parallelism)
    x_vals = np.linspace(-10, 10, 40)
    z_vals = np.linspace(-8, 8, 40)
    X, Z = np.meshgrid(x_vals, z_vals)
    Y = (c - n[0]*X - n[2]*Z) / n[1]
    ax.plot_surface(X, Y, Z, alpha=0.35, color='cyan', rstride=2, cstride=2, linewidth=0)
else:
    # if n[1] ~ 0, solve for X instead (rare)
    y_vals = np.linspace(-10, 10, 40)
    z_vals = np.linspace(-8, 8, 40)
    Y, Z = np.meshgrid(y_vals, z_vals)
    X = (c - n[1]*Y - n[2]*Z) / n[0]
    ax.plot_surface(X, Y, Z, alpha=0.35, color='cyan', rstride=2, cstride=2, linewidth=0)

# plot x-axis bold
ax.plot([-12, 12], [0,0], [0,0], color='k', lw=3, label='X-axis')

# mark particular point rp and foot
ax.scatter([rp[0]],[rp[1]],[rp[2]], color='blue', s=60, label='r_p')
if foot is not None:
    ax.scatter([foot[0]],[foot[1]],[foot[2]], color='green', s=60, label='foot on plane')
    # draw perpendicular segment from p0 on x-axis to foot
    ax.plot([p0[0], foot[0]], [p0[1], foot[1]], [p0[2], foot[2]],
            color='magenta', lw=2, linestyle='--', label=f'perp distance = {dist:.3f}')

# labels and view — choose view that shows parallelism (look along x to show plane side)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim(-12, 12)
ax.set_ylim(-12, 12)
ax.set_zlim(-8, 8)

# set viewing angle so x-axis appears lateral to plane: azim ~ 90 looks down +x direction
ax.view_init(elev=18, azim=90)
ax.legend()
ax.set_title("Plane through intersection — parallel to X-axis\n(blue plane, red line, black x-axis)")
plt.tight_layout()
plt.savefig("new_plane.png")
plt.show()

