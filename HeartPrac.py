from graphics import *
def test():
    winWidth = 1000
    winHeight = 700
    win = GraphWin("test", winWidth, winHeight)

    heart = Polygon(Point(0,0), Point(10,-10), Point(20, 0),
                    Point(0,30), Point(-20, 0), Point(-10, -10))
    heart.draw(win)

    heart.move(100, 100)

    arrow = Polygon(Point(1100, 300),Point(1260, 300), Point(1270, 285),
                    Point(1260, 300), Point(1275, 300), Point(1285, 285),
                    Point(1275, 300), Point(1290, 300), Point(1300, 285),
                    Point(1290, 300), Point(1300, 300), Point(1290, 300),
                    Point(1300, 315), Point(1290, 300), Point(1275, 300),
                    Point(1285, 315), Point(1275, 300), Point(1260, 300),
                    Point(1270, 315), Point(1260, 300), Point(1100, 300))
    arrow.draw(win)
    arrow.setFill("brown")
    arrow.setOutline("brown")
    arrow.setWidth(3)
    arrow.move(-500, 0)
                    
                    
    
    #construction of the arrow
    shaftPt1 = Point(1100, 300)
    shaftPt2 = Point(1300, 300)
    arrowShaft = Line(shaftPt1, shaftPt2)
    arrowShaft.setOutline("brown")
    arrowShaft.setWidth(5)
    arrowShaft.setFill("brown")
    arrowShaft.draw(win)

    #construction of the arrow fletchings
    fletchingBase1 = Point(1260, 300)
    fletchingPt1 = Point(1270, 285)
    fletchingPt2 = Point(1270, 315)
    fletching1 = Line(fletchingBase1, fletchingPt1)
    fletching2 = Line(fletchingBase1, fletchingPt2)
    fletching1.setFill("brown")
    fletching1.setOutline("brown")
    fletching2.setFill("brown")
    fletching2.setOutline("brown")
    fletching1.draw(win)
    fletching2.draw(win)
    
    fletchingBase2 = Point(1275, 300)
    fletchingPt3 = Point(1285, 285)
    fletchingPt4 = Point(1285, 315)
    fletching3 = Line(fletchingBase2, fletchingPt3)
    fletching4 = Line(fletchingBase2, fletchingPt4)
    fletching3.setFill("brown")
    fletching3.setOutline("brown")
    fletching4.setFill("brown")
    fletching4.setOutline("brown")
    fletching3.draw(win)
    fletching4.draw(win)
    
    fletchingBase3 = Point(1290, 300)
    fletchingPt5 = Point(1300, 285)
    fletchingPt6 = Point(1300, 315)
    fletching5 = Line(fletchingBase3, fletchingPt5)
    fletching6 = Line(fletchingBase3, fletchingPt6)
    fletching5.setFill("brown")
    fletching5.setOutline("brown")
    fletching6.setFill("brown")
    fletching6.setOutline("brown")
    fletching5.draw(win)
    fletching6.draw(win)


    #
