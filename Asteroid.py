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

def losowanie(ZU,Szer,Wys):
    if len(ZU) == 5:
        
        for j in range(5):
            Wolno = False
            while  not Wolno:
                ZU[j].goto(randint(-Szer/2+320,Szer/2-20), randint(-Wys/2+20,Wys/2-100))
                Wolno = True
                for i in range(5):
                    if i != j:
                        if ZU[ i ].distance(ZU[ j ]) <= (20*ZU[j].shapesize()[0] + 20*ZU[i].shapesize()[0]):
                            Wolno = False
            ZU[j].fillcolor((random(),random(),random()))
            ZU[j].shapesize(randint(1,5))
            ZU[j].o = randint(-5,5)
    else:
        for i in range(5):
            ZU.append(Turtle('turtle'))
            ZU[-1].pu()
            Wolno = False
            while  not Wolno:
                ZU[-1].goto(randint(-Szer/2+320,Szer/2-20), randint(-Wys/2+20,Wys/2-100))
                Wolno = True
                for i in ZU[:-1]:
                    if ZU[-1].distance(i) <= (20*i.shapesize()[0] + 20*ZU[-1].shapesize()[0]):
                        Wolno = False
            ZU[-1].fillcolor((random(),random(),random()))
            ZU[-1].shapesize(randint(1,5))
            ZU[-1].o = randint(-5,5)
    return ZU

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

    Exit = Turtle()
    Exit.shape('square')
    Exit.color('green','green')
    Exit.pu()
    Exit.shapesize(3)
    Exit.goto(Szer/2,150)
    
    ZU = []
    ZU = losowanie(ZU,Szer,Wys)
    rk.x = -500
    rk.y = -100
    
    czas = 5.5 # sekundy na poziom

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
           if z.distance(rk)<= 20*z.shapesize()[0]:
               rk.Vx = 0
               rk.Vy = 0
               rk.x = -500
               rk.y = -100
       if rk.distance(Exit) <= 30:
            undo()
            write('Nowy Poziom',font=('Arial',26,'normal'))
       else:
           undo()
           write('Vx = {:4.1f}; Vy = {:4.1f}; czas: {:4.1f}'.format(rk.Vx,rk.Vy, czas),font=('Arial',26,'normal'))
       update()
       sleep(0.04)
       czas = czas - 0.04
       
       if czas < 0 :
            ZU = losowanie(ZU,Szer,Wys)
            rk.x = -500
            rk.y = -100
            rk.Vx = 0
            rk.Vy = 0
            czas = 30.5 # sekundy na poziom

       
main()   
