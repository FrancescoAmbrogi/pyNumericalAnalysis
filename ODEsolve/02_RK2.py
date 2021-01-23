"""
2nd order Runge-Kutta method

We can semplify the procedure by deviding it into 3 steps

K1 = hy'(x,y)
K2 = hy'(x+h/2,y+1\2K1)
y(x+h) = y(x) + K2


Let's solve the problem y' = xy
Analytical solution = e^(x^2)

At the end we will also compare is with the solution
obtained using the Euler method.
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
ye = 1
h = 0.1 # step size

n = int((xn - x) / h)

# Main loop

"""
2nd order RK
"""
for i in range(1,n+1):
    K1 = h * dy(x,y)
    K2 = h * dy(x + h/2, y + K1/2)
    y += K2
    x += h
    myplt.plot1D(x, y, 1,**myplt.myColor(3))
    
# x domain
x = 0
xn = 2

y = 1 # initial value
h = 0.1 # step size

n = int((xn - x) / h)
    
"""
Euler method
"""
for i in range(n):
    y = y + dy(x,y)*h 
    x = x + h
    myplt.plot1D(x, y, 1,**myplt.myColor(2))
    
myplt.plot1D(xex, yex, 1,**myplt.myColor(1))