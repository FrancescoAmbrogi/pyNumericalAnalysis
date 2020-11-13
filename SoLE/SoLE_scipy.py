"""
Linear systems solved using Numpy and Scipy

@author: Francesco

"""
import numpy as np
import scipy as sp

A = np.array([[4, 1, 2, -1 ],
              [3, 6, -1, 2 ],
              [2, -1, 5, -3],
              [4, 1, -3, -8 ]],float)

b = np.array([2, -1, 3, 2], float)

x = np.linalg.solve(A,b)

x1 = np.dot(np.linalg.inv(A), b)



