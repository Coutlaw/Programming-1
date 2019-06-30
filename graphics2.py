2from graphics import *
def graphic():
    win = GraphWin("alias", 300, 500)
    ptA = Point(150, 250)
    ptB = ptA
    ptA.draw(win)
    ptB.move(-50, 100)
#ptB is the alias for ptA so when you change ptB it changes ptA
    ptC = ptB
    ptD = ptB.clone()

## random movment functions

import random
def randomMovement():
    for i in range(30):
        for cir in circles:
            cir.move(randint(0,40),0)
        time.sleep(.1)


#entry box to get info
def getInfo():
    winWidth = 300
    winHeight = 400
    win = GraphWin("get Info", winWidth, winHeight)

    instructPt = Point(winWidth//2, winHeight//2)
    instruct = Text(instructPt, "")
    instruct.draw(win)

    center =  Point(winWidth//2, winHeight//2)
    numEnt = Entry(center,15)
    numEnt.draw(win)
    numEnt.setText("Enter Number")

    #pause with getMouse to allow the entered number to be stored
    #eval command converts the entered string into a int
    win.getMouse()
    num = numEnt.getText()

    instruct.setText("Click to close")
    win.getMouse()
    win.close()

    print(num)

def string():
    name = "jasmine"
    for ch in name:
         print(ch)

    name[1]
    # this is the ch at position 1 (a) not (j)

    for i in range(7):
        print(name[i])

    name2 = "Zach"

#this will not work because Zach has more requests than it does CH's
    # will return string out of range error

#    for i in range(7):
#       print(name2[i])

    #correct way
    #len() command determines length of the string it affects

    for i in range(len(name2)):
        print(name2[i])

    #grabbing chunks out of strings = sliceing

    #how to take of slice
    #jasmine
    #inclusive of first but exclusive of last like range
    print(name[2:4])

def usrName():
    # how to make usernames
    first = "cass"
    middle = "donovan"
    last = "outlaw"

    usrName = last + first[0] + middle[0]

    print(usrName)

def lists():
    name =["jackson", "andrew", "josh", "cass"]
    nums = [1,2,3]

    #name + num = jackson, andrew, josh, cass, 1, 2, 3
    #num * 4 = 1,2,3,1,2,3,1,2,3,1,2,3
    #len(num) = 3
    #name[1] = andrew
    #name[:3] = jackson, andrew, josh -> comes back as a list
        #means number of items
    #name[len(name) - 1] = cass
    #name[5] = index out of range error
    #for name in range(len(name)):
        #print(name[i])
    #= names printed down
    #name[2:4] = josh, cass
    #   because it is positions 2 and 3 printed
    #name[0] is not equal to name[0:1]
    #name [0] is a string
    #name[0:1] is a list

    names = ["jackson", "andrew", "josh", "cass"]

##    names[1][2] - > yields the item andrew and takes the 2nd sub
    # gives you the string "d"
##    
    
    
