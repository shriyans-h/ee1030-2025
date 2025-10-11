import ctypes
import matplotlib.pyplot as plt
import numpy as np

# Load the C library
lib = ctypes.CDLL("./circle_ops.so")

# Define function argument and return types
lib.circle_params.argtypes = [ctypes.c_float, ctypes.c_float,
                              ctypes.POINTER(ctypes.c_float),
                              ctypes.POINTER(ctypes.c_float),
                              ctypes.POINTER(ctypes.c_float)]

lib.compare_pq.argtypes = [ctypes.c_float, ctypes.c_float]
lib.compare_pq.restype = ctypes.c_int

# Ask for simple values of p, q
p = float(input("Enter p: "))
q = float(input("Enter q: "))

# Variables to store results
cx = ctypes.c_float()
cy = ctypes.c_float()
r = ctypes.c_float()

# Call the C function
lib.circle_params(ctypes.c_float(p), ctypes.c_float(q),
                  ctypes.byref(cx), ctypes.byref(cy), ctypes.byref(r))

print(f"Circle center = ({cx.value:.2f}, {cy.value:.2f})")
print(f"Circle radius = {r.value:.2f}")

# Compare p^2 and 8q^2
cmp_result = lib.compare_pq(ctypes.c_float(p), ctypes.c_float(q))
if cmp_result == 0:
    print("p^2 = 8q^2")
elif cmp_result < 0:
    print("p^2 < 8q^2")
else:
    print("p^2 > 8q^2")

# ---------------- PLOTTING ---------------- #
# Circle equation: (x - cx)^2 + (y - cy)^2 = r^2
theta = np.linspace(0, 2*np.pi, 200)
x_circle = cx.value + r.value * np.cos(theta)
y_circle = cy.value + r.value * np.sin(theta)

# Plot circle
plt.plot(x_circle, y_circle, label='Circle', color='blue')

# Mark center and given point (p, q)
plt.scatter(cx.value, cy.value, color='red', label=f'Center ({cx.value:.2f},{cy.value:.2f})')
plt.scatter(p, q, color='green', label=f'Point ({p},{q})')

# X-axis (for chord bisection visualization)
plt.axhline(0, color='black', linestyle='--')

# Setup plot
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Circle x² + y² = px + qy')
plt.legend()
plt.grid(True)
plt.show()
