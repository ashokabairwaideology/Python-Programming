import turtle

window = turtle.Screen()
window.bgcolor("white")

youtube_logo = turtle.Turtle()
youtube_logo.speed(1)  # Set the speed of the turtle
youtube_logo.color("red")  # Set the color of the turtle

# Create the red circle
youtube_logo.penup()
youtube_logo.goto(-50, -50)  # Move the turtle to the starting position
youtube_logo.pendown()
youtube_logo.fillcolor("red")
youtube_logo.begin_fill()
youtube_logo.circle(50)
youtube_logo.end_fill()

# Create the white triangle
youtube_logo.penup()
youtube_logo.goto(-25, -25)  # Move the turtle to the starting position
youtube_logo.pendown()
youtube_logo.color("white")
youtube_logo.fillcolor("white")
youtube_logo.begin_fill()
for _ in range(3):
    youtube_logo.forward(50)
    youtube_logo.left(120)
youtube_logo.end_fill()

window.mainloop()
