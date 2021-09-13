from vpython import *
import random

N = 2
t = 0
m = 1
M = 100
scene = canvas(width=800, height=600)

def move(ball):
    ball.pos+=ball.vel*dt

vz = 0

ball1 = sphere(pos=vector(-2, 0, 0), radius=0.1, vel=vector(random.uniform(-1, 1), random.uniform(-1, 1), vz),
               color=color.red)

ball2 = sphere(pos=vector(2, 0, 0), vel=vector(random.uniform(-1, 1), random.uniform(-1, 1), vz), radius=0.1,
               color=color.red)

ball3 = sphere(pos=vector(1, 0, 0), radius=0.2, vel=vector(1, 0.5, 0), color=color.red, make_trail=True)

c1 = cylinder(pos=vector(2.5, -2.5, 0), axis=vector(0, 5, 0), radius=0.1)
c2 = cylinder(pos=vector(-2.5, -2.5, 0), axis=vector(0, 5, 0), radius=0.1)
c3 = cylinder(pos=vector(-2.5, 2.5, 0), axis=vector(5, 0, 0), radius=0.1)
c4 = cylinder(pos=vector(-2.5, -2.5, 0), axis=vector(5, 0, 0), radius=0.1)

dt = 0.005

while True:
    rate(1000)
    ball1.pos = ball1.pos + ball1.vel * dt
    ball2.pos = ball2.pos + ball2.vel * dt
    ball3.pos = ball3.pos + ball3.vel * dt

    if ball1.pos.x + ball1.radius > 2.5 or ball1.pos.x - ball1.radius < -2.5:
        ball1.vel.x = -ball1.vel.x
    if ball2.pos.x + ball2.radius > 2.5 or ball2.pos.x - ball2.radius < -2.5:
        ball2.vel.x = -ball2.vel.x
    if ball3.pos.x + ball3.radius > 2.5 or ball3.pos.x - ball3.radius < -2.5:
        ball3.vel.x = -ball3.vel.x

    if ball1.pos.y + ball1.radius > 2.5 or ball1.pos.y - ball1.radius < -2.5:
        ball1.vel.y = -ball1.vel.y
    if ball2.pos.y + ball2.radius > 2.5 or ball2.pos.y - ball2.radius < -2.5:
        ball2.vel.y = -ball2.vel.y
    if ball3.pos.y + ball3.radius > 2.5 or ball3.pos.y - ball3.radius < -2.5:
        ball3.vel.y = -ball3.vel.y



    r1 = ball1.pos + ball1.vel*dt
    r2 = ball2.pos+ball2.vel*dt

    if mag(r1-r2) < (ball1.radius+ball2.radius):
        a=mag2(ball1.vel-ball2.vel)
        b=dot(-2*(r1-r2),(ball1.vel-ball2.vel))
        c=mag2(r1-r2)-(ball1.radius+ball2.radius)**2
        delta=b**2-4*a*c
    if a!=0 and delta>=0:
        dtp=(-b+delta**0.5)/(2*a)
        ball1.pos=ball1.pos-ball1.vel*dtp
        ball2.pos=ball2.pos-ball2.vel*dtp
        b1vel=ball1.vel

        ball1.vel=ball1.vel-2*m/(m+m)*dot(ball1.vel-ball2.vel, norm(r1-r2) * norm(r1-r2))
        ball2.vel=ball1.vel+2*m/(m+m)*dot(b1vel-ball2.vel, norm(r1-r2) * norm(r1-r2))
        ball1.pos=ball1.pos+ball1.vel*dtp
        ball2.pos=ball2.pos+ball2.vel*dtp


    move(ball1)
    move(ball2)
    t += dt
