"""

In some branch of physics (Fluid Dynamics) the data we acquire 
are noisy in some form. Derivatives tends to amplify the noise 
and we need to be able to go through this problem. Here is
an example of noisy data and how the 2 point forfula works
compared with a 4 points stencil finite difference formula

"""
import numpy as np
import Plottings as myplt
import myderivatives

x = np.linspace(0, 2*np.pi,101)

# here we create some noisy data starting from the cos(x)
y = np.cos(x) + 0.1 * np.random.random(size = x.shape)
yreal = np.cos(x)

# Let us visualize this data
myplt.plot1D(x, y, 1, label='Data', **myplt.myColor(1))
myplt.plot1D(x, yreal, 1, label='cos(x)', **myplt.myColor(2))
myplt.plot1D(x, -(np.sin(x)), 1, label='-sin(x)', **myplt.myColor(4))

# First let us use a forward formula
ddx_f = myderivatives.d1ydx_f(x, y)

# Then we use a central formula
ddx_c = myderivatives.d1ydx_c(x, y)

"""
now let us use a 4 point centered formula
(y[i-2] - 8*y[i-1] + 8*y[i+1] - y[i+2])/(12*h)
here we assume a constant grid size h
"""
d1ydx_c4 = np.zeros(len(x))
h = x[1] - x[0]

for i in range(2,len(x)-2):
    d1ydx_c4[i] = (y[i-2] - 8*y[i-1] + 8*y[i+1] - y[i+2])/(12 * h)
# now we need to set the first 2 and last 2 values with lower schemes
d1ydx_c4[0] = (y[1] - y[0])/(x[1] - x[0])
d1ydx_c4[1] = (y[2] - y[1])/(x[2] - x[1])
d1ydx_c4[-2] = (y[-2] - y[-3]) / (x[-2] - x[-3])
d1ydx_c4[-1] = (y[-1] - y[-2]) / (x[-1] - x[-2])
    
    
# ---------------- Plottings ------------------------------ #

myplt.plot1D(x, ddx_f, 1, label = 'FD 2points', **myplt.myColor(3))
myplt.plot1D(x, ddx_c, 1, label = 'CD 2points', **myplt.myColor(5))
myplt.plot1D(x, d1ydx_c4, 1, label = 'CD 4points', **myplt.myColor(6))


