import turtle

num = [[(0, 0)] for i in range(10)]

inp = open('numbers.txt', 'r')
turtle.speed(1000)
c = str(input())


def number_read(a):
    s = inp.readline().rstrip()
    for item in s.split():
        step, turn = item.split(',')
        num[a].append((float(step), float(turn)))


for i in range(10):
    number_read(i)


def number_draw(a):
    for step, turn in num[a]:
        turtle.forward(step * 40)
        turtle.right(turn)


def number_indent(index):
    for i in index:
        number_draw(int(i))
        turtle.penup()
        turtle.forward(50)
        turtle.right(90)
        turtle.pendown()


turtle.right(90)
number_indent(c)
inp.close()

while True:
    turtle.left(1)
