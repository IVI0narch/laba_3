from random import *
import turtle
import math


number_of_turtles = 2
steps_of_time_number = 10000


pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
vx = [0] * number_of_turtles
vy = [0] * number_of_turtles
x_coord = [0] * number_of_turtles
y_coord = [0] * number_of_turtles
i = 0
for unit in pool:
    unit.penup()
    vx[i] = randint(1, 50)
    vy[i] = randint(1, 50)
    x_coord[i] = randint(-300, 300)
    y_coord[i] = randint(-300, 300)
    unit.goto(x_coord[i], y_coord[i])
    i += 1

'''
def respeed(vx1, vy1, vx2, vy2, delta_x, delta_y):
    angle_alpha = math.atan(delta_x / delta_y)
    angle_beta_1 = math.atan(vx1 / vy1)
    angle_beta_2 = math.atan(vx2 / vy2)
    gamma1 = angle_alpha - angle_beta_1
    v1_n = math.sqrt(vx1 ** 2 + vy1 ** 2) * math.cos(gamma1)
    gamma2 = angle_alpha - angle_beta_2
    v2_n = math.sqrt(vx2 ** 2 + vy2 ** 2) * math.cos(gamma2)
    v1_n, v2_n = v2_n, v1_n
    v1 = v1_n / math.cos(gamma1)
    vx1 = v1 * math.cos(angle_alpha)
    vy1 = v1 * math.sin(angle_alpha)
    v2 = v2_n / math.cos(gamma1)
    vx2 = v2 * math.cos(angle_alpha)
    vy2 = v2 * math.sin(angle_alpha)
    return vx1, vy1, vx2, vy2
'''
for i in range(steps_of_time_number):
    for j in range(number_of_turtles):
        x = x_coord[j]
        y = y_coord[j]
        if abs(y) >= 300:
            vy[j] = -vy[j]
        elif abs(x) >= 300:
            vx[j] = -vx[j]
        '''проверка на столкновение с другой черепахой
        for k in range(number_of_turtles):
            delta_x = x - x_coord[k]
            delta_y = y - y_coord[k]
            if (delta_x != 0) and math.sqrt((delta_x ** 2 + delta_y ** 2)) <= 20:
                vx[j], vy[j], vx[k], vy[k] = respeed(vx[j], vy[j], vx[k], vy[k], delta_x, delta_y)
                break'''
        x += vx[j] / 10
        y += vy[j] / 10
        pool[j].goto(x, y)
        x_coord[j] = x
        y_coord[j] = y