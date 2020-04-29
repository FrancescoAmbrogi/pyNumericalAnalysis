"""
Here we will show how to use the module sciPy to perform
interpolation. 
"""
import numpy as np
from scipy.interpolate import interp1d, lagrange
from scipy.stats import linregress
from scipy.optimize import curve_fit
import Plottings as myPlot

x = np.array([0,20,40,60,80,100])
y = np.array([26.0,48.6,61.6,71.2,74.8,75.2])

# This command interp1 will perform a linear interpolation
f = interp1d(x,y)
print('The function value at 50 is: ', f(50))

# If we want a quadratic interpolation we can type
f2 = interp1d(x, y, 'quadratic')
print('The function value at 50 is: ', f2(50))

# Or even cubic
f3 = interp1d(x, y, 'cubic')
print('The function value at 50 is: ', f3(50))

# Let us now try the lagrange interpolation function
L = lagrange(x, y)
print('The function value at 50 is: ', L(50))

"""
Here instead we will see the curve fitting function in scipy
"""

x1 = np.linspace(0,10,11)
y1 = np.array([0,7,17,26,35,45,70,38,55,47])
d = {'color':'black', 'linestyle':' ', 'marker':'*','markersize': 20}
myPlot.plot1D(x, y, 1, **d)

# This function will perform a linear regression algorithm
L1 = linregress(x,y)
print('y = (%f) + (%f)x' %(L1.intercept, L1.slope))
xfit = np.linspace(0,101,11)
yfit = L1.intercept + L1.slope*xfit
c = {'color':'red', 'linestyle':'-', 'linewidth':2}
myPlot.plot1D(xfit, yfit, 1, label='Linear fit', **c)

# In this section we will use the curv_fit function from sciPy
# The function require a function model curve_fit(f, x, y)
# f is a model function needed from curve_fit

# For a quadratic fitting we need 3 coefficients
# This is the model of the quadratic equation
def f1(x, a0, a1, a2):
    return a0 + a1*x + a2*x**2
# This is the model of the cubic equation
def f2(x, a0, a1, a2, a3):
    return a0 + a1*x + a2*x**2 + a3*x**3

a,b = curve_fit(f1, x, y)
g,h = curve_fit(f2, x, y)

# The coefficients are stored in a
print('The coeffs are: ', a)
print('The coeffs are: ', g)

yfit2 = a[0] + a[1]*xfit + a[2]*xfit**2
yfit3 = g[0] + g[1]*xfit + g[2]*xfit**2 + g[3]*xfit**3 

e = {'color':'blue', 'linestyle':'-', 'linewidth':2}
myPlot.plot1D(xfit, yfit2, 1, label='Quadratic fit', **e)

l = {'color':'green', 'linestyle':'-', 'linewidth':2}
myPlot.plot1D(xfit, yfit3, 1, label='Cubic fit', **l)
