"""
Thi sprogram contains the code to implement the Simpson's 3/8 rule
It is very similar to the formula seen before with the difference that here
we are tachin 3 strips which means that 4 points are needed.

NB Here the number of division must be divisible by 3!!

"""

from math import sin, pi

# Here we define the function we want to integrate
f = lambda x: x * sin(x)

a = 0
b = pi / 2
n = 36 # Remember that the number of division ust be even

h = (b - a) / n
S38 = (f(a) + f(b))

for i in range(1, n, 3): # Here we only sum the odd indeces
    S38 = S38 + 3 * (f(a + i * h) + f(a + (i+1)*h))

for i in range(3, n, 3):  # Here we only sum the odd indeces
    S38 = S38 + 2 * f(a + i * h)
    
I = h * (3 / 8) * S38

print('The integral = %f' % I)
# Here the accuracy of the simpsons 3/8 rule is less than the 1/3 rule.
# Therefore the 3/8 rule is less accurate than the simpson 1/3 rule


