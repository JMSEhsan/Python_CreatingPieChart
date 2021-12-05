# Creating Pie Chart
# https://www.w3schools.com/python/trypython.asp?filename=demo_matplotlib_pie2

import sys
#import matplotlib
#matplotlib.use('tkagg')

import matplotlib.pyplot as plt
import numpy as np

y = np.array([25, 10, 35, 30])
mylabels = ["Dates", "Persimmons", "Grapes", "Pomegranates"]

plt.pie(y, labels = mylabels)
plt.show() 

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()