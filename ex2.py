import turtle


def num_0(x, y):
    coords = [(0 + x, 0 + y), (40 + x, 0 + y),
              (0 + x, 40 + y), (40 + x, 40 + y),
              (0 + x, 80 + y), (40 + x, 80 + y)]
    turtle.pendown()
    turtle.goto(coords[0])
    turtle.goto(coords[1])
    turtle.goto(coords[5])
    turtle.goto(coords[4])
    turtle.penup()
    turtle.goto(x + 60, 80)
    turtle.pendown()
    x += 60
    return x, y


def num_1(x, y):
    coords = [(0 + x, 0 + y), (40 + x, 0 + y),
              (0 + x, 40 + y), (40 + x, 40 + y),
              (0 + x, 80 + y), (40 + x, 80 + y)]
    turtle.penup()
    turtle.goto(coords[2])
    turtle.pendown()
    turtle.goto(coords[5])
    turtle.goto(coords[1])
    turtle.goto(coords[5])
    turtle.penup()
    turtle.goto(x + 60, 80)
    turtle.pendown()
    x += 60
    return x, y


def num_2(x, y):
    coords = [(0 + x, 0 + y), (40 + x, 0 + y),
              (0 + x, 40 + y), (40 + x, 40 + y),
              (0 + x, 80 + y), (40 + x, 80 + y)]
    turtle.goto(coords[5])
    turtle.goto(coords[3])
    turtle.goto(coords[0])
    turtle.goto(coords[1])
    turtle.penup()
    turtle.goto(x + 60, 80)
    turtle.pendown()
    x += 60
    return x, y


def num_3(x, y):
    coords = [(0 + x, 0 + y), (40 + x, 0 + y),
              (0 + x, 40 + y), (40 + x, 40 + y),
              (0 + x, 80 + y), (40 + x, 80 + y)]
    turtle.goto(coords[5])
    turtle.goto(coords[2])
    turtle.goto(coords[3])
    turtle.goto(coords[0])
    turtle.penup()
    turtle.goto(x + 60, 80)
    turtle.pendown()
    x += 60
    return x, y


def num_4(x, y):
    coords = [(0 + x, 0 + y), (40 + x, 0 + y),
              (0 + x, 40 + y), (40 + x, 40 + y),
              (0 + x, 80 + y), (40 + x, 80 + y)]
    turtle.goto(coords[2])
    turtle.goto(coords[3])
    turtle.goto(coords[5])
    turtle.goto(coords[1])
    turtle.penup()
    turtle.goto(x + 60, 80)
    turtle.pendown()
    x += 60
    return x, y


def num_5(x, y):
    coords = [(0 + x, 0 + y), (40 + x, 0 + y),
              (0 + x, 40 + y), (40 + x, 40 + y),
              (0 + x, 80 + y), (40 + x, 80 + y)]
    turtle.goto(coords[5])
    turtle.goto(coords[4])
    turtle.goto(coords[2])
    turtle.goto(coords[3])
    turtle.goto(coords[1])
    turtle.goto(coords[0])
    turtle.penup()
    turtle.goto(x + 60, 80)
    turtle.pendown()
    x += 60
    return x, y


def num_6(x, y):
    coords = [(0 + x, 0 + y), (40 + x, 0 + y),
              (0 + x, 40 + y), (40 + x, 40 + y),
              (0 + x, 80 + y), (40 + x, 80 + y)]
    turtle.penup()
    turtle.goto(coords[5])
    turtle.pendown()
    turtle.goto(coords[2])
    turtle.goto(coords[3])
    turtle.goto(coords[1])
    turtle.goto(coords[0])
    turtle.goto(coords[2])
    turtle.penup()
    turtle.goto(x + 60, 80)
    turtle.pendown()
    x += 60
    return x, y


def num_7(x, y):
    coords = [(0 + x, 0 + y), (40 + x, 0 + y),
              (0 + x, 40 + y), (40 + x, 40 + y),
              (0 + x, 80 + y), (40 + x, 80 + y)]
    turtle.goto(coords[5])
    turtle.goto(coords[2])
    turtle.goto(coords[0])
    turtle.penup()
    turtle.goto(x + 60, 80)
    turtle.pendown()
    x += 60
    return x, y


def num_8(x, y):
    coords = [(0 + x, 0 + y), (40 + x, 0 + y),
              (0 + x, 40 + y), (40 + x, 40 + y),
              (0 + x, 80 + y), (40 + x, 80 + y)]
    turtle.penup()
    turtle.goto(coords[2])
    turtle.pendown()
    turtle.goto(coords[3])
    turtle.goto(coords[1])
    turtle.goto(coords[0])
    turtle.goto(coords[4])
    turtle.goto(coords[5])
    turtle.goto(coords[3])
    turtle.penup()
    turtle.goto(x + 60, 80)
    turtle.pendown()
    x += 60
    return x, y


def num_9(x, y):
    coords = [(0 + x, 0 + y), (40 + x, 0 + y),
              (0 + x, 40 + y), (40 + x, 40 + y),
              (0 + x, 80 + y), (40 + x, 80 + y)]
    turtle.penup()
    turtle.goto(coords[3])
    turtle.pendown()
    turtle.goto(coords[2])
    turtle.goto(coords[4])
    turtle.goto(coords[5])
    turtle.goto(coords[3])
    turtle.goto(coords[0])
    turtle.penup()
    turtle.goto(x + 60, 80)
    turtle.pendown()
    x += 60
    return x, y


turtle.speed(1)
x = 0
y = 0
x, y = num_1(x, y)
x, y = num_4(x, y)
x, y = num_1(x, y)
x, y = num_7(x, y)
x, y = num_0(x, y)
x, y = num_0(x, y)
