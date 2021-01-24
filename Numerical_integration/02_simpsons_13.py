"""
In this program we introduce the Simpson's 1/3 rule.
This method calculates the area of two strips at a time, therefore 3 values 
of the variable are necessary to carry out the caluclation. 
In order to cover the whole domain an EVEN number of 
divisions is needed. VERY IMPORTANT!

The Simpson ruule in compact form reads as:
    
    I = 1/3 * h * {[f(a) + f(B)] + sum_{i odd}^n-1 4 * f(xi) + sum_{i even}^n-2 2 * f(xi)}
    
"""

from math import sin, pi

# Here we define the function we want to integrate
#f = lambda x: x * sin(x)     # Function 1
f = lambda x: 1 / (1 + x)     # Function 2

a = 0
#b = pi / 2     # Function 1
b = 1           # Function 2
n = 2 # Remember that the number of division must be even

h = (b - a) / n
M = (f(a) + f(b))

for i in range(1,n,2): # Here we only sum the odd indeces
    M = M + 4 * f(a + i * h)

for i in range(2,n,2):  # Here we only sum the odd indeces
    M = M + 2 * f(a + i * h)
    
I = h / 3 * M

print('The integral = %f' % I)
# As we notice Simpson's rule is way faster and more accurate that the trapezoidal rule

# Error calculation
err = ((I-0.693147)/0.693147) * 100
print('The error in percentage is = %f' % err)
# Now compare the error with the trapezoidal method: what do you see?


