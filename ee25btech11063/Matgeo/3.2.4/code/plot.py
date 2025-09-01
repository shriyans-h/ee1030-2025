import numpy as np
import matplotlib.pyplot as plt

# --- set up a non-rectangular parallelogram ABCD (so the plot won't look square)
A = np.array([0.0, 0.0])
B = np.array([4.0, 0.0])
D = np.array([1.0, 3.0])   # note: not (0,3) — this slants the shape
C = B + D - A              # ensures ABCD is a parallelogram

k = 4.0 / 3.0              # scale factor for triangle BD'C' similar to BDC

# scaled triangle BD'C'
Dp = B + k * (D - B)
Cp = B + k * (C - B)

# Solve for t where A' = B + t*(A - B) and (A' - D') is parallel to (A - D)
v = A - D   # vector DA (we use A - D so later we test parallelism with A' - D')
numerator   = (B[1] - Dp[1]) * v[0] - (B[0] - Dp[0]) * v[1]
denominator = (A[0] - B[0]) * v[1] - (A[1] - B[1]) * v[0]
if abs(denominator) < 1e-12:
    raise RuntimeError("Degenerate configuration: can't compute A' (denominator ~ 0).")
t = numerator / denominator
Ap = B + t * (A - B)

# small helper for 2D cross product (scalar)
def cross2(u, v):
    return u[0]*v[1] - u[1]*v[0]

# Check parallelogram: opposite sides parallel
vec_ApB  = B - Ap
vec_DpCp = Cp - Dp
vec_ApDp = Dp - Ap
vec_BCp  = Cp - B

cond1 = abs(cross2(vec_ApB, vec_DpCp)) < 1e-8
cond2 = abs(cross2(vec_ApDp, vec_BCp)) < 1e-8
is_parallelogram = cond1 and cond2

print("Points:")
for name, p in [("A",A),("B",B),("C",C),("D",D),("D'",Dp),("C'",Cp),("A'",Ap)]:
    print(f"{name:3} = ({p[0]:.6f}, {p[1]:.6f})")
print("\nChecks:")
print(" A'B ∥ D'C' :", cond1)
print(" A'D' ∥ B C' :", cond2)
print("=> A'BC'D' is parallelogram?:", is_parallelogram)

# --- Plotting ---
plt.figure(figsize=(9,6))

# helper to plot and close polygons
def plot_poly(pts, style, label, z=1, lw=1.5):
    pts_closed = np.vstack([pts, pts[0]])
    plt.plot(pts_closed[:,0], pts_closed[:,1], style, label=label, linewidth=lw, zorder=z)

# triangles and parallelogram
plot_poly(np.array([B, D, C]),      '-o', "Δ B D C",       z=2, lw=1.5)
plot_poly(np.array([B, Dp, Cp]),    '--s', "Δ B D' C'",    z=2, lw=1.5)
plot_poly(np.array([Ap, B, Cp, Dp]), '-o', "Parallelogram A' B C' D'", z=3, lw=2)

# label points with offsets
pts = {"A":A,"B":B,"C":C,"D":D,"D'":Dp,"C'":Cp,"A'":Ap}
for name, p in pts.items():
    plt.scatter(p[0], p[1], s=60, zorder=5)
    plt.text(p[0] + 0.15, p[1] + 0.15, name, fontsize=10)

# set axis limits with margins so shape is clear
all_pts = np.vstack(list(pts.values()))
xmin, ymin = all_pts.min(axis=0) - 1.0
xmax, ymax = all_pts.max(axis=0) + 1.0
plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)

plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.legend()
plt.title("Triangles BDC (solid), BD'C' (dashed) and Parallelogram A'BC'D'")
plt.tight_layout()

# save and show
plt.savefig("parallelogram_plot.png", dpi=200)
plt.show()

