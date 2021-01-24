"""
In this code we will see ho to perform a double integration using 
Simpson's rule
"""

# Let us solve this integral

# I = \int_{-1}^{1} \int_{1}^{2} (x^2y + xy^2) dx dy

# Let us first define our function
f = lambda x,y: x**2 * y + x * y**2

#Define the upper and lower limit of each integrals
ax = 1
bx = 2

ay = -1
by = 1

# let's also define the number of division for each integral
nx = 2
ny = 2

hx = (bx - ax)/nx
hy = (by - ay)/ny

# Now we will start the integration
S2 = 0 # summation variable

# outer integration
for i in range(0, ny+1):  # remember the for loop will not include the last value
    if i == 0 or i == ny:
        p = 1   # this is the factor of the first term f0 and fn
    elif i % 2 == 1:    # if i is an odd number
        p = 4
    else:
        p = 2
            
    # inner integration
    
    for j in range(0, nx+1):
        if j == 0 or j == nx:
            q = 1   # this is the factor of the first term f0 and fn
        elif j % 2 == 1:    # if j is an odd number
            q = 4
        else:
            q = 2
            
        # the factor of each term will be multiplied together    
        S2 = S2 + p*q * f(ax + j*hx, ay + i*hy)
        
Int = hx*hy / 9 * S2
print('Integral = %f' % Int)
