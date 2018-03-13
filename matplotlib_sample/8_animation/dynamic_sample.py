import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    fig, ax = plt.subplots(1, 1)
    x=0
    y=np.sin(x)

    while True:
        x += 0.1
        y = np.sin(x)
        ax.plot(x, y, ".r")
        plt.pause(0.01)
