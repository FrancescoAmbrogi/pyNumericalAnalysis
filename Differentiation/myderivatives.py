"""
Finite differences on arrays
"""
import numpy as np

def d1ydx_f(x,y):
    d1ydx_f = np.zeros(len(x))
    for i in range(len(x)-1):
        d1ydx_f[i] = (y[i+1] - y[i])/(x[i+1] - x[i])
    # now we set the last value using a backward differencing scheme
    d1ydx_f[-1] = (y[-1] - y[-2])/(x[-1] - x[-2])
        
    return d1ydx_f

def d1ydx_b(x,y):
    d1ydx_b = np.zeros(len(x))
    # We nee dto set the first point using a forward formula
    d1ydx_b[0] = (y[0] - y[1])/(x[0] - x[1]) 
    for i in range(1,len(x)):
        d1ydx_b[i] = (y[i] - y[i-1])/(x[i] - x[i-1])
        
    return d1ydx_b

def d1ydx_c(x,y):
    d1ydx_c = np.zeros(len(x))
    # We need to update the first value using a FDM scheme
    d1ydx_c[0] = (y[0] - y[1])/(x[0] - x[1])
    for i in range(1,len(x)-1):
        d1ydx_c[i] = (y[i+1] - y[i-1])/(x[i+1] - x[i-1])
    # Now we set the last value using a backward formula
    d1ydx_c[-1] = (y[-1] - y[-2])/(x[-1] - x[-2])
    
    return d1ydx_c

def d2ydx_c(x,y):
    # central scheme for the second derivative
    d2ydx_c = np.zeros(len(x))
    # We need to update the first value using a FDM scheme
    d2ydx_c[0] = (y[0] - 2*y[1] +y[2])/(x[0] - x[1])**2
    for i in range(1,len(x)-1):
        d2ydx_c[i] = (y[i+1] - 2*y[i] + y[i-1]) / (x[i+1] - x[i])**2
    # Now we set the last value using a backward formula
    d2ydx_c[-1] = (y[-1] - 2*y[-2] + y[-3])/(x[-1] - x[-2])**2
    
    return d2ydx_c
    