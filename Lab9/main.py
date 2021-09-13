from vpython import *

G = 6.67 * 10 ** -11
M = 2 * 10 ** 30
t = 0

scene = canvas(title='zad1')

Slonce = sphere(pos=vector(0, 0, 0), radius=10 ** 10, color=color.yellow)
Merkury = sphere(pos=vector(70 * 10 ** 9, 0, 0), radius=10 ** 10, vel=vector(0, 47 * 10 ** 3, 0), color=color.white,
                 make_trail=True)
Wenus = sphere(pos=vector(110 * 10 ** 9, 0, 0), radius=10 ** 10, vel=vector(0, 35 * 10 ** 3, 0), color=color.purple,
               make_trail=True)
Ziemia = sphere(pos=vector(150 * 10 ** 9, 0, 0), radius=10 ** 10, vel=vector(0, 30 * 10 ** 3, 0), color=color.blue,
                make_trail=True)
Mars = sphere(pos=vector(250 * 10 ** 9, 0, 0), radius=10 ** 10, vel=vector(0, 24 * 10 ** 3, 0), color=color.red,
              make_trail=True)

L = [Merkury, Wenus, Ziemia, Mars]
dt = 3600

while True:
    rate(1000)
    for x in L:
        a = -G * M * x.pos / (mag(x.pos) ** 3)
        x.vel += a * dt
        x.pos = x.pos + x.vel * dt
