from turtle import *
import random 
screen1 = Screen()
t1 = Turtle()
t1.shape("triangle")
t1.hideturtle()

aScore = 0
bScore = 0
aMinDist = 300
bMinDist = 300
aColor = "lime"
bColor = "silver"

def drawCircle(radius,color):
    t1.home()
    t1.penup()
    t1.goto(0,radius)
    t1.pendown()
    t1.color(color)
    t1.seth(180)
    t1.fillcolor(color)
    t1.begin_fill()
    t1.circle(radius)
    t1.end_fill()
    t1.penup()
    t1.home()

drawCircle(300,"Blue")
drawCircle(200,"Red")
drawCircle(100,"Yellow")

def arrowShot(color):
    t1.penup()
    t1.home()
    t1.color(color)
    distance = random.randint(0,300)
    t1.setheading(random.randint(0,359))
    t1.forward(distance)
    t1.seth(90)
    t1.stamp()
    return distance

def getScore(distance):
    score = 0
    if distance <= 100:
        score += 10
    elif 101 <= distance <=200:
        score +=7
    elif 201 <= distance <=300:
        score +=5
    else:
        score +=0
    return score

#ashots
adist = arrowShot(aColor)
aScore += getScore(adist)
if adist<aMinDist:
    aMinDist = adist
    
adist = arrowShot(aColor)
aScore += getScore(adist)
if adist<aMinDist:
    aMinDist = adist

adist = arrowShot(aColor)
aScore += getScore(adist)
if adist<aMinDist:
    aMinDist = adist

#bshots
bdist = arrowShot(bColor)
bScore += getScore(bdist)
if bdist<bMinDist:
    bMinDist = bdist

bdist = arrowShot(bColor)
bScore += getScore(bdist)
if bdist<bMinDist:
    bMinDist = bdist

bdist = arrowShot(bColor)
bScore += getScore(bdist)
if bdist<bMinDist:
    bMinDist = bdist

if bScore > aScore:
    print("Archer B is the winner with",bScore,"points")
elif aScore > bScore:
    print("Archer A is the winner with",aScore,"points")
elif aScore == bScore:
    if bdist < adist:
        print("Archer B is the winner, closer to the center with",bdist)
    elif adist > bdist:
        print("Archer A is the winner, closer to the center with",adist)
    elif adist==bdist:
        print("Archer A and Archer B have tied")
