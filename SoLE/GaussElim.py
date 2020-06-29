"""
This program contains the Gaussian Elimination method
For solving a system of linear equation (SoLE)
@author: Francesco
"""

# Step 1: Put the system in the augmente dform

# Step 2: We need to make all the elements in the lower triangular part zero.
# We will do the elimination by column but the operations are by row.
 
import numpy as np

A = np.array([[2, 7, -1, 3, 1 ],
              [2, 3,  4, 1, 7 ],
              [6, 2, -3, 2, -1],
              [2, 1, 2, -1, 2 ],
              [3, 4, 1, -2, 1 ]],float)

b = np.array([5, 7, 2, 3, 4], float)

# Order of the square matrix
n = len(b)

# Let's create the unknown matrix x
x = np.zeros(n, float)

"""
Elimination part
"""

for k in range(n-1): # until the row before the last
    for i in range(k+1, n): 
        
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
   
    

    

            
        

            








