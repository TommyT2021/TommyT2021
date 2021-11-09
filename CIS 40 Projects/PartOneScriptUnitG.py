from turtle import *
screen1 = Screen()
t1 = Turtle()
t1.hideturtle()
t1.penup()
t1.speed(100)


size = 70
upperLeftX = -280
upperLeftY = 280

def drawSquare(x,y,color):
    t1.goto(x,y)
    t1.fillcolor(color)
    t1.begin_fill()
    loop_count=0
    while loop_count < 4:
        t1.forward(size)
        t1.right(90)
        loop_count += 1
    t1.end_fill()

column=0
while column < 4:
    drawSquare(upperLeftX,upperLeftY,"Red")
    upperLeftX +=70
    drawSquare(upperLeftX,upperLeftY,"Black")
    upperLeftX +=70
    column +=1





