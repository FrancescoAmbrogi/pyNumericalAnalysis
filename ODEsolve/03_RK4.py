"""
4th order Runge-Kutta method

Let's solve the problem y' = xy
Analytical solution = e^(x^2)

"""

import Plottings as myplt
import numpy as np
from math import exp

# definition of the function
dy = lambda x,y: x*y
f = lambda x: exp(x**2/2)

# exact function
xex = np.linspace(0,2,100)
yex = np.exp(xex**2/2)

# x domain
x = 0
xn = 2

y = 1 # initial value
h = 0.5 # step size

n = int((xn - x) / h)

# Main loop

"""
2nd order RK
"""
for i in range(n):
    K1 = h * dy(x,y)
    K2 = h * dy(x + h/2, y + K1/2)
    K3 = h * dy(x + h/2, y + K2/2)
    K4 = h * dy(x + h, y + K3)
    y += (K1 + 2*K2 + 2*K3 + K4) / 6
    x += h
    myplt.plot1D(x, y, 1,**myplt.myColor(1))
myplt.plot1D(xex, yex, 1,label="Exact",**myplt.myColor(3))