"""
Gauss elimination code 2

@author: Francesco
"""

import numpy as np

A = np.array([[0, 7, -1,  3, 1 ],
              [2, 3,  4,  1, 7 ],
              [6, 2,  0,  2, -1],
              [2, 1,  2,  0, 2 ],
              [3, 4,  1, -2, 1 ]],float)

b = np.array([5, 7, 2, 3, 4], float)

# Order of the square matrix
n = len(b)

# Let's create the unknown matrix x
x = np.zeros(n, float)

"""
Elimination part. We should make some modification to our problem in order
not to divide by 0.
"""

for k in range(n-1): # until the row before the last
    # here we make the check for a(k,k)
    if A[k,k] == 0:
        
        # lets swap the rows
        for j in range(n):
            A[k,j],A[k+1,j] = A[k+1,j],A[k,j]
        b[k],b[k+1] = b[k+1],b[k]
        
    for i in range(k+1, n): 
        # Here we make a check
        if A[i, k] == 0:
            # we don't need to make the further modification
            continue
        # Computation of the multiplier
        fctr = A[k,k] / A[i, k]
        
        # remember the subctraction goes from column to column
        for j in range(k,n):
            
            A[i,j] = A[k,j] - fctr * A[i,j]
            # Now you have a tridiagonal matrix
        
        # Now we need to compute the b which is independent of j
        b[i] = b[k] - fctr * b[i]
        
"""
Back-substitution step
"""
# we need to start from the very last element
# Here the incrementation of the loop is negative

x[n-1] = b[n-1] / A[n-1,n-1]

for i in range(n-2, -1, -1): # From the row before the last to the first row, backwards
    sumA = 0
    for j in range(i+1, n):
        
        sumA = sumA + A[i,j] * x[j]
        
    x[i] = (b[i] - sumA) / A[i,i]

print(x)



