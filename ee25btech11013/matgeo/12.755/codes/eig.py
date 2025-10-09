import numpy as np, ctypes, matplotlib.pyplot as plt
from matplotlib.lines import Line2D

lib = ctypes.CDLL("./libeig.so")
lib.process_matrix.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.double, ndim=2, flags="C_CONTIGUOUS"),
    np.ctypeslib.ndpointer(dtype=np.double, ndim=2, flags="C_CONTIGUOUS"),
    ctypes.c_double
]; lib.process_matrix.restype = None

A = np.array([[1,-1,0],[1,-1,1],[-1,0,1]],dtype=np.double)
B = np.zeros((3,3),dtype=np.double)
lib.process_matrix(A,B,1.0)

print("\nEigenvalues of A:", np.real_if_close(np.linalg.eigvals(A)))

fig = plt.figure(); ax = fig.add_subplot(111, projection='3d')
d = np.linspace(-2,2,30)
ax.plot_surface(*np.meshgrid(d,d), 0*np.meshgrid(d,d)[0], alpha=0.5,color='r')
ax.plot_surface(*np.meshgrid(d,d), -np.meshgrid(d,d)[0]+2*np.meshgrid(d,d)[1], alpha=0.5,color='g')
ax.plot_surface(0*np.meshgrid(d,d)[0], *np.meshgrid(d,d), alpha=0.5,color='b')
ax.scatter(0,0,0,color='k',s=50)

# Legend using Line2D proxies
ax.legend(handles=[Line2D([0],[0], color='r', lw=4, alpha=0.5, label='-y=0'),
                   Line2D([0],[0], color='g', lw=4, alpha=0.5, label='x-2y+z=0'),
                   Line2D([0],[0], color='b', lw=4, alpha=0.5, label='-x=0')])

ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
ax.set_title('Intersection of Planes for (A-I)x=0')
ax.view_init(20,-65)
plt.savefig("/mnt/c/Users/bharg/Documents/backupmatrix/ee25btech11013/matgeo/12.755/figs/Figure_1.png")
plt.show()
