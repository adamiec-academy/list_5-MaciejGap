from turtle import *

def painting():
    data = []
    for line in open("dots.txt", encoding="utf-8"):
        x = line.strip().split()
        p = (int(x[0]), int(x[1]))
        data.append(p)
    penup()
    x, y = data[0]
    goto(x // 2 - 150, -y // 2 + 150)
    pendown()
    for dot in data:
        x, y = dot
        goto(x//2 - 150, -y//2 + 150)
    exitonclick()

