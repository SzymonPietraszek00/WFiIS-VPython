import numpy as np
import matplotlib.pyplot as plt


def zad1():
    plt.style.use('classic')
    A = (0, 0)
    B = (1, 0)
    C = (0.5, 1)
    D = []
    E = []

    x = np.random.uniform(0, 1)
    y = np.random.uniform(0, 1)

    for i in range(10 ** 6):
        pkt = np.random.randint(3)

        if pkt == 0:
            wybrany = A
        elif pkt == 1:
            wybrany = B
        else:
            wybrany = C

        D.append((x + wybrany[0]) / 2)
        E.append((y + wybrany[1]) / 2)
        x = (x + wybrany[0]) / 2
        y = (y + wybrany[1]) / 2

    plt.plot(D, E, ',')
    plt.show()


if __name__ == '__main__':
    zad1()
