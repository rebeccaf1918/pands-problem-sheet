# Weekly Task 08
# plotask.py
# Histogram of a normal distribution of 1000 values with a mean of 5 and standard deviation of 2, 
# And a plot of the function h(x)=x3 in the range [0, 10], on the one set of axes.
# Author: Rebecca Feeley

import numpy as np 
from numpy import random
import matplotlib.pyplot as plt

np.random.seed(1)
histogram = np.random.normal(loc=5, scale = 2, size = 1000)

plt.hist(histogram)
# plt.show()

xpoints = np.array(range(1,11))
ypoints = pow(xpoints, 3)

plt.plot (xpoints, ypoints, color = 'g', label = "h(x)=x^3")

plt.grid(linestyle = '--', linewidth = 1)
plt.title("Weekly Task Plot")
plt.legend()

plt.show()
