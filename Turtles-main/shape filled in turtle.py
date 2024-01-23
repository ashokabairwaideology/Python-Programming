# draw color-filled square in turtle

import turtle

# creating turtle pen
t = turtle.Turtle()

# taking input for the side of the square
s = int(input("Enter the length of the side of the square: "))

# taking the input for the color
col = input("Enter the color name or hex value of color(# RRGGBB): ")

# set the fillcolor
t.fillcolor(col)

# start the filling color
t.begin_fill()

# drawing the square of side s
for _ in range(4):
    t.forward(s)
t.right(90)

# ending the filling of the color
t.end_fill()






# draw color filled triangle in turtle

import turtle

# creating turtle pen
t = turtle.Turtle()

# taking input for the side of the triangle
s = int(input("Enter the length of the side of the triangle: "))

# taking the input for the color
col = input("Enter the color name or hex value of color(# RRGGBB): ")

# set the fillcolor
t.fillcolor(col)

# start the filling color
t.begin_fill()

# drawing the triangle of side s
for _ in range(3):
    t.forward(s)
t.right(-120)

# ending the filling of the color
t.end_fill()












# draw color-filled hexagon in turtle

import turtle

# creating turtle pen
t = turtle.Turtle()

# taking input for the side of the hexagon
s = int(input("Enter the length of the side of the hexagon: "))

# taking the input for the color
col = input("Enter the color name or hex value of color(# RRGGBB): ")

# set the fillcolor
t.fillcolor(col)

# start the filling color
t.begin_fill()

# drawing the hexagon of side s
for _ in range(6):
    t.forward(s)
t.right(-60)

# ending the filling of the color
t.end_fill()






# draw color filled star in turtle

import turtle

# creating turtle pen
t = turtle.Turtle()

# taking input for the side of the star
s = int(input("Enter the length of the side of the star: "))

# taking the input for the color
col = input("Enter the color name or hex value of color(# RRGGBB): ")

# set the fillcolor
t.fillcolor(col)

# start the filling color
t.begin_fill()

# drawing the star of side s
for _ in range(5):
    t.forward(s)
t.right(144)

# ending the filling of color
t.end_fill()



# draw color filled circle in turtle

import turtle

# creating turtle pen
t = turtle.Turtle()

# taking input for the radius of the circle
r = int(input("Enter the radius of the circle: "))

# taking the input for the color
col = input("Enter the color name or hex value of color(# RRGGBB): ")

# set the fillcolor
t.fillcolor(col)

# start the filling color
t.begin_fill()

# drawing the circle of radius r
t.circle(r)

# ending the filling of the color
t.end_fill()

