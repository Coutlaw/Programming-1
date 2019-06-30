## Lab9.py
##
## Name 1:Cass Outlaw
##
## Name 2:Jesse Deacon
##

from graphics import *
from math import sqrt

def starter():
    weight = eval(input("What is your weight? "))
    numWins = eval(input("How many wins do you have? "))

    if weight >= 150 and weight < 160 and numWins > 5:
        print("You can start")
    elif weight > 199:
        print("You can start")
    elif numWins > 20:
        print("You can start")
    else:
        print("You cannot start")

def isValid(isbn):
    total = 0

    if len(isbn) == 10:
        
        isbnString = isbn
        for i in range(len(isbnString)):
            total += eval(isbnString[i])*(10-i)

        return total%11 == 0

    else:
        return len(isbn) == 10
    
    
    
        

def circleOverlap():
    """
    Draw two circles and determine whether they overlap.
    """
    #Build window
    winHeight = 400
    winWidth = 400
    win = GraphWin("Overlapping circles", winHeight, winWidth)

    #Text area for instructions for user
    instruct = Text(Point(winWidth/2, winHeight-10), "")
    instruct.draw(win)

    #Get center point and x/y for center
    instruct.setText("To draw a circle, click the centerpoint for the circle")
    center = win.getMouse()
    center.draw(win)
    cX = center.getX()
    cY = center.getY()



    #Get point on the circumference and its x/y coordinates
    instruct.setText("Click a point on the border of the circle.")
    border = win.getMouse()
    bX = border.getX()
    bY = border.getY()

    


    #Calculate radius using Euclidean distance
    radius = sqrt((cX-bX) ** 2 + (cY-bY) ** 2)
    circle = Circle(center, radius)
    circle.draw(win)

    #Get center point and x/y for center
    instruct.setText("To draw a circle, click the centerpoint for the circle")
    center2 = win.getMouse()
    center2.draw(win)
    cX2 = center2.getX()
    cY2 = center2.getY()



    #Get point on the circumference and its x/y coordinates
    instruct.setText("Click a point on the border of the circle.")
    border2 = win.getMouse()
    bX2 = border2.getX()
    bY2 = border2.getY()

    


    #Calculate radius using Euclidean distance
    radius2 = sqrt((cX2-bX2) ** 2 + (cY2-bY2) ** 2)
    circle2 = Circle(center2, radius2)
    circle2.draw(win)

    distance = sqrt((cX2 -cX) ** 2 + (cY2 - cY) **2)
    radSum = radius + radius2

    if distance > radSum:
        instruct.setText("The circles do not overlap")
    else:
        instruct.setText("The circles overlap")
    win.getMouse()
        
        

    # Wait for another click to exit
    instruct.setText("Click anywhere to close.")
    win.getMouse()
    win.close()

def leapYear(year):
    if year%400 == 0:
        return True
    elif year%100 == 0:
        return False
    elif year%4 == 0:
        return True
    else:
        return False

def main():
    ''' Add code to test all of your functions '''
#    circleOverlap()
####    starter()
##    num = input("ISBN to test: ")
##    print(isValid(num))
    num = eval(input("Year to test: "))
    boo = leapYear(num)
    if boo:
        print(str(num)+" is a leap year.")
    else:
        print(str(num)+" is not a leap year.")

