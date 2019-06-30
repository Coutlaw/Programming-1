#   Name: Cass Outlaw 
#   greetingCard.py
#
#   Problem: Creat an graphics window with a valentines day greeting
#           Have a graphic arrow travel through the heart           
#
#   Certification of Authenticity:
#   I certify that this lab is entirely my own work.

#import librarys
from graphics import *
import time
#define function
def main():
    #create graphics window "Happy V-day"
    winWidth = 1000
    winHeight = 700
    win = GraphWin("Happy V-day", winWidth, winHeight)
    win.setBackground("pink")

    #create text at the top of the window saying "happy valentines day"
    topTextPT = Point(winWidth / 2, 100)
    topText = Text(topTextPT, "Happy Valentines Day")
    topText.setSize(20)
    topText.draw(win)
    topText.setFill("pink")

    #create loop making the previous text apear as if it were growing
    for i in range(5, 37):
        topText.setFill("red")
        topText.setSize(i)
        time.sleep(.01)
        
    #create another text with the introduction to what the user will see
    midTextPt = Point(winWidth / 2 , winHeight / 2 )
    midText = Text(midTextPt, "Can a loving heart out run an arrow?")
    midText.setFill("red")
    midText.draw(win)
    midText.setSize(36)

    #give user instructions to start program sequence
    clickTextPt = Point(winWidth / 2, winHeight / 2 + 50)
    clickText = Text(clickTextPt, "Click to find out")
    clickText.setSize(12)
    clickText.draw(win)
    #wait of user input to begin
    win.getMouse()

    #undraw the previous text so the window is bare
    
    midText.undraw()
    clickText.undraw()

    #construction of the polygon that creats the heart shape
    heart = Polygon(Point(0,0), Point(10,-10), Point(20, 0),
                    Point(0,30), Point(-20, 0), Point(-10, -10))
    heart.draw(win)
    heart.setFill("red")

    #construction of polygon arrow
    #used the original code below to aquire points then converted the
        #individual objects into single polygon for better animation
    arrow = Polygon(Point(1100, 300), Point(1260, 300), Point(1270, 285)
                    , Point(1260, 300), Point(1275, 300),
                    Point(1285, 285), Point(1275, 300), Point(1290, 300)
                    , Point(1300, 285), Point(1290, 300),
                    Point(1300, 300), Point(1290, 300), Point(1300, 315)
                    , Point(1290, 300), Point(1275, 300),
                    Point(1285, 315), Point(1275, 300), Point(1260, 300)
                    , Point(1270, 315), Point(1260, 300),
                    Point(1100, 300))
    arrow.draw(win)
    arrow.setFill("brown")
    arrow.setOutline("brown")
    arrow.setWidth(3)

