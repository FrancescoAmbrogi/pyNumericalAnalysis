"""
With this program we start the section: curve fitting
We want to find the equation of the curve that passes through the given data
points with least deviation from the points

NB The main difference between interpolation and curve fitting is that in 
this case the function does not have to coincide with all the points.

Here we use the method of least-squares method.
Find the equation of a straight line that fits the data.
"""
from FraFunctions import plot1D
import numpy as np

# Let us considere that we have this dataset
x = np.array([3, 4, 5, 6, 7, 8],float) 
y = np.array([0, 8, 14, 33, 25, 45],float)

# Degree of the polynomial
n = len(x)

# Lets us find the coefficients a and b of the straight line
a = (np.mean(y)*np.sum(x**2) - np.mean(x)*np.sum(x*y))/(np.sum(x**2) - n*np.mean(x)**2)
b = (np.sum(x*y) - np.mean(x)*np.sum(y))/(np.sum(x**2) - n*np.mean(x)**2)

# Finally we print the result
print('The straight line equation is: \n')
print('y = (%.3f) +(%.3f)x' % (a,b))

yline = a + b*x

# Let us plot the points and the straight line
d = {'color':'black',
     'linestyle':'--',
     'marker':'o'}
c = {'color':'red',
     'linestyle':'-'}

plot1D(x, y, label='Data', **d)
plot1D(x, yline, label='Fit', **c)



