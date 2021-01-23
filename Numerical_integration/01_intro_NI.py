"""
This program will start the section about
the numerical integration. Very very useful topic in
numerical analysis.

The trapezoidal rule basically divides the area under the function
(the integral) in a number of trapezoids and then it approximates it by summing
up the area of all the trapezoids.

Let's start by finding the integral of: /int_0^pi/2 x * sin(x) dx

"""
import numpy as np
from math import pi

# let us define the function we want to integrate
f = lambda x: x * np.sin(x)

# Let us define the first and last value of the integral
a = 0
b = pi / 2

# define the numbers of segments
n = 5

# Let us define the grid size
h = (b - a) / n

"""
Here starts the computation
"""
M = 0.5 * (f(a) + f(b)) 

for i in range(1,n):
    # Remember the range function will not comprehend the last value n
    # we need to sum f(x1) f(x2) .... f(x_(n-1))
    # but we remember that the grid is uniform and f(x1) = f(a + h)
    M = M + f(a + i*h)

Int = h * M

"""
Let us print the result
"""
#Rmembering that the analytical value is: 1
print('The integral of f is = %f:' % Int)

# We see that unless we use a very large number of intervals
# The error of the trapezoidal rule has a pretty high error associated.

    
    




