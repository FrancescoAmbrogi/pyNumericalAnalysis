"""
With this program we start the section of 
numerical differentiation. The finite difference method is used
to find the slope or derivative of a function.

The most used FDM methods are:
    1. Forward differences
    2. Backward differences
    3. Central differences
"""
import Plottings as myPlot
import numpy as np
from math import sin,cos,pi

# This is the numerical domain
x_sin = np.linspace(0,2*pi,101)
f1 = lambda x_sin: np.sin(x_sin)


def f_d1dx(f,x,h):
    f_d1dx = (f(x+h) - f(x)) / h
    return f_d1dx

def b_d1dx(f,x,h):
    b_d1dx = (f(x) - f(x-h)) / h
    return b_d1dx

def c_d1dx(f,x,h):
    c_d1dx = (f(x+h) - f(x-h)) / (2*h)
    return c_d1dx

myPlot.plot1D(x_sin, np.sin(x_sin), 3, label = 'sin(x)',xlabel='Angle [rad]', ylabel = 'f(x)', **myPlot.myColor(1))
myPlot.plot1D(x_sin, f_d1dx(f1,x_sin,0.5), 3, label='FD', xlabel='Angle [rad]', ylabel = 'f(x)', **myPlot.myColor(2))
myPlot.plot1D(x_sin, b_d1dx(f1,x_sin,0.5), 3, label='BD', xlabel='Angle [rad]', ylabel = 'f(x)', **myPlot.myColor(3))
myPlot.plot1D(x_sin, c_d1dx(f1,x_sin,0.5), 3, label='CD', xlabel='Angle [rad]', ylabel = 'f(x)', **myPlot.myColor(4))
myPlot.plot1D(x_sin, np.cos(x_sin), 3, 'sine_deriv.png', label='cos(x)', xlabel='Angle [rad]', ylabel = 'f(x)', **myPlot.myColor(5))



 