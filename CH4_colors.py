## ch4
## using color_rgb()
## applying movement to an object
## adding instructions
def main():
    color()

    
from graphics import *
def color():
    winHeight = 600
    winWidth = 600
    win = GraphWin("colors", winWidth, winHeight)

    winCent = Point(winWidth / 2, winHeight / 2)

    #setting text/ instructions
    bTextPt = Point(winWidth / 2, winHeight - 20)
    instructions = Text(bTextPt, "Click to draw circle")
    instructions.draw(win)
    

    #draw circle where user clicks
    clickPt = win.getMouse()
    cir = Circle(clickPt, 100)
    cir.draw(win)
    #define new color
    hotPink = color_rgb(255, 105, 180)
    cir.setFill(hotPink)

    #change insructions
    instructions.setText("Enjoy!")


    #create movment for cirlce
    for i in range(30):
        cir.move(5,0)
        time.sleep(.2)

    #change instructions
    instructions.setText("Click to close")

    #close window
    clickPt2 = win.getMouse()
    win.close()


    
    
