"""
Here we perform interpolation using spline
"""
from scipy.interpolate import interp1d
from scipy.optimize import fmin

import numpy as np
import Plottings as myPlt

x = np.array([ 0,      1,      2,      3,      4    ])
y = np.array([ 0.,     0.308,  0.55,   0.546,  0.44 ])

# Here we create the interpolating function
fx = interp1d(x, y, kind='cubic', bounds_error=False)

# To find the maximum we use an optimization technique. 
# We minimize the negative of the function

fx2 = interp1d(x, -y, kind='cubic')
xmax = fmin(fx2, 2.5)

xfit = np.linspace(0,4)

myPlt.plot1D(x, y, 1, label='Data', **myPlt.myColor(1))
myPlt.plot1D(xfit, fx(xfit), 1, label='Spline fit', **myPlt.myColor(2))
myPlt.plot1D(xmax, fx(xmax), 1, label='Max Valuse', **myPlt.myColor(3))

