# This program explains how a very simple iterative methods works
# Let's solve equation 3x**2 -5x +2 = 0
# Analytical solutions: x_1 = 1, x_2 = 2/3 
"""
This first method uses a for loop
"""
from math import sqrt
import time
from matplotlib import pyplot as plt

# The iterative method requires an initial guess
x = 0

# The iterative method also needs the degree of accuracy
eps = 10e-06

# Let us also define the figure
plt.figure(11,figsize=(22,14), dpi=100)

# The iterative method is started with a loop
# it = iterations

t = time.time()
for it in range(1,101): # Remembere python starts counting from 0
    # Here we write the equation in the compact form, there are two of them
    
    #x_new = sqrt((5*x - 2)/3)
    x_new = (3*x**2 + 2)/5
    
    plt.subplot(211)
    plt.grid(True)
    plt.plot(it, x_new, '-ko', it, x, '-ro')
    plt.pause(0.05)
    plt.ylabel('Value of x', fontsize=20)
    
    # Now we need to check if x_new is close to x
    if abs(x_new - x) < eps:
        break
    
    # Now we need to update the x value
    x = x_new
    
print('Number of iterations: %d' % it)
print('The solution found is: %0.5f' % x_new)
print('The calculation with for took: ' + str('{0:2f}'.format(time.time() -t)) + 's\n')
    
# Notice that we only found one root of the equation 2/3.
# In order to find the other one we should change the form of the equation

"""
This second method uses a while loop
"""
y = 3 # this is now an arbitrary value
y_new = 0 # this is now the initial guess
yps = 10e-06
its = 0
t1 = time.time()

#plt.figure(21,figsize=(22,14), dpi=100)
#plt.grid(True)
#plt.title('Convergence While Loop',fontsize=24)


while abs(y_new - y) >= yps: # if this condition is NOT satisfied the loop will not be executed
    its += 1
    y = y_new
    y_new = (3*y**2 + 2)/5
    #y_new = sqrt((5*y - 2)/3)
    plt.subplot(212)
    plt.grid(True)
    plt.plot(its,y_new,'-m*',its,y,'-b*')
    plt.xlabel('Iterations', fontsize=20)
    plt.ylabel('Value of y', fontsize=20)
    plt.pause(0.05)
    
print('The solution found is: %0.5f' % y_new)
print('Number of iterations: %d' % its)
print('The calculation with for took: ' + str('{0:2f}'.format(time.time() -t1)) + 's\n')


plt.show()



