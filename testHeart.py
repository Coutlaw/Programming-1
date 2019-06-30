from graphics import *
def test():
    winWidth = 1000
    winHeight = 700
    win = GraphWin("test", winWidth, winHeight)

 #   x**2 + (y - (x ** 2) ** (1/3)) ** 2 = 1
#define the top two circles on the heart
    cirCent1 = Point(winWidth / 2 - 20, winHeight / 2 - 40)
    cirCent2 = Point(winWidth / 2 + 20, winHeight / 2 - 40)

    cirLeft = Circle(cirCent1, 20)
    cirRight = Circle(cirCent2, 20)
    cirLeft.setFill("Red")
    cirLeft.setOutline("Red")
    cirLeft.setWidth(0)
    cirRight.setFill("Red")
    cirRight.setOutline("Red")
    cirLeft.draw(win)
    cirRight.draw(win)
    cirRight.setWidth(0)

#create small rectangle to cover gap between circles and triangle
##    recC1 = Point(winWidth / 2 - 20, winHeight / 4 + 50)
##    recC2 = Point(winWidth / 2 + 20, winHeight /4 + 70)
##    
##    rec1 = Rectangle(recC1, recC2)
##    rec1.setFill("Red")
##    rec1.setOutline("Red")
##    rec1.draw(win)
##    rec1.setWidth(0)
    
#Create bottom triangle to complete the heart shape   
    triPt1 = Point(winWidth / 2 - 37, winHeight / 2 - 30)
    triPt2 = Point(winWidth / 2 + 37, winHeight / 2 - 30)
    triPt3 = Point(winWidth / 2, winHeight / 2 + 30)
    
    tri = Polygon(triPt1, triPt2, triPt3)
    tri.setFill("Red")
    tri.setOutline("Red")
    tri.draw(win)
    tri.setWidth(0)

    
    
    
    for i in range(15):
        clickPt = win.getMouse()
        x = clickPt.getX()
        y = clickPt.getY()
        print(x, ",", y)


    
        
    
        
