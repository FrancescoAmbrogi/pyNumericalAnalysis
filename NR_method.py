'''
# In this program we implement the Newton Raphson method
# For solving high order non linear equation
# The basic rule is:
# x_new = x - f(x) / f'(x)
# Therefore we need to evaluate the derivative of the f
# let us use thea same equation as simple_it_method
# Let's solve equation 3x**2 -5x +2 = 0
# Analytical solutions: x_1 = 1, x_2 = 2/3 
'''
import time
from matplotlib import pyplot as plt

x = 0 # initial guess
eps = 10e-06 # tolerance
t = time.time()
plt.figure(11,figsize=(22,14), dpi=100)
plt.grid(True)

for it in range(1,101): # Where it is the counter for iterations
    x_new = x - (3*x**2 - 5*x +2)/(6*x - 5)
    
    plt.plot(it, x_new, '-ko')
    plt.plot(it, x, '-ro')
    plt.pause(0.05)
    plt.xlabel('Iterations', fontsize=20)
    plt.ylabel('Value of x', fontsize=20)
    # Check for convergence
    if abs(x_new - x) < eps:
        break
    x = x_new
    
plt.show()
    
print('Number of iterations: %d' % it)
print('The solution found is: %0.5f' % x_new)
print('The calculation with for took: ' + str('{0:2f}'.format(time.time() -t)) + 's\n')    
    