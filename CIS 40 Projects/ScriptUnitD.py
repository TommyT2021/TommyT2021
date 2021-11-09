def welcome():
    name = input("What is your name? ")
    print("Hello",name,"let's have some geometry fun!")

def printSquareArea(side):
    print("The Square Area is",side*side)

def calcRectangleArea(length,width):
    rectangleArea = length*width
    return int(rectangleArea)

print("The Rectangle Area is", calcRectangleArea(4,5))

def printRectangleVolume(length,width,height):
    Volume = calcRectangleArea(length,width) * height
    print("The Rectangle Volume is", Volume)
