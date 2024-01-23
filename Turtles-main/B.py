import turtle
t=turtle.Turtle()
t.penup()
#draw straight line
t.goto(-30,50) #centering in the screen
t.pendown()
t.pensize(10)
t.pencolor("black")
t.right(90)
t.forward(200)
t.penup()
t.goto(-30,50) #centering in the screen
#draw first curve
t.pendown()
t.right(-90)
t.circle(-50,180)
t.penup()
t.goto(-30,-50) #centering in the screen
#draw second curve
t.pendown()
t.pendown()
t.right(180)
t.circle(-50,180)
