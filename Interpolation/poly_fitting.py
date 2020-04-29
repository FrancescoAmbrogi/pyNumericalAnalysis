"""
Curve fitting with a polynomial fit algorith
Let's say that we have a number of data points, and
we want to fit them within a curve. We need to solve a system
of liner equation, commonly called Vandermonde system
"""
import numpy as np
import Plottings as myPlot

x = np.arange(6) # It will start frm zero to 5
y = np.array([2, 8, 14, 28, 39, 62], float)

# Let us visualize the data we have
d = {'color':'black',
     'marker':'*',
     'markersize':20,
     'linestyle':' '}

myPlot.plot1D(x, y, 1, label='Data', **d)

m = len(x)
# remember the curve fitting is independent by the number of points
# So we can choose the polynomial degree we want
n = 2
A = np.zeros((n+1, n+1))   # Matrix A of the system A x = b
b = np.zeros((n+1))        # RHS of the system
xc = np.zeros((n+1))        # Coefff we want to find


for row in range(n+1):
    for col in range(n+1):
        if row == 0 and col == 0:
            A[row,col] = m # This is an exeption
            continue
        A[row,col] = np.sum(x**(row+col))
    b[row] = np.sum(x**row * y)
    
# Now we will use numpy linear algebra solve module
# For example the Gauss Elimination method
xc = np.linalg.solve(A, b)
#xc = np.linalg.solve(A, b)

print('The polynomial :\n')
print('f(x) = \t %f' %xc[0])
for i in range(1, n+1):
    print('\t %+f x^%d' % (xc[i],i))

# ---------------- Compute the fitting ----------------
xfit = np.linspace(0,5,101)
yfit = 0
for i in range(0,n+1):
    yfit = yfit + xc[i]*xfit**[i]
# -----------------------------------------------------    

c = {'color':'red'}
myPlot.plot1D(xfit, yfit, 1, label=('Fitting order: %i' %n), **c)
    
    


 
        