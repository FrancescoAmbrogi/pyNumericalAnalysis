"""
In sciPy there are many built in function to evaluate
the roots of a function. there are at least 4 of them:
    1. newton(f, x0)
    2. bisect(f, x1, x2)
    3. fsolve(f, x0)
    4. root(f, x0)
SciPy is a thirdy party library in python    
"""
from scipy.optimize import newton, bisect, fsolve, root

# Let us firstly define our function
def givenf(x):
    f = x**3 - 6*x**2 + 11*x - 6
    return f

# Let us apply newton directly
print(newton(givenf, 0, fprime=None, tol=1.0e-6, maxiter=100, full_output=True, disp=True))
print("\n")
# Let us use bisect
print(bisect(givenf, 0, 1.2))
print("\n")

# Let us use the function fsolve
x0 = [-1, 0, 1, 2, 3, 4]
print(fsolve(givenf, x0)) # fsolve can accept an array of initial guesses
print("\n")

# let us try the function root
print(root(givenf, 0).x)
