import turtle

s = turtle.Screen().bgcolor("yellow")
t = turtle.Turtle()
t.speed(3000)
t.width(20)

def curve():
    for i in range (200):
        t.right(1)
        t.forward(1)

def heart():
    t.color("black","grey")
    t.begin_fill()
    t.left(140)
    t.forward(113)
    curve()
    t.left(120)
    curve()
    t.forward(112)
    t.end_fill()

heart()
t.pencolor("black")
t.penup()
t.goto(0,170)
t.pendown()

for broken in range (3):
    t.left(75)
    t.forward(40)
    t.right(65)
    t.forward(45)

turtle.done()
