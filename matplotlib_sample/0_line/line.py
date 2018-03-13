import numpy as np
import matplotlib.pyplot as plt

def line(function, x_range):
    plt.figure()
    x = np.linspace(x_range[0], x_range[1], 100)
    y = function(x)

    plt.grid()

    plt.plot(x, y)
    plt.show()

def line2(function, x_range):
    plt.figure()
    x = np.linspace(x_range[0], x_range[1], 100)
    y = function(x)

    plt.xlim(0.001, 1)
    plt.xlabel('T[s]', fontsize=15)
    plt.xscale('log')
    plt.ylim(0,1.5)
    plt.ylabel('F[N]', fontsize=15)
    #plt.yscale('log')
    plt.grid()
    plt.tick_params(labelsize=11)

    plt.plot(x, y, label='hoge')
    plt.legend(fontsize=12)
    plt.show()


def line_with_max(function, x_range):
    x = np.linspace(x_range[0], x_range[1], 100)
    y = function(x)
    plt.plot(x, y)

    i = np.argmax(y)
    x_hat = x[i]
    y_hat = y[i]
    plt.plot(x_hat, y_hat, 'o')

    plt.grid()
    plt.show()



def gaussian(x):
    return np.exp(-x**2)

if __name__ == '__main__':
    line(gaussian, (-3,3))
    line2(gaussian, (-3,3))
    line_with_max(gaussian, (-3,3))