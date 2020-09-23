from random import *
import turtle


turtle.speed(3)
for i in range(1000):
    turtle.forward(randint(0, 20))
    n = random()
    if 2*n > 1:
        turtle.left(randint(0,90))
    else:
        turtle.right(randint(0,90))