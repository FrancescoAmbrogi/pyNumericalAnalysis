"""
In this file we define useful functions
"""
from matplotlib import pyplot as plt

# the first function is a 2D plot function
def plot2D(x , y, fname=None, xlabel=None, ylabel=None ,**kwargs):   
    "This function will build a 2D plot and it will save it if fname is not true."
    plt.figure(101, figsize=(22,14), dpi=100)
    plt.plot(x, y, **kwargs)
    plt.grid(True)
    plt.rc('xtick', labelsize=32) 
    plt.rc('ytick', labelsize=32)
    
    if xlabel and ylabel:
        plt.xlabel(xlabel, fontsize=32)
        plt.ylabel(ylabel, fontsize=32)
    else:
        plt.xlabel('x', fontsize=32)
        plt.ylabel('y', fontsize=32)
        
    if fname:
        plt.savefig(fname)
    else:
        plt.show()
