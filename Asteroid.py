from Rakieta import *
from math import sin, cos, pi
from time import sleep
from random import random, randint

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
    Szer = 1200
    Wys = 600
    setup(Szer,Wys)
    tracer(0)
    pencolor((0.5,0.5,0.5))
    pensize(5)
    pu()
    goto(-Szer/2+20,-Wys/2+20)
    pd()
    
    for i in range(2):
        fd(Szer-40)
        lt(90)
        fd(Wys-100)
        lt(90)

    pu()
    goto(-Szer/2+30,Wys/2-70)
    pd()
    
    pencolor((0,1,0))
    write('Vx = {}; Vy = {}'.format(rk.Vx,rk.Vy),font=('Arial',26,'normal'))

    ZU = []
    for i in range(10):
        ZU.append(Turtle('turtle'))
        ZU[-1].pu()
        ZU[-1].goto(randint(-Szer/2+320,Szer/2-20),randint(-Wys/2+20,Wys/2-100))
        ZU[-1].fillcolor((random(),random(),random()))
        ZU[-1].shapesize(randint(1,9))
        ZU[-1].o = randint(-5,5)
    rk.x = -500
    rk.y = -100
    
    GameOver = False
    while not GameOver:
       rk.Vx += rk.a*cos(rk.heading()*pi/180)
       rk.Vy += rk.a*sin(rk.heading()*pi/180)
       rk.x += rk.Vx
       rk.y += rk.Vy
       if  rk.x<= -Szer/2+20:
           rk.x = -Szer/2+20
           rk.Vx = 0
           rk.Vy = 0
       elif rk.x >= Szer/2 - 20:
            rk.x = Szer/2-20
            rk.Vx = 0
            rk.Vy = 0
       elif rk.y <= -Wys/2+20:
           rk.y = -Wys/2+20
           rk.Vx = 0
           rk.Vy = 0
       elif rk.y >= Wys/2-100:
           rk.y = Wys/2-100
           rk.Vy = 0
           rk.Vx = 0
       rk.goto(rk.x,rk.y)
       for z in ZU:
           z.lt(z.o)
           z.shapesize()[0]
           if z.distance(rk)<=5*z.shapesize()[0]:
               rk.Vx = 0
               rk.Vy = 0
               rk.x = -500
               rk.y = -100
       undo()
       write('Vx = {:4.1f}; Vy = {:4.1f}'.format(rk.Vx,rk.Vy),font=('Arial',26,'normal'))
       update()
       sleep(0.04)
main()   
