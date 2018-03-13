import numpy as np
import matplotlib.pyplot as plt

def scatter(x1, y1, x2, y2):
    plt.scatter(x1, y1, c="blue")
    plt.scatter(x2, y2, c="red")
    plt.grid()
    plt.show()

if __name__ == '__main__':
    x1 = np.random.normal(-0.5, size=100)
    y1 = np.random.normal(-0.5, size=100)
    x2 = np.random.normal(1, 2, size=50)
    y2 = np.random.normal(1, 1, size=50)

    scatter(x1, y1, x2, y2)