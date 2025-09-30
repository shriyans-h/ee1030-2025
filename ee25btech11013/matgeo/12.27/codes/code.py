import numpy as np
import matplotlib.pyplot as plt
import ctypes


lib = ctypes.CDLL("./libcode.so")

lib.solve_2x2.argtypes = [ctypes.POINTER(ctypes.c_double),
                          ctypes.POINTER(ctypes.c_double),
                          ctypes.POINTER(ctypes.c_double)]
lib.solve_2x2.restype = ctypes.c_int


A = np.array([[1200, 500],
              [900, 250]], dtype=np.float64)
b = np.array([0.5, 1/3], dtype=np.float64)


x = np.zeros(2, dtype=np.float64)

status = lib.solve_2x2(A.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                       b.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                       x.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))

if status == 0:
    u, v = x
    man_weeks, woman_weeks = 1/u, 1/v
    men_required = round(man_weeks)

    print(f"One man finishes in {man_weeks:.0f} weeks")
    print(f"One woman finishes in {woman_weeks:.0f} weeks")
    print(f"Men required in 1 week: {men_required}")

    u_vals = np.linspace(0, u*2, 400)
    v1 = (0.5 - 1200*u_vals) / 500
    v2 = ((1/3) - 900*u_vals) / 250

    plt.plot(u_vals, v1, label='1200u + 500v = 1/2')
    plt.plot(u_vals, v2, label='900u + 250v = 1/3')

    plt.plot(u, v, 'ro', label=f'({u:.6f}, {v:.6f})')
    plt.annotate(f'({u:.6f}, {v:.6f})', xy=(u, v), xytext=(u*1.1, v*1.1))
    plt.legend(); plt.grid(True)
    plt.xlabel("u = 1/x"); plt.ylabel("v = 1/y")

    plt.title("Bridge Work Problem")

    plt.savefig("/mnt/c/Users/bharg/Documents/backupmatrix/ee25btech11013/matgeo/12.27/figs/Figure_1.png")
    plt.show()

else:
    print("No unique solution.")

