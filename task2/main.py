import math
import random
random.seed()


def met(n):
    file = open('zad2.txt', 'w')

    k=0
    w=100

    for i in range(1,n):

        x = random.random()
        y = random.random()

        if x*x + y*y <=1:
            k += 1

        p = 4 * k / i

        if i < 100:
            file.write(str(i) + ")" + str(p) + "\t\t" + str(p / math.pi) + '\n')
        elif i % w == 0:
            w = w*10
            file.write(str(i) + ")" + str(p) + "\t\t" + str(p / math.pi) + '\n')

    file.close()

if __name__ == '__main__':
    met(1000001)


# Metoda Monte Carlo i liczba pi.