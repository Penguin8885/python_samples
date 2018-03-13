import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


if __name__ == '__main__':
    fig = plt.figure()
    ims = []

    x = np.arange(0, 10, 0.1)

    for a in range(50):
        y = np.sin(x - a)
        im = plt.plot(x, y, "r")
        ims.append(im)

    ani = animation.ArtistAnimation(fig, ims)
    plt.show()