# ORIGINAL CODE: that led to creation of polygon arrow
##    #construction of the arrow
##    shaftPt1 = Point(1100, 300)
##    shaftPt2 = Point(1300, 300)
##    arrowShaft = Line(shaftPt1, shaftPt2)
##    arrowShaft.setOutline("brown")
##    arrowShaft.setWidth(5)
##    arrowShaft.setFill("brown")
##    arrowShaft.draw(win)
##
##    #construction of the arrow fletchings
##    fletchingBase1 = Point(1260, 300)
##    fletchingPt1 = Point(1270, 285)
##    fletchingPt2 = Point(1270, 315)
##    fletching1 = Line(fletchingBase1, fletchingPt1)
##    fletching2 = Line(fletchingBase1, fletchingPt2)
##    fletching1.setFill("brown")
##    fletching1.setOutline("brown")
##    fletching2.setFill("brown")
##    fletching2.setOutline("brown")
##    fletching1.draw(win)
##    fletching2.draw(win)
##    
##    fletchingBase2 = Point(1275, 300)
##    fletchingPt3 = Point(1285, 285)
##    fletchingPt4 = Point(1285, 315)
##    fletching3 = Line(fletchingBase2, fletchingPt3)
##    fletching4 = Line(fletchingBase2, fletchingPt4)
##    fletching3.setFill("brown")
##    fletching3.setOutline("brown")
##    fletching4.setFill("brown")
##    fletching4.setOutline("brown")
##    fletching3.draw(win)
##    fletching4.draw(win)
##    
##    fletchingBase3 = Point(1290, 300)
##    fletchingPt5 = Point(1300, 285)
##    fletchingPt6 = Point(1300, 315)
##    fletching5 = Line(fletchingBase3, fletchingPt5)
##    fletching6 = Line(fletchingBase3, fletchingPt6)
##    fletching5.setFill("brown")
##    fletching5.setOutline("brown")
##    fletching6.setFill("brown")
##    fletching6.setOutline("brown")
##    fletching5.draw(win)
##    fletching6.draw(win)


    #construct loop sequence for the heart to fall and rise
    #first loop dropps the heart
    y = 0
    x = 10
    for i in range(2, 13):
        y = i ** 2
        heart.move(x, y)
        time.sleep(.05)

    #second loop raises the heart
    x = 10
    y = 0
    for i in range(-12, -2):
        y = i ** 2
        heart.move(x, -y)
        time.sleep(.05)

    #third loop drops the heart
    x = 10
    y = 0
    for i in range(2, 13):
        y = i ** 2
        heart.move(x, y)
        time.sleep(.05)

    #fourth loop raises the heart
    x = 10
    y = 0
    for i in range(-12, -2):
        y = i ** 2
        heart.move(x, -y)
        time.sleep(.05)
        
    #fith loop drops the heart
    x = 10
    y = 0
    for i in range(2, 13):
        y = i ** 2
        heart.move(x, y)
        time.sleep(.05)
        
    #sixth loop raises the heart
    x = 10
    y = 0
    for i in range(-12, -2):
        y = i ** 2
        heart.move(x, -y)
        time.sleep(.05)        

    #seventh loop drops the heart and begins movement for the arrow
        #the arrow will colide with the heart at the end of the loop
    x = 10
    y = 0
    for i in range(2, 10):
        y = i ** 2
        heart.move(x, y)
        arrow.move(-50, 0)
        time.sleep(.05)
        
    #after the arrow contacts the heart this loop will move both of them
        #directly backwards as if the arrow pinned the heart to the wall
    for i in range(5):
        heart.move(-140, 0)
        arrow.move(-140, 0)
        time.sleep(.05)
        
    #construct blood splatter for when the heart hits the wall
    splatCent = Point(0, 300)
    splat1 = Circle(splatCent, 5)
    splat1.setFill("red")
    splat1.setOutline("red")
    splat1.draw(win)
    
    splat2 = Circle(splatCent, 5)
    splat2.setFill("red")
    splat2.setOutline("red")
    splat2.draw(win)
    
    splat3 = Circle(splatCent, 5)
    splat3.setFill("red")
    splat3.setOutline("red")
    splat3.draw(win)
    
    splat4 = Circle(splatCent, 5)
    splat4.setFill("red")
    splat4.setOutline("red")
    splat4.draw(win)

    splat5 = Circle(splatCent, 5)
    splat5.setFill("red")
    splat5.setOutline("red")
    splat5.draw(win)

    #crete a loop that causes the 5 splatter points to spray when the
        #heart hits the wall
    #first loop to make 2 splatters rise to a peak and the others fly
        #off the screen
    x = 5
    y1 = 0
    y2 = 0
    for i in range(2, 8):
        y1 = i ** 2
        y2 = (i + 2) ** 2
        splat1.move(x, - y1)
        splat2.move(x * 4, 30)
        splat3.move(x * 4, -20)
        splat4.move(x * 2, - y2)
        splat5.move(x * 3, y1)
        
    #second loop to make two of the splatters fall after their peak
    x = 5
    y1 = 0
    y2 = 0
    for i in range(-5, 100):
        y1 = i ** 2
        y2 = (i + 2) ** 2
        splat1.move(x, y1)
        splat2.move(x * 4, 20)
        splat3.move(x * 4, -20)
        splat4.move(x * 2, y2)
        splat5.move(x * 3, y1)

    #create text that appears after the heart fails to escape to answer
        #the original question
    nope = Text(midTextPt, "No a heart can't out run an arrow!!")
    nope.setSize(36)
    nope.setFill("red")
    nope.draw(win)

    #create text with user instructions on how to end the programs
    closeText = Text(clickTextPt, "Click to close")
    closeText.setSize(12)
    closeText.draw(win)
    
    #close the program when user clicks the window
    win.getMouse()
    win.close()

    

    
