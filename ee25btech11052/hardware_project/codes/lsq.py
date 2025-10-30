import numpy as np
import matplotlib.pyplot as plt
import padasip as pa

A = np.loadtxt('/home/shriyasnh/Desktop/hardware_project/codes/training_data.txt')
X = np.hstack((np.ones((A.shape[0],1)),A[:,[0]],A[:,[0]]**2))
T = A[:,[0]]
C = A[:,[1]]

#Least squares method
v, av, bv = np.linalg.lstsq(X, C, rcond=None)[0]
n_lsq = np.zeros((3,1))
n_lsq[0][0] = v
n_lsq[1][0] = av
n_lsq[2][0] = bv
print(n_lsq)

#Plot both the results
plt.plot(T, X@n_lsq)
plt.plot(T, C, 'k.')
plt.grid()
plt.ylabel('Output Voltage (V)')
plt.xlabel(r'Temperature ($^{\circ}$C)')
plt.tight_layout()
plt.savefig('/home/shriyasnh/Desktop/hardware_project/codes/figs/train.png')


#Plot for validation
B = np.loadtxt('/home/shriyasnh/Desktop/hardware_project/codes/validating_data.txt')
Xv = np.hstack((np.ones((B.shape[0],1)),B[:,[0]],B[:,[0]]**2))
Cv = B[:,[1]]
Tv = B[:,[0]]
plt.figure()
plt.plot(Tv, Xv@n_lsq)
plt.plot(Tv, Cv, 'k.')
plt.ylabel('Output Voltage (V)')
plt.xlabel(r'Temperature ($^{\circ}$C)')
plt.grid()
plt.tight_layout()
plt.savefig('/home/shriyasnh/Desktop/hardware_project/codes/figs/valid.png')
