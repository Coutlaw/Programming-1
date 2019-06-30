from graphics import *

def GraphData(val1, val2):
    
    winWidth = 500
    winHeight = 500
    win = GraphWin("Data Plotted", winWidth, winHeight)
    win.setBackground("white")

    dotColor = "red"
    center1 = Point(50,winHeight - val1)
    center2 = Point(100, winHeight - val2)
    dot1 = Circle(center1,10)
    dot2 = Circle(center2,10)
    dot1.draw(win)
    dot2.draw(win)
    dot1.setFill(dotColor)
    dot2.setFill(dotColor)

    lineColor = dotColor
    line1 = Line(center1, center2)
    line1.draw(win)
    line1.setFill(lineColor)
    line1.setWidth(3)


    
def main():
    val1 = 300
    val2 = 350
    GraphData(val1, val2)

