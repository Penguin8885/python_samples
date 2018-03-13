import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

def plot_implicit_3d(function, range_=(-2.5,2.5)):
    '''
    function : implicit function
    range_   : common plot range of x, y, z
    '''
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    A = np.linspace(range_[0], range_[1], 100)
    B = np.linspace(range_[0], range_[1], 15)
    A1, A2 = np.meshgrid(A, A)

    for z in B:
        X, Y = A1, A2
        Z = function(X, Y, z)
        cset = ax.contour(X, Y, Z+z, [z], zdir='z')

    for y in B:
        X, Z = A1, A2
        Y = function(X, y, Z)
        cset = ax.contour(X, Y+y, Z, [y], zdir='y')

    for x in B:
        Y, Z = A1, A2
        X = function(x, Y, Z)
        cset = ax.contour(X+x, Y, Z, [x], zdir='x')

    ax.set_zlim3d(range_[0]*0.75, range_[1]*0.75)
    ax.set_xlim3d(range_[0], range_[1])
    ax.set_ylim3d(range_[0], range_[1])

    plt.show()



def function(x, y, z):
    return x*x + y*y + z*z - 3

if __name__ == '__main__':
    plot_implicit_3d(function)