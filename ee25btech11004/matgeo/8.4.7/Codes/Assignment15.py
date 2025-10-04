import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize = (6,6))
ax = fig.add_subplot(111)

X = np.linspace(-10,10,50)

p1 = X*X/8

p2 = X*X/2
l = np.zeros(50) - 2

ax.plot(X,p1, label = '$x^2 = 8y$', color = 'green')
ax.plot(X,p2, label = '$x^2 = 2y$', color = 'red')
ax.plot(X,l, label = '$y=-2$', color = 'orange')

ax.scatter(0,2, label = 'Focus')

ax.grid(True)
ax.legend()
plt.show()
