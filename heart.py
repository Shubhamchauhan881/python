import math
from turtle import *

def hearta(k):
    return 15 * math.sin(k)**3

def heartb(k):
    return 12 * math.cos(k) - 5 * \
           math.cos(2*k) - 2 * \
           math.cos(3*k) - \
           math.cos(4*k)

speed(0)
bgcolor("black") 
color("#f73487")

penup()  # Lift the pen up before starting

for i in range(6000): 
    goto(hearta(i)*20, heartb(i)*20)
    pendown()  # Put the pen down to draw

goto(0, 0)  # This is optional if you want to end at the origin
done()