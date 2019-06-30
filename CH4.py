#Chapter 4 class content
#graphics
#pg 108 -> in textbook
#Objects
#   the object car is made of 2 categories
#       properties - color, make, model, numDoors, fuelCapacity
#           desciptions

#       Methods - drive a car, sitIn, lock, stop, reverse, turn, fuel
#           actions

#building objects / using constructor

def tifCar():
    tifCar = car("kia", "Soul")     #constructor
    tifCar.setFuel(15)              #methods that set parameters
    tifCar.setColor                 # for the object being constructed
    
# car would be refered to as a class
#   class are blueprints to build objects

###     IMPORTS OF LIBRARYS
## other imports of librarys
# import math
# print(math.sqrt(81))
#   or
# from math import *
# print(sqrt(81))
##

## POINTS ON A GRAPH
#building point objects
from graphics import *
## KEEPS YOU FROM TYPING objectName.methodName for every function
def main():
                #before you can display the dot you must create a
            # graphics windown so the dot can be shown
    win = GraphWin("Example", 400, 600)
        # creating the grahic window with command
        # GraphWin("Name", Width, Height)
    
    
    ptA = Point(50, 100)
    #print("point's x:", ptA.getX(1))    #objectName.methodName()
    ptA.setFill("red")                  #setting color (dont import)
# displaying point with command
# object.draw(windown you want object displayed in)
# when drawing graphics the top left point is (0,0)
    ptA.draw(win)
    ptB = Point(300, 500)
    ptB.draw(win)

    line = Line(ptA, ptB)
    line.draw(win)

#more refined code
    #importing time library to make loop slower
import time
def points():
    winWidth = 300
    winHeight = 550
    win = GraphWin("Shapes", winWidth, winHeight)

    ptA = Point(50, 100)
    ptA.setFill("white")
    ptB = Point(250, 300)
    ptB.setFill("white")
    ptA.draw(win)
    ptB.draw(win)
    

    winCenter = Point(winWidth/2, winHeight/2)
    winCenter.draw(win)

    win.setBackground("red")

    colors = ["purple", "blue", "magenta", "yellow", "green"]

    for color in colors:
        time.sleep(.4)
        win.setBackground(color)
        
    # defining the objectName.methodName to close window after function
    #store clickPt as a variable so you can recall it later
    clickPt = win.getMouse()
    win.close()
# recall the clickpoint
    print("clicked point", end= " ")
    print("(" +str(clickPt.getX()) + ", " + str(clickPt.getY()) + ")")
    
#ssame code with circle funciton
    #importing time library to make loop slower
import time
def points2():
    winWidth = 300
    winHeight = 550
    win = GraphWin("Shapes", winWidth, winHeight)

    ptA = Point(50, 100)
    ptA.setFill("white")
    ptB = Point(250, 300)
    ptB.setFill("white")
    ptA.draw(win)
    ptB.draw(win)
    

    winCenter = Point(winWidth/2, winHeight/2)
    winCenter.draw(win)



        
    # defining the objectName.methodName to close window after function
    #store clickPt as a variable so you can recall it later
    clickPt = win.getMouse()

    winCenter.setFill("white")
    cir = Circle(clickPt, 40)
    cir.draw(win)
    cir.setwidth(5)
    cir.setFill("purple")
    cir.setOutline("yellow")

    clickPt2 = win.getMouse()
    win.close()

    
    
