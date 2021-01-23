"""
This program contains the Gaussian Elimination method
For solving a system of linear equation (SoLE)

In many fields of physics and mathematics we will end
up having to solve a system of equations [linear or non linear
depending on the physics] which can also be huge in size.

The system is on the form Ax = b where

- A is the matrix of the coefficients
- x is the vecor of unknowns
- b is commonly referred a the right hand side RHS

Example:
    
    2*x1 + 7*x2 - 1*x3 + 3*x4 +   x5 = 5
    2*x1 + 3*x2 + 4*x3 +   x4 + 7*x5 = 7 
    6*x1 + 2*x2 - 3*x3 + 2*x4 -   x5 = 2
    2*x1 +   x2 + 2*x3 -   x4 - 2*x5 = 3
    3*x1 + 4*x2 +   x3 - 2*x4 +   x5 = 3
    
This is a system of linear equation where the matrix A are the
numbers (coeff.) before the variables, the unknowns are
x1 to x5 and the RHS is all is contained after the = sign.

To solve this type of problem one can use
- Direct methods
- Iterative methods
- Methods based on optimization

The Gauss elimination algorithm belongs to the first class
It is a direct method that aims at solving: x = A^(-1) b

The way it does it is by reshaping the matrix A in a form
we (engineers and physicists) really like which is: a 
triangular matrix.

@author: Francesco
"""

# Step 1: Put the system in the augmented form

# Step 2: We need to make all the elements in the lower triangular part zero.
# We will do the elimination by column but the operations are by row.
 
import numpy as np

# Here we build the matrix A
A = np.array([[2, 7, -1, 3, 1 ],
              [2, 3,  4, 1, 7 ],
              [6, 2, -3, 2, -1],
              [2, 1, 2, -1, 2 ],
              [3, 4, 1, -2, 1 ]],float)

# Here we define the RHS vector
b = np.array([5, 7, 2, 3, 4], float)

# Order of the square matrix
n = len(b)

# Let's create the unknown matrix x
x = np.zeros(n, float)

"""
Here we set up the elimination algorithm
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
Here we solve the system by performing a backsubstitution step
"""
# we need to start from the very last element
# Here the incrementation of the loop is negative

x[n-1] = b[n-1] / A[n-1,n-1]

for i in range(n-2, -1, -1): # From the row before the last to the first row, backwards
    sumA = 0
    for j in range(i+1, n):
        
        sumA = sumA + A[i,j] * x[j]
        
    x[i] = (b[i] - sumA) / A[i,i]
   
print('The solution is: ', x)    

    

            
        

            








