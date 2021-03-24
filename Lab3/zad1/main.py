import random
import time


spacje = 18
points = int(0)
turns = 0
losowe = (-1,1)

def start():
    print("|" + (' ' * spacje) + 'START' + (' ' * spacje) + "|")
    print("|" + (' ' * (spacje+2)) + '*' + (' ' * (spacje+2)) + "|" + str(points))



if __name__ == '__main__':
    start()

    while True:
        points = points + random.choice(losowe)
        print("|" + (' ' * (spacje + 2 + points)) + '*' + (' ' * (spacje + 2 - points)) + "|" + str(points))
        turns += 1
        time.sleep(0.03)
        if(points == 20 or points == -20):
            print("Rzucono " + str(turns) + "razy moneta")
            break