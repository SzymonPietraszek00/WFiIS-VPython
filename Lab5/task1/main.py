import numpy as np

plik = open('wynik.txt', 'w')



def create_room(num):
    matched_birthday = 0

    for i in range(1000):
        a = np.random.randint(1, 366, num)
        b = a[:, np.newaxis]

        if (np.sum(a == b) - num) > 0:
            matched_birthday = matched_birthday + 1

        if (matched_birthday / 1000) > 0.5 :
            s = matched_birthday


    plik.write(str(num) + ')\t' + str(matched_birthday / 1000) + '\n')


if __name__ == '__main__':

    for i in range(1, 367):
        create_room(i)


