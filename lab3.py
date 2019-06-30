## <your name>
## lab3.py

from graphics import *

#Calculate the average of a group of numbers per assignment instructions
def average():
    print("Finds average")

    numTest = eval(input("Enter the number of homeworks you have done "))

    
    testTotal = 0
    for i in range(numTest):
        testGrade = eval(input("Enter your grade on HW"+str(i+1)+": "))
        testTotal = testTotal + testGrade
        
    average = testTotal / numTest
    

    print("Your average after", numTest,"tests is", average)

def fibonacci():
    print("Finds value of input number in Fionacci sequence")

    n = eval(input("Enter the number of the sequence you want "))

    pre = 0
    curr = 1
    temp = 0
    for i in range(n - 1):
        temp = pre + curr
        pre = curr
        curr = temp

    print("Your fibonacci number is:", pre)
        
        

def newton():
    x = eval(input("Enter The number you want to take the root of: "))
    numAppx = eval(input("Enter the number of approximations you want "))

    approx = x / 2 
    for i in range(numAppx - 1):
        approx = (x / approx + approx) / 2
        
    print("After", numAppx, "approximations your square is", approx)

def clickCircles():
    winWidth = 300
    winHeight = 400
    win = GraphWin("Click to draw", winWidth, winHeight)

    instructPoint = Point(winWidth//2, winHeight - 20)
    instructions = Text(instructPoint, "Click on window to draw a circle.")
    instructions.draw(win)

    for i in range(5):
        clickPt = win.getMouse()
        cir = Circle(clickPt, 100)
        cir.draw(win)
        cir.setWidth(2)
        cir.setFill("orange")
        cir.setOutline("purple")

    instructions.setText("Click again to exit.")
    win.getMouse()
    win.close()
    
def house():
    winWidth = 300
    winHeight = 400
    win = GraphWin("Click to draw", winWidth, winHeight)
    win.setBackground("blue")

    rCorner1 = Point(winWidth / 4, winHeight / 2)
    rCorner2 = Point(winWidth * 3 / 4, winHeight * 3 / 4)
#    RC1.draw(win)
#    RC2.draw(win)
    rec = Rectangle(rCorner1, rCorner2)
    rec.draw(win)
    rec.setWidth(2)
    rec.setFill("white")
    rec.setOutline("white")

    tPoint1 = Point(winWidth / 4, winHeight / 2)
    tPoint2 = Point(winWidth * 3 / 4, winHeight / 2)
    tPoint3 = Point(winWidth / 2, winHeight / 3)
    triangle = Polygon(tPoint1, tPoint2, tPoint3)
    triangle.draw(win)
    triangle.setFill("brown")

    win.getMouse()
    win.close()       

def sequence():
    n = eval(input("Enter number of the sequence you want: "))

    value = 2
    for i in range(n):
        print(value, end = " ")
        additive = (i % 2)
        additive *= 2
        value = value + additive

    
#Example graphics program
def clickPoint():
    winWidth = 300
    winHeight = 400
    win = GraphWin("Click a point", winWidth, winHeight)

    instructPoint = Point(winWidth//2, winHeight - 20)
    instructions = Text(instructPoint, "Click on window to draw a point.")
    instructions.draw(win)

    clickPt = win.getMouse()
    clickPt.draw(win)

    instructions.setText("Click again to exit.")
    win.getMouse()
    win.close()
    
def main():
    #average()
    fibonacci()
    #newton()
    #sequence()
    #pi()
