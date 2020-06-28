"""
There are several quadrature function in scipy
"""

from scipy.integrate import quad, dblquad, nquad
import numpy as np

# Quad
f = lambda x: x*np.sin(x)

I = quad(f, 0, np.pi/2)
print(I) # The second value is the estimated absolute error
Int,_ = quad(f, 0, np.pi/2)
print(Int) # this will onli print the result 

# Double integration
fn = lambda x,y: x**2 * y + x * y**2
ax = 1; bx = 2;
ay = -1; by = 1; # Here the semicolon is used to put different commands in single lines

print(dblquad(fn, ax, bx, lambda y:ay, lambda y:by))
   