"""
FDM with non-uniform grid

Sometimes we do not want a uniform grid. Thinking about CFD
this is because we want to resolve the velocity gradients in
our domain and for this reason we might want to refine the 
grid were this gradients are concentrated (Ex near a solid wall).

"""
import numpy as np
import time
from math import pi
import Plottings as myplt

# lets use the cosine this time
x = np.linspace(0,2*pi,101)
y = np.cos(x)
dy_analy = -(np.sin(x))

# Let's calculate the CPU time
tfdm = time.time()
"""
We first use a forward differencee scheme
remembering that the last point is not defined
"""
d1ydx_f = np.zeros(len(x))
for i in range(len(x)-1):
    d1ydx_f[i] = (y[i+1] - y[i])/(x[i+1] - x[i])
# now we set the last value using a backward differencing scheme
d1ydx_f[-1] = (y[-1] - y[-2])/(x[-1] - x[-2])

print('FDM took %f sec' %(time.time() - tfdm))

tbdm = time.time()
"""
Now we use a backward difference scheme
remembering that the first point is not defined
"""
d1ydx_b = np.zeros(len(x))
# We nee dto set the first point using a forward formula
d1ydx_b[0] = (y[0] - y[1])/(x[0] - x[1]) 
for i in range(1,len(x)):
    d1ydx_b[i] = (y[i] - y[i-1])/(x[i] - x[i-1])
    
print('FBM took %f sec' %(time.time() - tbdm))

"""
Now we use a central difference scheme
remembering that the first & last points are not defined
"""    
tcdm = time.time()

d1ydx_c = np.zeros(len(x))
# We need to update the first value using a FDM scheme
d1ydx_c[0] = (y[0] - y[1])/(x[0] - x[1])
for i in range(1,len(x)-1):
    d1ydx_c[i] = (y[i+1] - y[i-1])/(x[i+1] - x[i-1])
# Now we set the last value using a backward formula
d1ydx_c[-1] = (y[-1] - y[-2])/(x[-1] - x[-2])

print('FCM took %f sec' %(time.time() - tcdm))


# lets plot the results compared with analytical derivative
myplt.plot1D(x, dy_analy, 1, label='Analytical', **myplt.myColor(1))
myplt.plot1D(x, d1ydx_f, 1,label='FD', **myplt.myColor(2))
myplt.plot1D(x, d1ydx_b, 1,label='BD', **myplt.myColor(3))
myplt.plot1D(x, d1ydx_c, 1,label='CD', **myplt.myColor(4))



    
