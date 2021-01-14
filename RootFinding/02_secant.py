"""
In this program we implement the secant method
in the root finding topic.
"""
# Let us define the function of the secant method
import time
from math import cos

t = time.time()
def sec_method(f, x1, x2, tol, imax):
    for i in range(imax):
        xn = x2 - (x2 - x1)/(f(x2) - f(x1)) * f(x2)
        if abs(xn - x2) < tol:
            break
        else:
            x1 = x2
            x2 = xn
    else: # This else is related to the for loop (feature in python)
        print("Warning!! Max iterations number is reached")
    return xn, i

# Let us define the function here
# and lets do it using the lambda function
f = lambda x: x**3 - 6*x**2 + 11*x - 6
f2 = lambda x: x - cos(x)

# Remember: the secant method will need 2 guesses
x1 = float(input("Enter the first guess x1: "))
x2 = float(input("Enter the second guess x2: "))

# The tolerance is always required
tol = 1.0E-6
imax = 100

# Here now, we call the function 
sol, nit = sec_method(f2, x1, x2, tol, imax)

# here we print the solution on the shell:
print('Number of iterations: %d' % nit)
print('The solution found is: %0.5f' % sol)
print('The calculation took: ' + str('{0:2f}'.format(time.time() -t)) + 's\n')
        
