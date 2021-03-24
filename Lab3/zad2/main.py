import math


def calcul():

   file = open('plik.txt', 'w')

   L = [round(50 * math.sin(x*2*math.pi/50)) for x in range(51)]

   tab = []

   for i in L:
       if i < 0:
            tab.append("-"*-i)
       elif i == 0:
            tab.append('0')
       elif i > 0:
            tab.append('+' * i)



   for j in tab:
     file.write(j + '\n')

   file.close()


if __name__ == '__main__':
    calcul()


