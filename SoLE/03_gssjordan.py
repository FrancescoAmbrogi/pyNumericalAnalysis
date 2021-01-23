"""
This program solves a Linear Systems of Equations 
using the Gauss-Jordan Elimination method

@author: Francesco
"""

# The k loop from 0 to n-1 to index the pivot rows and eliminated columns
# Each step we will perform the partial pivoting technique in order not to have 
# a pivot element 0

import numpy as np

def gssjor(a,b): # the matrix of coeff and the vector b
    a = np.array(a, float)
    b = np.array(b, float)
    
    # define the length of the system
    n = len(b)
    
    """
    Here we start the main loop of the program
    """
    for k in range(n):
        # we start the script of the partial pivoting
        if np.fabs(a[k,k]) < 1.0e-12:
            for i in range(k+1,n):
                if np.fabs(a[i,k]) > np.fabs(a[k,k]):
                    a[[k,i]] = a[[i,k]]
                    b[[k,i]] = b[[i,k]]
                    break
        # STEP 1: division of the pivot row
        pvt = a[k,k]
        a[k] /= pvt
        b[k] /= pvt
        
        # STEP 2: elimination loop
        for i in range(n):
            if i == k or a[i,k] == 0: continue
            factor = a[i,k]
            a[i] -= factor * a[k]
            b[i] -= factor * b[k]
            
    return b, a


"""
Let's define the a matrix and b vector

"""

a = [[0,3,3,1],[6,1,3,2],[4,-3,0,1],[6,1,-6,-5]]
b = [0,-2,-7,6]   

X,A = gssjor(a, b)

print("The solution: ")
print(X)
print("The transformed matrix:")
print(A)
        
                    
