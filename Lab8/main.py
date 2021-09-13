from turtle import fillcolor

from vpython import *
import random

scene = canvas(width=550, height=580)

x = 4
siz = 0.5
temp = 7
dt = 0.005

box(pos=vector(x, 0, 0), size=vector(siz, temp, temp), color=color.cyan)  # prawa
box(pos=vector(-x, 0, 0), size=vector(siz, temp, temp), color=color.red)  # lewa
box(pos=vector(0, -x, 0), size=vector(temp, siz, temp), color=color.blue)  # dolna
box(pos=vector(0, x, 0), size=vector(temp, siz, temp), color=color.yellow)  # gorna
box(pos=vector(0, 0, -x), size=vector(temp, temp, siz), color=color.purple)  # tylna

L = []

for i in range(40):
    ball = sphere(pos=vector(0, 0, 0), radius=0.5, color=color.green)  # kulka
    ball.vel = vector(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1))
    L.append(ball)

# ball = sphere(pos=vector(0, 0, 0), radius=0.8, color=color.green)  # kulka
# ball.vel = vector(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1))

while True:
    rate(1000)
    for ball in L:
        ball.pos += ball.vel * dt
        if ball.pos.x + ball.radius > x:
            ball.vel.x = -ball.vel.x
            ball.color = (random.randint(1,255), random.randint(1,255), random.randint(1,255))
        if ball.pos.x - ball.radius < -x:
            ball.vel.x = -ball.vel.x
            ball.color = color.red
        if ball.pos.y + ball.radius > x:
            ball.vel.y = -ball.vel.y
            ball.color = color.yellow
        if ball.pos.y - ball.radius < -x:
            ball.vel.y = -ball.vel.y
            ball.color = color.blue
        if ball.pos.z + ball.radius > x:
            ball.vel.z = -ball.vel.z
            ball.color = color.blue
        if ball.pos.z - ball.radius < -x:
            ball.vel.z = -ball.vel.z
            ball.color = color.purple
