import turtle
def star():
    sidelength = int(input("Please input sidelength："))
    turtle.begin_fill()
    i = 1
    for i in range(5):
        turtle.forward(sidelength)
        turtle.right(144)
        i += 1
turtle.end_fill()
star()