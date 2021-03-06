'''
# In this program we implement the Newton Raphson method
# For solving high order non linear equation
# The basic rule is:
# x_new = x - f(x) / f'(x)
# Therefore we need to evaluate the derivative of the f
# let us use the same equation as 04_bisection_rf

# Let's solve first equation 3x**2 -5x +2 = 0
# Analytical solutions: x_1 = 1, x_2 = 2/3
# Equation: x**6 -x - 1 = 0
# It has a solution very close to 1
'''
import time
from matplotlib import pyplot as plt
from math import sin, cos

x = float(input("Enter the initial guess: ")) # initial guess x = 0
eps = 10e-06 # tolerance
t = time.time()
plt.figure(11,figsize=(22,14), dpi=100)
plt.grid(True)

for it in range(1,101): # Where it is the counter for iterations
    #x_new = x - (-4*x**2 - 7*x +12)/(-8*x - 7)
    x_new = x - (x**6 - x - 1)/(5*x**5 - 1)
    
    plt.plot(it, x_new, '-ko')
    plt.plot(it, x, '-ro')
    plt.pause(0.05)
    plt.xlabel('Iterations', fontsize=20)
    plt.ylabel('Value of x', fontsize=20)
    # Check for convergence
    if abs(x_new - x) < eps:
        break
    x = x_new
    
print('Number of iterations: %d' % it)
print('The solution found is: %0.5f' % x_new)
print('The calculation took: ' + str('{0:2f}'.format(time.time() -t)) + 's\n') 

"""
Let's now solve equation
f(y) = y**2 + cos**2(y) - 4y
f'(y) = 2y - 2*sin(y)cos(y) - 4
"""

y = 10 # initial guess
t1 = time.time()
plt.figure(21,figsize=(22,14), dpi=100)
plt.grid(True)

for it in range(1,101): # Where it is the counter for iterations
    y_new = y - (y**2 + cos(y)**2 - 4*y)/(2*(y -sin(y)*cos(y) - 2))
    
    plt.plot(it, y_new, '-ko')
    plt.plot(it, y, '-ro')
    plt.pause(0.05)
    plt.xlabel('Iterations', fontsize=20)
    plt.ylabel('Value of y', fontsize=20)
    # Check for convergence
    if abs(y_new - y) < eps:
        break
    y = y_new

print('Number of iterations: %d' % it)
print('The solution found is: %0.5f' % y_new)
print('The calculation took: ' + str('{0:2f}'.format(time.time() -t1)) + 's\n') 
    
    
plt.show()
    
   
    