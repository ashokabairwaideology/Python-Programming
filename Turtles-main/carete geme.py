from turtle import *
state = {'turn': 0}
def spinner():
    clear()
    angle = state['turn']/100
    right(angle)
    forward(100)
    dot(120, 'red')
    back(100)
    right(90)
    forward(100)
    dot(120, 'green')
    back(100)
    right(90)
    forward(100)
    dot(120, 'yellow')
    back(100)
    right(90)
    forward(100)
    dot(120, 'blue')
    back(100)
    right(90)
    update()
def animate():
    if state['turn']>0:
        state['turn']-=1

    spinner()
    ontimer(animate, 1000)
def flick():
    state['turn']+=10

setup(720, 720, 870, 0)
hideturtle()
tracer(False)
width(10)
onkey(flick, 'space')
listen()
animate()
done()




#press spacebar turn spped fast
