#  Creating Pie Chart
# https://www.w3schools.com/python/trypython.asp?filename=demo_matplotlib_pie2

import sys
#import matplotlib
#matplotlib.use('tkagg')

import matplotlib.pyplot as plt
import numpy as np

y = np.array([40, 20, 30, 10])
mylabels = ["Pomegranates", "Persimmons", "Grapes", "Dates"]

plt.pie(y, labels = mylabels)
plt.show() 

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()