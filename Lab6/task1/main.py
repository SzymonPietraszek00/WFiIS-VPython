import numpy as np
import matplotlib.pyplot as plt
import random

x_zero = [0.0]
y_zero = [0.0]
num = 0

def goo():
    for i in range(1, 10 ** 6 + 1):
        temp = random.uniform(0, 100)
        if temp < 7.0:
            # prawdopodobienstwo 0.07
            x = 0.2 * x_zero[i - 1] - 0.26 * y_zero[i - 1]
            y = 0.23 * x_zero[i - 1] + 0.22 * y_zero[i - 1] + 1.6
        elif temp < 14.0:
            # prawdopodobienstwo 0.07
            x = -0.15 * x_zero[i - 1] + 0.28 * y_zero[i - 1]
            y = 0.26 * x_zero[i - 1] + 0.24 * y_zero[i - 1] + 0.44
        elif temp < 99.0:
            # prawdopodobienstwo 0.85
            x = 0.85 * x_zero[i - 1] + 0.04 * y_zero[i - 1]
            y = -0.04 * x_zero[i - 1] + 0.85 * y_zero[i - 1] + 1.6
        else:
            # prawdopodobienstwo 0.01
            x = 0.0
            y = 0.16 * y_zero[i - 1]
        x_zero.append(x)
        y_zero.append(y)


if __name__ == '__main__':
    goo()
    plt.plot(x_zero, y_zero, ',', color='lightgreen')

    plt.savefig('myfig.png', format='png', bbox_inches='tight', pad_inches=0.05, dpi=300)


    plt.show()
