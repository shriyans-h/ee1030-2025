import matplotlib.pyplot as plt
import numpy as np

p = np.array([[7], [-6]])
q = np.array([[3], [4]])

r = (p*2 + q*1)/3

points = [p, q, r]
x = [a[0] for a in points]
y = [a[1] for a in points]

fig, ax = plt.subplots()

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_title('Plotting P, Q and R')

ax.plot(x, y, 'b-')
ax.plot(x, y, 'ro')
ax.grid()

ax.annotate('P', p)
ax.annotate('Q', q)
ax.annotate('R', r)
fig.savefig('figs/plot.png')