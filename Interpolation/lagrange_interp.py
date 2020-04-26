"""
This program reports the algorithm for the Lagrange
Polynomial interpolation.
Remember: for a polynomial of order n, n+1 points are required.

The general form of Lagrange interpolation is:
    y(x) = Sum_(i=1)^(n+1) yi Li(x)
Where the Li are the Lagrange coefficients, calculated as:
    Li(x) = P_(j=1)^(n+1) (x - xj)/(xi - xj) with j .ne. i each time
"""
x = [0, 20, 40, 60, 80, 100]
y = [26.0, 48.6, 61.6, 71.2, 74.8, 75.2]

# we need to know the degree of the polinomial which is N points - 1
m = len(x) # the length of the array x
n = m-1    # This is the degree of the polynomial

# Now we need to start the loop of summation which is the outer one
yp = 0 # Initialization required by the summation
xp = float(input("Enter the value of xp: "))

for i in range(n+1):
    
    L = 1 # Initialization of the product needs to be 1
    
    # here we need to add the inner loop whichis the product
    
    for j in range(n+1):
        if j != i:  # we have the condition that j .ne. i
            L = L * (xp-x[j]) / (x[i] - x[j])
    
    yp = yp + y[i] * L

print('For x = %.1f, y = %.1f' % (xp, yp))
