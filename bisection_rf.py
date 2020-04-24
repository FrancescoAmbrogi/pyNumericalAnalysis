"""
This program belongs to the root finding procedure of numerical analyisis
It is very similar to the bisection method and it is know as
Regula Falsi method.
"""
import time

t = time.time()
def bisection_rf(f,x1,x2,tol=1.0E-6,ilim=100):
    y1 = f(x1)
    y2 = f(x2) 
    xg = 0 # Initialization of the solution
    i = 0 # this is the counter of the false position
    
    if y1 == 0:
        xg = x1
        print('The root is:', xg)
    elif y2 == 0:
        xg = x2
        print('The root is:', xg)
    elif y1 * y2 > 0:
        print('No roots exists between ', x1, 'and ', x2, '\n')
    else:
        # Here we start the actual computation
        for i in range(1,ilim+1):
            xg = x2 - (x2 - x1)/(y2 - y1) * y2
            yg = f(xg)
            if abs(yg) < tol: # If the absolute value of the function at that point is less han tol
                break # we basically found the root
            elif y1 * yg < 0:
                # If there is a change in sign then
                x2 = xg
                y2 = yg
            else:
                x1 = xg
                y1 = yg
    return  xg, i

# Here we define the function we want to evaluate the root of
def givenf(x):
    f = 2*x**2 - 5*x + 3
    return f

# Here instead we call x1 and x2, the two guesses, from the user:
x1 = float(input('Enter the first guess x1: '))
x2 = float(input('Enter the second guess x2: '))

sol, nits = bisection_rf(givenf, x1, x2)

# here we print the solution on the shell:
print('Number of iterations: %d' % nits)
print('The solution found is: %0.3f' % sol)
print('The calculation took: ' + str('{0:2f}'.format(time.time() -t)) + 's\n')


