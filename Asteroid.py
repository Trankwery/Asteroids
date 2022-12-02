from Rakieta import *
from math import sin, cos, pi
from time import sleep

rk = Turtle()
rk.pu()
rk.tiltangle(90)
rk.shape('rk_shape')

rk.Vx = 0
rk.Vy = 0
rk.a = 0
rk.x = 0
rk.y = 0
def start():
    rk.a = 0.1
    if rk.shape() == 'rk_shape':
        rk.shape('rk_fshape')
def stop():
    rk.a=0
    rk.shape('rk_shape')
def left():
    rk.lt(5)
def right():
    rk.rt(5)
onkeypress(start,'Up')
onkeyrelease(stop,'Up')
onkeypress(left,'Left')
onkeypress(right,'Right')
listen()
bgcolor('black')
def main():
    tracer(0)
    GameOver = False
    while not GameOver:
       rk.Vx += rk.a*cos(rk.heading()*pi/180)
       rk.Vy += rk.a*sin(rk.heading()*pi/180)
       rk.x += rk.Vx
       rk.y += rk.Vy
       rk.goto(rk.x,rk.y)

       update()
       sleep(0.04)
main()   
