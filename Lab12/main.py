from vpython import *
import math

L1 = 1
L2 = 1.00000000001

g1 = 9.8
g2 = 9.80000000001

t = 0
dt = 0.0001

fi = math.pi
teta = math.pi - 0.1
ball1_speed = 0
ball2_speed = 0
ball3_speed = 0
ball4_speed = 0

fi2 = math.pi
teta2 = math.pi - 0.1

# pierwsze wahadlo
ball1 = sphere(pos=vector(L1 * math.sin(fi), -L1 * math.cos(fi), 0), radius=0.1, color=color.blue)
ball2 = sphere(pos=vector(L1 * math.sin(fi) + L1 * math.sin(teta), -L1 * math.cos(fi) - L1 * math.cos(teta), 0),
               radius=0.1,
               color=color.blue)

lin1 = cylinder(pos=vector(0, 0, 0), axis=ball1.pos, radius=0.01)
lin2 = cylinder(pos=ball1.pos, axis=ball2.pos - ball1.pos, radius=0.01)

# drugie wahadlo
ball3 = sphere(pos=vector(L2 * math.sin(fi), -L2 * math.cos(fi), 0), radius=0.1, color=color.red)
ball4 = sphere(pos=vector(L2 * math.sin(fi) + L2 * math.sin(teta), -L2 * math.cos(fi) - L2 * math.cos(teta), 0),
               radius=0.1,
               color=color.red)

lin3 = cylinder(pos=vector(0, 0, 0), axis=ball3.pos, radius=0.01)
lin4 = cylinder(pos=ball3.pos, axis=ball4.pos - ball3.pos, radius=0.01)

while t < 1000:
    rate(5000)

    # pierwszy uklad niebieski
    fi_move = (-g1 / L1 * (2 * math.sin(fi) - math.sin(teta) * math.cos(fi - teta)) - 1 / 2 * (
            ball1_speed ** 2) * math.sin(2 * fi - 2 * teta) - ball2_speed * sin(fi - teta)) / (
                      1 + (math.sin(fi - teta)) ** 2)
    teta_move = (-g1 / L1 * (2 * math.sin(teta) - - 2 * math.sin(fi) * math.cos(fi - teta)) + 1 / 2 * (
            ball2_speed ** 2) * math.sin(2 * fi - 2 * teta) + 2 * (ball1_speed ** 2) * sin(fi - teta)) / (
                        1 + (math.sin(fi - teta)) ** 2)

    ball1_speed = ball1_speed + fi_move * dt
    ball2_speed = ball2_speed + teta_move * dt

    fi = fi + ball1_speed * dt
    teta = teta + ball2_speed * dt

    ball1.pos = vector(L1 * math.sin(fi), -L1 * math.cos(fi), 0)
    ball2.pos = vector(L1 * math.sin(fi) + L1 * math.sin(teta), -L1 * math.cos(fi) - L2 * math.cos(teta), 0)

    lin1.axis = ball1.pos
    lin2.pos = ball1.pos
    lin2.axis = ball2.pos - ball1.pos

    # drugi wahadlo czerwone

    fi_move2 = (-g1 / L2 * (2 * math.sin(fi2) - math.sin(teta2) * math.cos(fi2 - teta2)) - 1 / 2 * (
            ball3_speed ** 2) * math.sin(2 * fi2 - 2 * teta2) - ball4_speed * sin(fi2 - teta2)) / (
                       1 + (math.sin(fi2 - teta2)) ** 2)
    teta_move2 = (-g1 / L2 * (2 * math.sin(teta2) - - 2 * math.sin(fi2) * math.cos(fi2 - teta2)) + 1 / 2 * (
            ball4_speed ** 2) * math.sin(2 * fi2 - 2 * teta2) + 2 * (ball3_speed ** 2) * sin(fi2 - teta2)) / (
                         1 + (math.sin(fi2 - teta2)) ** 2)

    ball3_speed = ball3_speed + fi_move2 * dt
    ball4_speed = ball4_speed + teta_move2 * dt

    fi2 = fi2 + ball1_speed * dt
    teta2 = teta2 + ball2_speed * dt

    ball3.pos = vector(L2 * math.sin(fi2), -L2 * math.cos(fi2), 0)
    ball4.pos = vector(L2 * math.sin(fi2) + L2 * math.sin(teta2), -L2 * math.cos(fi2) - L2 * math.cos(teta2), 0)

    lin3.axis = ball3.pos
    lin4.pos = ball3.pos
    lin4.axis = ball4.pos - ball3.pos

    t = t + dt
