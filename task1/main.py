import math


def Leibnitz(n):
    file = open('plikwynik.txt', 'w')

    w = 100
    l = 1
    m = 1
    x = 0
    for i in range(1,n):
        x = (x + l/m)
        if(m>0):
            m = (m+2)*(-1)
        else:
            m = (m-2) * (-1)

        if i < 100:
            file.write(str(i) + ")" + str(4*x) + "\t\t" + str(4*x/math.pi) + "\n")
        elif i % w == 0:
            w = w*10
            file.write(str(i) + ")" + str(4 * x) + "\t\t" + str(4 * x / math.pi) + "\n")

    file.close()

if __name__ == '__main__':
    Leibnitz(10000001)

# Szereg Leibnitza.

# pi = 4*(1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ...)

# gdzie pi to jest liczba pi.
# Proszę napisać program, który liczy pi w ten sposób. Program powinien tworzyć plik tekstowy w którem ma być wypisane:

# 1) wyliczona liczba z szeregu,  stosunek wyliczonej liczby do dokladnej liczby pi
# 2)
# 3)
# 4)
# .
# .
# 99)
# 100)
# 10**3)
# 10**4)
# 10**5)
# 10**6)
# 10**7)

# Np. wiersz 2) oznacza, że bierzemy 2 wyrazy szeregu Leibnitza tzn. 4*(1 - 1/3).
# Wiersz 86) oznacza, że bierzemy 86 wyrazów szeregu Leibnitza itd.
# Wypisujemy dla wszystkich liczb całkowitych od 1 do 100 a potem skok na 10**3, 10**4, 10**5, 10**6, 10**7.
# Liczby wskazujące wiersze 1), 2) itd. mają być widoczne w pliku.
# Im więcej wyrazów szeregu Leibnitza tym lepiej powinniśmy przybliżyć liczbę pi i stosunek powinien być bliższy jedynki.
