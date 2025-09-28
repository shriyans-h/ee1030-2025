
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt

from call import get_data_from_c

all_data = get_data_from_c()
num_points = 51
focus = all_data[0:2]
parabola_orig = all_data[2 : 2 + num_points*2].reshape((num_points, 2))

parabola_locus = all_data[2 + num_points*2 :].reshape((num_points, 2))

# --- Plotting ---
fig, ax = plt.subplots(figsize=(12, 10))

ax.plot(parabola_orig[:, 0], parabola_orig[:, 1], 'b-', label='$y^2=4ax(a=2)$')
ax.plot(parabola_locus[:, 0], parabola_locus[:, 1], 'r-', label='Locus Parabola')
ax.text(8 + 0.5, 8, '$y^2=4ax(a=2)$', fontsize=12, color='blue')
ax.axvline(x=0, color='g', linestyle='--', label='Directrix of Locus (x=0)')

ax.scatter(focus[0], focus[1], color='black', s=100, zorder=5, label='Focus')
ax.text(focus[0] + 0.2, focus[1] + 0.2, 'F(2,0)')

ax.set_title('Locus of the Midpoint',fontsize=14)
ax.set_xlabel('X-axis',fontsize=14)
ax.set_ylabel('Y-axis',fontsize=14)

ax.grid(True)
ax.axis('equal')
ax.legend()
plt.show()
