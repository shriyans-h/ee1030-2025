import numpy as np
import matplotlib.pyplot as plt

# --- Define a slanted parallelogram ABCD
A = np.array([0.0, 0.0])
B = np.array([4.0, 0.0])
D = np.array([1.5, 3.0])      # slanted
C = B + D - A                 # ensures ABCD is a parallelogram

k = 4.0 / 3.0  # scale factor for BD'C' ~ BDC

# --- Compute D' and C' by homothety about B
Dp = B + k * (D - B)   # D' = B + k*(D - B)
Cp = B + k * (C - B)   # C' = B + k*(C - B)

# --- Build A' so that A'BC'D' is parallelogram
Ap = B + Dp - Cp

# --- Plotting
plt.figure(figsize=(8,6))

# original ABCD (parallelogram)
poly_ABCD = np.vstack([A,B,C,D,A])
plt.plot(poly_ABCD[:,0], poly_ABCD[:,1], 'b-', linewidth=2, label="ABCD (original parallelogram)")

# scaled triangle B-D'-C'
plt.plot([B[0], Dp[0], Cp[0], B[0]], [B[1], Dp[1], Cp[1], B[1]],
         'r--', linewidth=1.5, label="Δ B D' C'")

# parallelogram A'-B-C'-D'
poly_par = np.vstack([Ap, B, Cp, Dp, Ap])
plt.plot(poly_par[:,0], poly_par[:,1], 'g-o', linewidth=2, label="A' B C' D' (parallelogram)")

# plot points and annotate (only names, no coordinates)
pts = {"A":A,"B":B,"C":C,"D":D,"D'":Dp,"C'":Cp,"A'":Ap}
for name,p in pts.items():
    plt.scatter(p[0], p[1], s=60, zorder=5)
    plt.text(p[0]+0.08, p[1]+0.08, f"{name}", fontsize=10, fontweight="bold")

plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.legend()
plt.title("Parallelograms ABCD and A' B C' D' with scaled triangle BD'C'")
plt.tight_layout()

# --- Save the figure ---
plt.savefig("parallelogram_with_scaling.png", dpi=300)

plt.show()


