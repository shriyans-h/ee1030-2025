import ctypes
import sys
import matplotlib.pyplot as plt

# Load the compiled shared library
lib = ctypes.CDLL("./libslope.so")

# Define the argument and return types for the C function
lib.perpendicularSlope.argtypes = [ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float]
lib.perpendicularSlope.restype = ctypes.c_float

# Input points
x1, y1 = 3.0, 6.0
x2, y2 = -3.0, 4.0

# Call the C function
perp_slope = lib.perpendicularSlope(x1, y1, x2, y2)

# Print the perpendicular slope
if perp_slope == 9999999.0:
    print("The perpendicular line is vertical (slope undefined).")
else:
    print(f"The slope of the perpendicular line is: {perp_slope:.2f}")

# Plot the original line connecting (x1, y1) and (x2, y2)
plt.figure(figsize=(6, 6))
plt.plot([x1, x2], [y1, y2], 'b-o', label='Line Joining Points')

# Highlight the two points
plt.scatter([x1, x2], [y1, y2], color='red')
plt.text(x1, y1, f"({x1}, {y1})", fontsize=10, ha='right')
plt.text(x2, y2, f"({x2}, {y2})", fontsize=10, ha='right')
# Midpoint
mid_x = (x1 + x2) / 2.0
mid_y = (y1 + y2) / 2.0
plt.scatter(mid_x, mid_y, color='green', label='Midpoint')
plt.text(mid_x, mid_y, f"({mid_x:.1f}, {mid_y:.1f})", fontsize=10, ha='left')

# Add labels and grid
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Line Joining Two Points")
plt.grid(True)
plt.legend()
plt.axis('equal')

# Show the plot
plt.savefig("fig1.png")
plt.show()
