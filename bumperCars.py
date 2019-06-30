#   Name: Cass Outlaw 
#   bumperCars.py
#
#   Problem: Create a graphic window that simulates bumpercars hitting
#           eachother and they will bounce off walls and eachother
#
#   Certification of Authenticity:
#   I certify that this lab is entirely my own work.

#import librarys
from graphics import *
from math import *
import time
import random

def main():
    # set number of times loop will run and move the bumper cars
    # a good test is 1000 times
    numReps = eval(input("Enter number of times loop will run: "))
    # define and draw window
    winWidth = 500
    winHeight = 500
    win = GraphWin("Bounce House", winWidth, winHeight)
    win.setBackground("white")

    #create 2 circles to represent cars
    center1 = Point(100, winHeight / 2)
    center2 = Point(winWidth - 100, winHeight / 2)
    ball1 = Circle(center1, 25)
    ball2 = Circle(center2, 25)
    ball1.draw(win)
    ball2.draw(win)
    ball1.setFill("black")
    ball2.setFill("black")

    #create a color list for the random selection of colors
        # i didnt know I could use randomColor() untill I was done
    colors = ["yellow", "green", "blue", "red", "purple", "orange"]
    
    # create the amounts that the x and y coordinates of the balls
        # will move
        # these are constants so the speed doesnt change in the loop
        # only direction will change
    # x and y movement for ball 1
    xMove = random.randint(1, 20)
    yMove = random.randint(1, 20)
    # x and y movement for ball 2
    x2Move = random.randint(1, 20)
    y2Move = random.randint(1, 20)
    # initilize loop
    for i in range(numReps):
        # move the balls by their constants
        ball1.move(xMove, yMove)
        ball2.move(x2Move, y2Move)
        # find center of balls after movment for calculations
        c1 = ball1.getCenter()
        c2 = ball2.getCenter()
        # find x and y coordinates of the balls center points
        x1 = c1.getX()
        x2 = c2.getX()
        y1 = c1.getY()
        y2 = c2.getY()
        # calculate distance between center points of the balls
        # to determine if they collided
            # could have used didCollide()
            # but didnt know untill I finished
        dist = sqrt(((x2 - x1)**2) + ((y2 - y1)**2))

        #create if statments in nest so that if more than one
        # contitional at a time is met then ther balls will not
        # leave the window
        # determine if ball 1 hits either vertical wall
        if x1 <= 25 or x1 >= 475:
            xMove = -xMove
            ball1.setFill(random.choice(colors))
            # determine if ball 2 hits either vertical wall
            if x2 <= 25 or x2 >= 475:
                x2Move = -x2Move
                ball2.setFill(random.choice(colors))
                # determine if ball 1 hits a horizontal wall
                if y1 <= 25 or y1 >= 475:
                    yMove = - yMove
                    ball1.setFill(random.choice(colors))
                    # determine if ball 2 hits a horizontal wall
                    if y2 <= 25 or y2 >= 475:
                        y2Move = -y2Move
                        ball2.setFill(random.choice(colors))
                        # determine if balls collided
                        if dist <= 50:
                            ball1.setFill(random.choice(colors))
                            ball2.setFill(random.choice(colors))
                            xMove = -xMove
                            yMove = -yMove
                            x2Move = -x2Move
                            y2Move = -y2Move
                            
# no need to check ball one it was in the first conditional
        # determine if ball 2 hits a vertical wall
        elif x2 <= 25 or x2 >= 475:
            x2Move = -x2Move
            ball2.setFill(random.choice(colors))
            # determine if ball 1 hits a horizontal wall
            if y1 <= 25 or y1 >= 475:
                    yMove = - yMove
                    ball1.setFill(random.choice(colors))
                    # determine if ball 2 hits a horizontal wall
                    if y2 <= 25 or y2 >= 475:
                        y2Move = -y2Move
                        ball2.setFill(random.choice(colors))
                        # determine if balls collided
                        if dist <= 50:
                            ball1.setFill(random.choice(colors))
                            ball2.setFill(random.choice(colors))
                            xMove = -xMove
                            yMove = -yMove
                            x2Move = -x2Move
                            y2Move = -y2Move
                            
        # determine if ball 1 hits a horizontal wall
        elif y1 <= 25 or y1 >= 475:
            yMove = - yMove
            ball1.setFill(random.choice(colors))
            # determine if ball 2 hits a horizontal wall
            if y2 <= 25 or y2 >= 475:
                        y2Move = -y2Move
                        ball2.setFill(random.choice(colors))
                        # determine if balls collided
                        if dist <= 50:
                            ball1.setFill(random.choice(colors))
                            ball2.setFill(random.choice(colors))
                            xMove = -xMove
                            yMove = -yMove
                            x2Move = -x2Move
                            y2Move = -y2Move
                            
        # determine if ball 2 hits a horizontal wall
        elif y2 <= 25 or y2 >= 475:
            y2Move = -y2Move
            ball2.setFill(random.choice(colors))
            # determine if balls collided
            if dist <= 50:
                ball1.setFill(random.choice(colors))
                ball2.setFill(random.choice(colors))
                xMove = -xMove
                yMove = -yMove
                x2Move = -x2Move
                y2Move = -y2Move
                
        #determine if balls collided
        elif dist <= 50:
            ball1.setFill(random.choice(colors))
            ball2.setFill(random.choice(colors))
            xMove = -xMove
            yMove = -yMove
            x2Move = -x2Move
            y2Move = -y2Move
            
    #close window after completion
    instructPt = Point(winWidth / 2, winHeight / 2)
    text = Text( instructPt, "Click window to close")
    text.draw(win)
    text.setFill("black")
    win.getMouse()
    
    
    win.close()

            

        

                
    
    
    
