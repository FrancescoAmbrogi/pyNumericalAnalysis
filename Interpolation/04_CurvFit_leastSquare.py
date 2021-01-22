"""
With this program we start the section: curve fitting
We want to find the equation of the curve that passes through the given data
points with least deviation from the points

NB The main difference between interpolation and curve fitting is that in 
this case the function does not have to coincide with all the points.

Here we use the method of least-squares method.
Find the equation of a straight line that fits the data.
"""
import Plottings as myPlt
import numpy as np

# Let us considere that we have this dataset
x = np.array([0, 10, 20, 30, 40, 50, 60],float) 
y = np.array([-2.0, 1.7, 8.2, 33, 25, 45, 32],float)

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

myPlt.plot1D(x, y, 1, label='Data',**myPlt.myColor(1))
myPlt.plot1D(x, yline, 1, label='Fit', **myPlt.myColor(2))



