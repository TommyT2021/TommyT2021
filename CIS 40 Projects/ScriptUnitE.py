from turtle import *
screen1 = Screen()
turtle1 = Turtle()
turtle1.color("Green")
turtle1.pensize(3)

#front hood
turtle1.forward(100)
turtle1.right(90)
turtle1.forward(100)

#front trunk
turtle1.left(90)
turtle1.forward(100)
turtle1.right(90)
turtle1.forward(100)

#front bumper
turtle1.right(90)
turtle1.forward(50)

#front tire
turtle1.color("Black")
turtle1.right(90)
turtle1.circle(50)

#middle bumper
turtle1.penup()
turtle1.left(90)
turtle1.forward(100)
turtle1.pendown()
turtle1.color("Green")
turtle1.forward(100)

#back tire
turtle1.color("Black")
turtle1.right(90)
turtle1.circle(50)

#back bumper
turtle1.penup()
turtle1.left(90)
turtle1.forward(100)
turtle1.pendown()
turtle1.color("Green")
turtle1.forward(50)

#back trunk
turtle1.right(90)
turtle1.forward(100)
turtle1.right(90)
turtle1.forward(100)

#back hood
turtle1.left(90)
turtle1.forward(100)
turtle1.right(90)
turtle1.forward(100)

#hide turtle
turtle1.hideturtle()
