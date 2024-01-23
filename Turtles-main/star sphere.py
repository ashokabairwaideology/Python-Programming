import turtle as t
t1 = t.Turtle()
t1.speed(0)
t.bgcolor("black")
t1.color("white")
for j in range(12):
 for i in range(0,100,4):
     t1.circle(50+i)
 t1.lt(30)