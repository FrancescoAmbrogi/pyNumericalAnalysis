"""
With this program we start the section of 
numerical differentiation. The finite difference method is used
to find the slope or derivative of a function.

The most used FDM methods are:
    1. Forward differences
    2. Backward differences
    3. Central differences

In this program the computation is carried out taking uniform 
grid size h.

This routine also uses a new module Plottings.
I would suggest everyone to build his own module,
it's a very powerful tool of python.

"""
import Plottings as myPlot
import numpy as np
from math import pi

# This is the numerical domain
# Let-s use a well know function
# which has a very well know derivative

x_sin = np.linspace(0,2*pi,101)
f1 = lambda x_sin: np.sin(x_sin)

# 1st order forward
# Uses a two point stencil: i+1 and i
def f_d1dx(f,x,h):
    f_d1dx = (f(x+h) - f(x)) / h
    return f_d1dx

# 1st order backward
# Uses a two point stencil: i and i-1
def b_d1dx(f,x,h):
    b_d1dx = (f(x) - f(x-h)) / h
    return b_d1dx

# 2nd order central
# Uses a two point stencil: i+1 and i-1
def c_d1dx(f,x,h):
    c_d1dx = (f(x+h) - f(x-h)) / (2*h)
    return c_d1dx

# 2nd order central second derivative
# Uses a two point stencil: i+1 and i-1
def c_d2dx(f,x,h):
    c_d2dx = (f(x+h) - 2*f(x) + f(x-h)) / h**2
    return c_d2dx

# Define the grid size
dx = 0.1

myPlot.plot1D(x_sin, np.sin(x_sin), 1, label = 'sin(x)',xlabel='Angle [rad]', ylabel = 'f(x)', **myPlot.myColor(1))
myPlot.plot1D(x_sin, f_d1dx(f1,x_sin,dx), 1, label='FD', xlabel='Angle [rad]', ylabel = 'f(x)', **myPlot.myColor(2))
myPlot.plot1D(x_sin, b_d1dx(f1,x_sin,dx), 1, label='BD', xlabel='Angle [rad]', ylabel = 'f(x)', **myPlot.myColor(3))
myPlot.plot1D(x_sin, c_d1dx(f1,x_sin,dx), 1, label='CD', xlabel='Angle [rad]', ylabel = 'f(x)', **myPlot.myColor(4))
# exact solution
myPlot.plot1D(x_sin, np.cos(x_sin), 1, label='cos(x)', xlabel='Angle [rad]', ylabel = 'f(x)', **myPlot.myColor(5))
# second derivative
myPlot.plot1D(x_sin, -(np.sin(x_sin)), 2, label = '-sin(x)',xlabel='Angle [rad]', ylabel = 'f(x)', **myPlot.myColor(1))
myPlot.plot1D(x_sin, c_d2dx(f1, x_sin, dx), 2, label='2nd CD', xlabel='Angle [rad]', ylabel = 'f(x)', **myPlot.myColor(2))


 