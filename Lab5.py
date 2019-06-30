# Lab5.py
# Name 1:Tiffani Griffith-Dowty
# Name 2: Cass Outlaw

from graphics import *
import math
import time

def cupConverter():
    # Author: RoxAnn H. Stalvey, modified by Walter Pharr
    # Illustrates getting numeric input through graphics window
    ounceRate = 8
    milliliterRate = 29.57
    winWidth = 300
    winHeight = 200
    win = GraphWin("Convert cups to milliliters", winWidth, winHeight)

    #Specify the message for the input box
    boxDesc = Text(Point(100, 50), "Input cups: ")
    boxDesc.draw(win)

    #Create the Entry object and set its default text to a number
    #  allowing the user to see what type of value is expected
    inp = Entry(Point(200, 50), 5)
    inp.setText("0")
    inp.draw(win)

    #Create a Text object for outputting the result
    output = Text(Point(150, 150), "")
    output.draw(win)

    #This button isn't necessary, but it makes a nice point for the user
    #  to click.  If you click anywhere in the window, the code reacts
    #  the same way.
    btPtX = winWidth/2
    btPtY = winHeight/2
    button = Text(Point(btPtX, btPtY), "Click")
    button.draw(win)
    border = Rectangle(Point(btPtX-35, btPtY-20), Point(btPtX+35, btPtY+20))
    border.draw(win)

    # Wait for a mouse click
    win.getMouse()

    # Discover intput and convert it to a number
    # If numeric input wasn't needed, simply omit the eval()
    cups = eval(inp.getText())

    #Calculate milliliter equivalent here
    ounces = cups * ounceRate
    milliliters = ounces * milliliterRate

    # Display output and change button
    output.setText("value entered in milliliters = " + str(milliliters))
    button.setText("Quit")
    
    # Wait for another click to exit
    win.getMouse()
    win.close()


def target():
    winWidth = 500
    winHeight = 500
    win = GraphWin("Archery Target", winWidth, winHeight)

    # Add code here to get the dimensions and draw the target
    center = (Point(winWidth/2,winHeight/2))
    whiteCir = Circle(center, winWidth*(1/2))
    blackCir = Circle(center, winWidth*(4/10))
    blueCir= Circle(center, winWidth*(3/10))
    redCir = Circle(center, winWidth/5)
    yellowCir = Circle(center, winWidth/10)
    whiteCir.setFill("white")
    blackCir.setFill("black")
    blueCir.setFill("blue")
    redCir.setFill("red")
    yellowCir.setFill("yellow")

    whiteCir.draw(win)
    blackCir.draw(win)
    blueCir.draw(win)
    redCir.draw(win)
    yellowCir.draw(win)
    

    # Wait for another click to exit
    win.getMouse()
    win.close()



def triangle():
    winWidth = 500
    winHeight = 500
    win = GraphWin("Draw a Triangle", winWidth, winHeight)

    textPoint = Point(winWidth / 2, winHeight / 4 )
    text = Text(textPoint, "Click three times to make a triangle")
    text.draw(win)

    # Add code here to accept the mouse clicks, draw the triangle.
    point1 = win.getMouse()
    point2 = win.getMouse()
    point3 = win.getMouse()

    triangle = Polygon(point1, point2, point3)
    triangle.draw(win)



    side1x = abs(point2.getX() - point1.getX())
    side1y = abs(point2.getY() - point1.getY())
    side2x = abs(point3.getX() - point2.getX())
    side2y = abs(point3.getY() - point2.getY())
    side3x = abs(point1.getX() - point3.getX())
    side3y = abs(point1.getY() - point3.getY())

    length1 = math.sqrt((side1x ** 2) + (side1y ** 2))
    length2 = math.sqrt((side2x ** 2) + (side2y ** 2))
    length3 = math.sqrt((side3x ** 2) + (side3y ** 2))
    perimeter = (length1 + length2 + length3)
    s = perimeter / 2
    area = math.sqrt(s*(s-length1) * (s-length2) * (s-length3))

    
    
    # and display its area in the graphics window.
    text.undraw()
    text2 = Text(textPoint,"Area = " + str(area) +" Perimeter = " + str(perimeter))
    text2.draw(win)

    # Wait for another click to exit
    win.getMouse()
    win.close()

def colorShape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    #create window
    winWidth = 400
    winHeight = 400
    win = GraphWin("Color Shape", winWidth, winHeight)
    win.setBackground("white")

    #create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(winWidth/2, winHeight-20), msg)
    inst.draw(win)

    #create circle in window's center
    shape = Circle(Point(winWidth/2, winHeight/2 - 30), 50)
    shape.draw(win)

    #redTexPt is 50 pixels to the left and forty pixels down from center
    redTextPt = Point(winWidth/2 - 50, winHeight/2 + 40)
    redText = Text(redTextPt, "Red: ")
    redText.setTextColor("red")
 
    #greenTextPt is 30 pixels down from red
    greenTextPt = redTextPt.clone()
    greenTextPt.move(0,30)
    greenText = Text(greenTextPt, "Green: ")
    greenText.setTextColor("green")
 
    #blueTextPt is 60 pixels down from red
    blueTextPt = redTextPt.clone()
    blueTextPt.move(0,60)
    blueText = Text(blueTextPt, "Blue: ")
    blueText.setTextColor("blue")

    inp = Entry(Point(winWidth/2, winHeight/2 + 40), 5)
    inp.setText("0")
    inp.draw(win)
    inp1 = Entry(Point(winWidth/2, winHeight/2 + 70), 5)
    inp1.setText("0")
    inp1.draw(win)
    inp2 = Entry(Point(winWidth/2, winHeight/2 + 100), 5)
    inp2.setText("0")
    inp2.draw(win)
    #display rgb text
    redText.draw(win)
    greenText.draw(win)
    blueText.draw(win)
    shape.setFill("white")
    for i in range(5):
        win.getMouse()
        inpA = eval(inp.getText())
      
        inpB = eval(inp1.getText())
       
        inpC = eval(inp2.getText())
        
        shape.setFill(color_rgb(inpA, inpB, inpC))

def anotherSeries():
    num = eval(input("Enter the number in the series you want: "))

    total = 0
    
    for i in range(num):
        total += (i % 3 + 1) * 2

    print("Your total is: ", total)



    
    
def main():
 #   cupConverter()
#    target()
#    triangle()
    colorShape()







