"""
With this program we start the interpolation section
Let us say that we have a table of points:
    x = 0 20 40 60 80 100
    y = 26.0 48.6 61.6 71.2 74.8 75.2
These maybe represents pressure or temperature changing
"""
from matplotlib import pyplot as plt
from FraFunctions import plot2D

time = [0, 20, 40, 60, 80, 100]
temp = [26.0, 48.6, 61.6, 71.2, 74.8, 75.2]
temp2 = [30.0, 15.6, 58.6, 77.2, 82.8, 64.2]

d = {'color':'black',
     'marker':'s'}
c = {'color':'magenta',
     'marker':'d'}

plot2D(time, temp, **d)
plot2D(time, temp2, xlabel='Time', ylabel='Temperature', **c)


# In the linear interpolation method assumed that the behavior
# Of the function between any two points is represented by 
# a stright line. Ex: we want the temperature at 75 sec

def lin_interp(xp, x, y):
    for i, xi in enumerate(x): # This statement returns two things
        # we want to be sure the value of x is in the right position
        if xp < xi:
            # here we need the index, an we can use some pythonic method
            t =  y[i-1] + (y[i] - y[i-1])/(x[i] - x[i-1])*(xp - x[i-1])
            return t
    else:
        print("Warning: value xp out of range!!")

xp = float(input("Enter the point you want to evaluate the function at: "))
print("The themperature at: ", xp, " is: ", lin_interp(xp, time, temp), " C")
     
plt.show() 