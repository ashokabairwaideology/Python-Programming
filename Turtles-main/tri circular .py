import turtle as t
t1 = t.Turtle()
t1.speed(0)
t.bgcolor("black")
t1.color("white")
c = ["violet","indigo","blue","green","yellow","orange","red"]
#VIBGYOR
for j in range(12):
 for i in range(0,90,3):
     t1.circle(50+i)
 t1.lt(30)
 t1.color(c[j%7])
 
 