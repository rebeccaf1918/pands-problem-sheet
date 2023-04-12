# Weekly Task 08
# plotask.py
# Histogram of a normal distribution of 1000 values with a mean of 5 and standard deviation of 2, 
# And a plot of the function h(x)=x3 in the range [0, 10], on the one set of axes.
# Author: Rebecca Feeley

import numpy as np 
from numpy import random
import matplotlib.pyplot as plt # these modules are necessary to plot the function and create the histogram

np.random.seed(1) # for debugging purposes, the seed here is used to give the same set of random numbers each time
histogram = np.random.normal(loc=5, scale = 2, size = 1000) # this creates an array of 1000 random numbers using (size),
# the loc (i.e mean) is set to 5, and the scale (i.e standard deviation) is set to 2.

plt.hist(histogram) # a historgram is plotted of the generated random numbers using the matplotlib hist function.
# plt.show() is not used at this point as it would not take in the second function on the same plot

xpoints = np.array(range(1,11)) # here the range function is used to create numbers from 1 to 10 (inclusive)
# also, the numpy array function converts these numbers from the range into an array called x points
ypoints = pow(xpoints, 3) # the numpy pow function takes each of the xpoints, and raises it to the power of 3 (i.e cubes it)

plt.plot (xpoints, ypoints, color = 'g', label = "h(x)=x^3") 
# here, a plot of the xpoints and ypoints are created, with the matplotlib functions colour used (g for green) 
#and itss given the label h(x)=x^3

# the next few lines are matplotlib functions which are used for altering the appearance of the plot i.e adding a title, and grid 
plt.grid(linestyle = '--', linewidth = 1)
plt.title("Weekly Task Plot")
plt.legend()
plt.xlim(1,10) # this function sets the x axis from 1 to 10 inclusive

plt.show() # this creates the plot with both the histogram and function on it as per the assignment
