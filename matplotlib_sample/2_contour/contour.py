import numpy as np
import matplotlib.pyplot as plt

def contour(function, x_range, y_range):
    x = np.linspace(x_range[0], x_range[1], 100)
    y = np.linspace(y_range[0], y_range[1], 100)
    X, Y = np.meshgrid(x, y)
    Z = function(X, Y)
    plt.contour(X, Y, Z)
    plt.colorbar()
    plt.show()

def color_contour(function, x_range, y_range):
    x = np.linspace(x_range[0], x_range[1], 100)
    y = np.linspace(y_range[0], y_range[1], 100)
    X, Y = np.meshgrid(x, y)
    Z = function(X, Y)
    plt.pcolor(X, Y, Z)
    plt.colorbar()
    plt.show()

def Gaussian(x, y):
    return np.exp(-x**2-y**2)

if __name__ == '__main__':
    contour(Gaussian, (-2,2), (-2,2))
    color_contour(Gaussian, (-2,2), (-2,2))