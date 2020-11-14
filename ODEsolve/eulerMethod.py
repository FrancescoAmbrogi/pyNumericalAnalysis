"""
Euler's method to solve ODE

@author: Francesco

Let's solve the equation: y' = xy
Exact solution: y = e^(x^2/2)
"""

import Plottings as myplt
import numpy as np

# definition of the function
dy = lambda x,y: x*y

# exact function
xex = np.linspace(0,2,100)
yex = np.exp(xex**2/2)

# x domain
x = 0
xn = 2
y = 1 # initial value
h = 0.01 # step size

n = int((xn - x) / h)

print('x \t\t y')
print('%f \t %f' % (x,y))

for i in range(n):
    y = y + dy(x,y)*h 
    x = x + h
    print('%f \t %f' % (x,y))
    
    myplt.plot1D(x, y, 1, **myplt.myColor(2))
myplt.plot1D(xex, yex, 1, **myplt.myColor(1))



