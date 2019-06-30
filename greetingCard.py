#   Name: Cass Outlaw 
#   greetingCard.py
#
#   Problem: Creat an graphics window with a valentines day greeting
#           Have a graphic arrow travel through the heart           
#
#   Certification of Authenticity:
#   I certify that this lab is entirely my own work.


from graphics import *
import time
def main():
    winHeight = 700
    winWidth = 600
    win = GraphWin("Happy V-day", winWidth, winHeight)

    win.setBackground("pink")
#set top text heading "Happy Valintines Day"
    topTextPt = Point(0, 100)
    topText = Text(topTextPt, "Happy Valentines Day")
    topText.setSize(30)
    topText.draw(win)

#move top text from off screen slowly to the center of the card
    for i in range(6):
        topText.move(50, 0)
        time.sleep(.1)

#define the top two circles on the heart
    cirCent1 = Point(winWidth / 2 - 75, winHeight / 4 + 50)
    cirCent2 = Point(winWidth / 2 + 75, winHeight / 4 + 50)

    cirLeft = Circle(cirCent1, 75)
    cirRight = Circle(cirCent2, 75)
    cirLeft.setFill("Red")
    cirLeft.setOutline("Red")
    cirLeft.setWidth(0)
    cirRight.setFill("Red")
    cirRight.setOutline("Red")
    cirLeft.draw(win)
    cirRight.draw(win)
    cirRight.setWidth(0)

#create small rectangle to cover gap between circles and triangle
    recC1 = Point(winWidth / 2 - 20, winHeight / 4 + 50)
    recC2 = Point(winWidth / 2 + 20, winHeight /4 + 70)
    
    rec1 = Rectangle(recC1, recC2)
    rec1.setFill("Red")
    rec1.setOutline("Red")
    rec1.draw(win)
    rec1.setWidth(0)
    
#Create bottom triangle to complete the heart shape   
    triPt1 = Point(winWidth / 2 - 148, winHeight / 4 + 70)
    triPt2 = Point(winWidth / 2 + 147, winHeight / 4 + 70)
    triPt3 = Point(winWidth / 2, winHeight / 4 * 3)
    
    tri = Polygon(triPt1, triPt2, triPt3)
    tri.setFill("Red")
    tri.setOutline("Red")
    tri.draw(win)
    tri.setWidth(0)

#construct the hearts to rain down from the sky
    cirCent4 = Point(winWidth /6 - 20, -50)
    cirCent5 = Point(winWidth / 6 + 20, -50)
    heartCircleLeft1 = Circle(cirCent4, 20)
    heartCircleRight1 = Circle(cirCent5, 20)
    heartTrianglePoint1 = Point(85, -45)
    heartTrianglePoint2 = Point(115, -45)
    heartTrianglePoint3 = Point(100, -20)
    heartTriangle1 = Polygon(heartTrianglePoint1, heartTrianglePoint2,
                                                     heartTrianglePoint3)
    heartCircleLeft1.draw(win)
    heartCircleLeft1.setFill("red")
    heartCircleLeft1.setOutline("red")
    heartCircleRight1.draw(win)
    heartCircleRight1.setFill("red")
    heartCircleRight1.setOutline("red")
    heartTriangle1.draw(win)
    heartTriangle1.setFill("red")
    

#construct arrow
    arrowPt1 = Point(600, 650)
    arrowPt2 = Point(900, 950)
    arrowShaft = Line(arrowPt1, arrowPt2)
    arrowShaft.setWidth(10)
    arrowShaft.setOutline("Brown")
    arrowShaft.setFill("Brown")
    arrowShaft.draw(win)

    tipPt1 = Point(590, 640)
    tipPt2 = Point(600, 680)
    tipPt3 = Point(625, 650)
    arrowTip = Polygon(tipPt1, tipPt2, tipPt3)
    arrowTip.setFill("grey")
    arrowTip.draw(win)

##right fletchings on the arrow
##    fR1 = Point()
##    fR2 = Point()
##    fletching1 = Line(fR1, fR2)
##    fR3 = Point()
##    fR4 = Point()
##    fletching2 = Line(fR3, fR4)
##    fR5 = Point()
##    fR6 = Point()
##    fletching3 = Line(fR5, fR6)

#draw fletchings

###left fletchings on the arrow
##    fL1 = Point()
##    fL2 = Point()
##    fletching4 = Line(fL1, fL2)
##    fL3 = Point()
##    fL4 = Point()
##    fletching5 = Line(fl3, fL4)
##    fL5 = Point()
##    fL6 = Point()
##    fletching6 = Line(fL5, fL6)
##    fletching
    
#reconstruct upper left circle and part of a rectangle to cover shooting arrow
    cirLeft2 = Circle(cirCent1, 75)
    cirLeft2.setOutline("Red")
    cirLeft2.setFill("Red")
    cirLeft2.draw(win)
    cirLeft2.setWidth(0)

    cirCent3 = Point(winWidth / 2 - 30, winHeight / 2 - 25)
    cirLeft3 = Circle(cirCent3, 40)
    cirLeft3.setOutline("Red")
    cirLeft3.setFill("Red")
    cirLeft3.draw(win)
    cirLeft3.setWidth(0)


#make arrow move through the heart
    for i in range(19):
        arrowShaft.move(-25, -25)
        arrowTip.move(-25, -25)
        time.sleep(.09)

#give heart affects after it is punctured by arrow
    colors = ["white", "pink", "purple", "red", "black"]

    for i in range(20):
        for color in colors:
            win.setBackground(color)
            time.sleep(.09)






