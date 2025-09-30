import numpy as np
import matplotlib.pyplot as plt

A = np.array([[1200, 500],
              [900, 250]], dtype=float)

b = np.array([0.5, 1/3], dtype=float)

u, v = np.linalg.solve(A, b)

man_weeks = 1 / u
woman_weeks = 1 / v
men_required = round(man_weeks)

print(f"One man finishes in {man_weeks:.0f} weeks")
print(f"One woman finishes in {woman_weeks:.0f} weeks")
print(f"Men required in 1 week: {men_required}")


u_vals = np.linspace(0, u*2, 400)
v1 = (0.5 - 1200*u_vals) / 500
v2 = ((1/3) - 900*u_vals) / 250

plt.figure(figsize=(7,6))
plt.plot(u_vals, v1, label='1200u + 500v = 1/2')
plt.plot(u_vals, v2, label='900u + 250v = 1/3')


plt.plot(u, v, 'ro', markersize=8, label=f'Solution ({u:.6f}, {v:.6f})')
plt.annotate(f'({u:.6f}, {v:.6f})', xy=(u, v), xytext=(u*1.1, v*1.1))

plt.xlabel("u = 1/x")
plt.ylabel("v = 1/y")
plt.title("Bridge Work Problem")
plt.legend()
plt.grid(True)
plt.savefig("/mnt/c/Users/bharg/Documents/backupmatrix/ee25btech11013/matgeo/12.27/figs/Figure_1.png")
plt.show()


