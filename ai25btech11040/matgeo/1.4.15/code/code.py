import matplotlib.pyplot as plt
import numpy as np

p = np.array([[7], [-6]])
q = np.array([[3], [4]])

l = 1
m = 2

r = (p*m + q*l)/(l+m)

points = [p, q, r]
x = [a[0] for a in points]
y = [a[1] for a in points]

if (r[0][0] > 0 and r[1][0] > 0):
    print("Q1")
if (r[0][0] > 0 and r[1][0] < 0):
    print("Q4")
if (r[0][0] < 0 and r[1][0] > 0):
    print("Q2")
if (r[0][0] < 0 and r[1][0] < 0):
    print("Q3")

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