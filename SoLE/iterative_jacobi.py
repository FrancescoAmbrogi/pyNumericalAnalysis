"""
Jacobi's method for solving a SLE'

@author: Francesco
"""

import numpy as np

A = np.array([[4, 1, 2, -1 ],
              [3, 6, -1, 2 ],
              [2, -1, 5, -3],
              [4, 1, -3, -8 ]],float)

b = np.array([2, -1, 3, 2], float)

# Let us determine the size of the array
(n,) = np.shape(b)

# We want to give the initial guess for the whole array x
x = np.full(n,1.0, float)

# let's create an array of given size empy
xnew = np.empty(n, float)

# let's define the maximum number of iterations
imax = 100

# also the tolerance is very important
tol = 1.0e-6

# Starts the iteration

for i in range(imax): # remeber always that the range function willl not include tha last number
    for k in range(n): # here we will go equation by equation
        s = 0 # initialization of the summation variable
        for p in range(n):
            if p != k:
                s = s + A[k,p] * x[p]
                
        xnew[k] = -1/A[k,k] * (s - b[k])  
    
    if (abs(xnew - x) < tol).all():
        break
    else:
        x = np.copy(xnew) # here we should use copy and not just xnew
        # if we do not copy then the two array are linked to each other and changing one
        #would also affect the other
        
print('The solution: ')
print(x)
print('Number of iterations: %d '% (i+1))
        
        
        
    
    




