import ctypes
import pandas as pd
import matplotlib.pyplot as plt

# Load the shared library
lib = ctypes.CDLL("./libparallelogram.so")
lib.dx_from_abc.argtypes = [ctypes.c_double]*6
lib.dx_from_abc.restype = ctypes.c_double
lib.dy_from_abc.argtypes = [ctypes.c_double]*6
lib.dy_from_abc.restype = ctypes.c_double

# Given points
ax, ay = 1.0, 3.0
bx, by = -1.0, 2.0
cx, cy = 2.0, 5.0

dx = lib.dx_from_abc(ax, ay, bx, by, cx, cy)
dy = lib.dy_from_abc(ax, ay, bx, by, cx, cy)

print("From Python via .so:")
print("D =", dx, dy)

# Read the points written by C main
df = pd.read_csv("points.dat", sep=r"\s+", header=None, names=["label","x","y"])

# Plot
order = ["A","B","C","D","A"]
xs = [df.loc[df["label"]==lbl,"x"].values[0] for lbl in order]
ys = [df.loc[df["label"]==lbl,"y"].values[0] for lbl in order]

plt.plot(xs, ys, marker="o")
for lbl in ["A","B","C","D"]:
    x = df.loc[df["label"]==lbl,"x"].values[0]
    y = df.loc[df["label"]==lbl,"y"].values[0]
    plt.text(x, y, f"{lbl}({x:.0f},{y:.0f})")

plt.title("Parallelogram ABCD")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.savefig("/home/r-nikhil/ee1030-2025/ai25btech11025/matgeo/1.3.4/figs/plotc.png")
plt.show()
