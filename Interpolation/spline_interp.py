"""
Here we perform interpolation using spline
"""
from scipy.interpolate import interp1d
from scipy.optimize import fmin

import numpy as np
from FraFunctions import plot1D

x = np.array([ 0,      1,      2,      3,      4    ])
y = np.array([ 0.,     0.308,  0.55,   0.546,  0.44 ])

# Here we create the interpolating function
fx = interp1d(x, y, kind='cubic', bounds_error=False)

# To find the maximum we use an optimization technique. 
# We minimize the negative of the function
fx2 = interp1d(x, -y, kind='cubic')
xmax = fmin(fx2, 2.5)

xfit = np.linspace(0,4)
d = {'color':'red',
     'linestyle':'-.',
     'marker':'o'}
c = {'color':'green',
     'marker':'*'}
a = {'color':'blue',
     'linestyle':'-'}

plot1D(x, y, label='Data', **d)
plot1D(xfit, fx(xfit), label='Spline fit', **a)
plot1D(xmax, fx(xmax),label='Max Valuse', **c)

