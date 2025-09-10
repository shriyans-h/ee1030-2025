import numpy as np
import matplotlib.pyplot as plt

def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB


vector = np.zeros(3)
vector[0] = input("Input the first entry")
vector[1] = input("Input the second entry")
vector[2] = input("Input the third entry")

print(np.linalg.norm(vector))

A = np.array([vector[0],vector[1],vector[2]])
B = np.array([vector[1],vector[2],vector[0]])
C = np.array([vector[2],vector[0],vector[1]])


fig = plt.figure(figsize = (6,6))

ax = fig.add_subplot(111, projection='3d')

AB = line_gen(A,B)
BC= line_gen(B,C)
CA= line_gen(C,A)


#Plotting all lines
plt.plot(AB[0,:],AB[1,:],AB[2,:],label='$AB$')
plt.plot(BC[0,:],BC[1,:],BC[2,:],label='$BC$')
plt.plot(CA[0,:],CA[1,:],CA[2,:],label='$CA$')


ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

plt.grid()
plt.axis('equal')


plt.show()