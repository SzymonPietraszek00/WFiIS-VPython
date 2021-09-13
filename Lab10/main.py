from vpython import *

dt = 0.001
k = 1
m = 1
t = 0

scene = canvas(width=750, height=750, range=4)

wallL = box(pos=vector(-4, 0, 0), size=vector(0.5, 6, 0.5))
wallR = box(pos=vector(4, 0, 0), size=vector(0.5, 6, 0.5))

bal1 = sphere(pos=vector(-2, 0, 0), radius=0.5, vel=vector(0, 0, 0), color=color.blue)
bal2 = sphere(pos=vector(0, 2, 0), radius=0.5, vel=vector(0, 0, 0), color=color.blue)
bal3 = sphere(pos=vector(2, 0, 0), radius=0.5, vel=vector(0, 0, 0), color=color.blue)

Balls = [bal1, bal2, bal3]

he1 = helix(pos=wallL.pos, axis=bal1.pos - wallL.pos, radius=0.2, coils=10, thickness=0.05, color=color.green)
he2 = helix(pos=bal1.pos, axis=bal2.pos - bal1.pos, radius=0.2, coils=10, thickness=0.05, color=color.green)
he3 = helix(pos=bal2.pos, axis=bal3.pos - bal2.pos, radius=0.2, coils=10, thickness=0.05, color=color.green)
he4 = helix(pos=bal3.pos, axis=wallR.pos - bal3.pos, radius=0.2, coils=10, thickness=0.05, color=color.green)

F = [0, 0, 0]

while True:
    rate(1000)


    for i in range(3):
        if i == 0:
            F[0] = (k * (bal2.pos - 2 * bal1.pos))
        if i == 1:
            F[1] = (k * (bal1.pos + bal3.pos - 2 * bal2.pos))
        else:
            F[2] = (k * (bal2.pos - 2 * bal3.pos))

        Balls[i].vel = Balls[i].vel + F[i] * dt
        Balls[i].pos = Balls[i].pos + Balls[i].vel * dt

    he1.axis = bal1.pos - wallL.pos

    he2.axis = bal2.pos - bal1.pos
    he2.pos = bal1.pos

    he3.axis = bal3.pos - bal2.pos
    he3.pos = bal2.pos

    he4.axis = wallR.pos - bal3.pos
    he4.pos = bal3.pos
