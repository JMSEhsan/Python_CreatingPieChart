# Creating Grid
#https://www.w3schools.com/python/matplotlib_grid.asp



#One lines to make our compiler able to draw:
import sys
#import matplotlib
#matplotlib.use('Agg')

import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5, 6, 6, 7, 20])
y = np.array([4, 5, 10, 5, 12, 3, 15, 7, 7])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid()

plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
