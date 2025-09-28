import ctypes
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mp


# Load the shared C library

lib = ctypes.CDLL("./5.2.44.so")

# Define argument and return types
lib.rref_solver.argtypes = [ctypes.c_double * 6, ctypes.c_double * 2]

# Create augmented matrix for system:
aug = (ctypes.c_double * 6)(1, 1, 5,   1, -1, 1)  # Flattened 2x3
solution = (ctypes.c_double * 2)()

# Call C function
lib.rref_solver(aug, solution)

# Convert result to numpy vector (ensure flat)
x_sol = np.array([solution[0], solution[1]], dtype=float).flatten()
print("Solution vector from C:", x_sol) # This correctly prints [3. 2.]

# plot
x_vals = np.linspace(-2, 10, 400)
y1 = 5 - x_vals         # Correct for x + y = 5
y2 = x_vals - 1         # CORRECTED for x - y = 1

plt.plot(x_vals, y1, label=r"$x+y=5$")
plt.plot(x_vals, y2, label=r"$x-y=1$")

plt.scatter(x_sol[0], x_sol[1], color="red", zorder=5)
plt.text(float(x_sol[0])+0.2, float(x_sol[1]), f"({x_sol[0]:.1f}, {x_sol[1]:.1f})", color="red")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Graphical Solution of the Linear System")
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.legend()
plt.grid(True)
plt.savefig("Figure_1_Corrected.png")
plt.show()
