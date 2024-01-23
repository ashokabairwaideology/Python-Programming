import turtle as t
t1 = t.Turtle()
t1.speed(0)
t.bgcolor("black")
c = ["violet","indigo","blue","green","yellow","orange","red"]
#VIBGYOR
for i in range(0,100,2):
 t1.color(c[i%7])
 t1.circle(50+i)