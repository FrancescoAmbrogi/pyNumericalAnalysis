"""
Let us implement now the bisection method for root finding
Let use it to find the root of the function: f = 2x**2 - 5x + 3
"""
from matplotlib import pyplot as plt
import numpy as np
import time

# Create an x array
x = np.linspace(0,2,21)
# Let us evaluate the function f in x
f = 2*x**2 - 5*x + 3

# Let us plot the function f to understand its shape
plt.figure(11,figsize=(22,14), dpi=100)
plt.grid(True)
plt.plot(x, f, '-ko', label='Function f')
plt.xlabel('Value of x', fontsize=20)
plt.ylabel('Value of f', fontsize=20)
plt.legend(fontsize=26)

# Lets use another way of definying a function
def givenf(x):
    f = 2*x**2 - 5*x + 3
    return f

# We see precisely that this function has two roots 1.0 and 1.5
# In the bisection method we basically want to enclose one of them with our guesses

# Choose 2 initial guesses
x1 = float(input("Enter the first guess x1: "))  # 0
x2 = float(input("Enter the second guess x2: "))  # 1.4
# We have to evaluate the function in x1 and x2 to see it it change sign
y1 = givenf(x1)
y2 = givenf(x2)

# now we need to check for the sign of y1 and y2
if y1 == 0 or y2 == 0:
    print('We found one of the root!\n')
    if y1 == 0:
        print('The root is:',x1)
    else:
        print('The root is:',x2)
elif y1*y2 > 0:
    print('We missed the root!')
    exit
else:
    print('We bounded the root!\n')
    
t = time.time()
plt.figure(21,figsize=(22,14), dpi=100)
plt.grid(True)
plt.xlabel('Iterations', fontsize=20)
plt.ylabel('Value of x', fontsize=20)

# Now begins the computation of bisection method
# Don't forget the tolerance
eps = 1.0E-6
for it in range(1,101): # we assume 100 iteration of bisection method
    xc = (x1 + x2)/2 # This is the middle value between the two initial guesses
    # Let us evaluate yc
    yc = givenf(xc)
    y1 = givenf(x1)
    
    plt.plot(it, x1, '-ko')
    plt.plot(it, xc, '-ro')
    plt.pause(0.05)
    
    if abs(y1) < eps:
        break # we approached one of the roots
    elif y1 * yc < 0: # The root is in the first half
        x2 = xc
    else: # The root is in the second half
        x1 = xc
    
    
    
print('Number of iterations: %d' % it)
print('The solution found is: %0.5f' % x1)
print('The calculation took: ' + str('{0:2f}'.format(time.time() -t)) + 's\n')     
        
        
        
        
    
    


    
