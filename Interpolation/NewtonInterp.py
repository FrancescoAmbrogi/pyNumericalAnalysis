"""
Here we program the Newton interpolation method
Remember, Newton rules for interpolation  reads:
    y(x) = a0 + (x - x1)a1 + (x - x1)(x - x2)a2 + ...
    
"""
import numpy as np
from FraFunctions import plot1D

x = [0.0, 1.5, 2.8, 4.4, 6.1, 8.0]
y = [0.0, 0.9, 2.5, 6.6, 7.7, 8.0]
d = {'color':'black',
     'marker': 'o'}
plot1D(x, y, **d)


# the degree of the polynomial is
n = len(x) - 1

# Now we need to construct a matrix which takes the value of y in the divided differences table
# Let us use numpy
Dy = np.zeros((n+1,n+1)) # here we have initialized the matrix
# Let as fill the first column od Dy
Dy[:,0] = y   # !!!!! Remember the index of the first column in Python is 0
for j in range(n):
    for i in range(j+1, n+1):
        # Here we write the Newton formula as it is
        Dy[i,j+1] = (Dy[i,j] - Dy[j,j])/(x[i] - x[j])

# now we need to implement the sobstitution stage
xp = float(input("Enter the xp value: "))

yp = Dy[0,0]
for i in range(n):
    xprod = 1  # For product the initialization must be 1
    for j in range(i+1):   # We know that the range starts from 0 so we need to go to i+1
        xprod = xprod * (xp - x[j])
    yp = yp + xprod * Dy[i+1, i+1]

print('For x = %.1f, y = %.1f' % (xp,yp))
        
