#   Cass Outlaw
#   Problem: to create a graphical user interface version of hangman
#
#   Certification of Authenticity:
#   I certify that this lab is entirely my own work.

#import libraries to be used 
from random import *
from graphics import*
import time
import random

# wordList function accepts one peramiter that is a file
# then converts this file into a list of the individual lines
# where the indivudual lines are all words
# as strings
def wordList(file):
    # opens the file
    infile = open(file)
    # creates one string of all the data
    data = infile.read()
    # creates one list of all the lines
    words = data.split("\n")
    # edits the list to remove the last space in the list
    words = words[:len(words)-1]

    # this returns the file as a simple list of words to be chosen from
    return words

# secretWord is a fucntion that accepts the list of words from
# the function worList and at random returns one word
def secretWord(words):
    word = random.choice(words)
    # simply returns the chosen word
    return word

# endgame is a function that accepts the word chosen by secretWord,
# and the number of correct guesses so far from the guessWord function
# the function will take the lenght of the secretWord word and
# see if the user that many correct guesse
# if len(word) > trueTotal the function returns false
# else the function returns true
def endGame(word, trueTotal):
    val = trueTotal == len(word)
    
    return val

# stickman is a function that accepts the grahical window,
# the number of false guesse (falseTotal), the graphical window width
# and height
# the function then uses these inputs to graph portions of the hangman
def stickMan(win, falseTotal, winWidth, winHeight):
    # first item created is the rope that hangs the hangman
    rope1 = Line(Point(winWidth /2-7, winHeight /3+25),
                 Point(winWidth/2+7, winHeight /3+25))
    rope2 = Line(Point(winWidth /2 +7, winHeight/3+25),
                 Point(winWidth/2 + 30, winHeight/3))
    rope3 = Line(Point(winWidth/2 +30, winHeight/3),
                 Point(winWidth/2 + 30, winHeight/3-100))
    rope1.setWidth(7)
    rope2.setWidth(7)
    rope3.setWidth(7)
    rope1.setFill("black")
    rope2.setFill("black")
    rope3.setFill("black")
    
    # the next item is the head of the hangman    
    head = Circle(Point(winWidth / 2, winHeight / 3), 25)
    head.setFill("brown")

    # next item is the hangmans body
    body = Line(Point(winWidth/2, winHeight/3),
                Point(winWidth/2, winHeight/3 + 150))
    body.setFill("brown")
    body.setWidth(15)

    # next item is his left arm
    lArm = Line(Point(winWidth/2, winHeight/3 +50),
                Point(winWidth/2-75, winHeight/3+75))
    lArm.setFill("brown")
    lArm.setWidth(15)
    # then his right arm
    rArm = Line(Point(winWidth/2, winHeight/3+50),
                Point(winWidth/2+75, winHeight/3+75))
    rArm.setFill("brown")
    rArm.setWidth(15)

    # then create his right leg
    rLeg = Line(Point(winWidth/2, winHeight/3+150),
                Point(winWidth/2 -60, winHeight/3 +200))
    rLeg.setFill("brown")
    rLeg.setWidth(15)
    
    # then his left leg
    lLeg = Line(Point(winWidth/2, winHeight/3+150),
                Point(winWidth/2+60, winHeight/3+200))
    lLeg.setFill("brown")
    lLeg.setWidth(15)

    # this contional loop is to compare the number of false guesses
    # to determine what part of the hangman needs to apear at a time
    # by default it doesnt draw any of the hangman

    # the first incorrect guess draws the hangmans leg
    if falseTotal == 1:
        rLeg.draw(win)
    # then the next leg
    elif falseTotal ==2:
        rLeg.draw(win)
        lLeg.draw(win)
    # then the arm
    elif falseTotal ==3:
        rLeg.draw(win)
        lLeg.draw(win)
        rArm.draw(win)
    # then the last arm
    elif falseTotal ==4:
        rLeg.draw(win)
        lLeg.draw(win)
        rArm.draw(win)
        lArm.draw(win)
    # then draws the hangmans body
    elif falseTotal ==5:
        rLeg.draw(win)
        lLeg.draw(win)
        rArm.draw(win)
        lArm.draw(win)
        body.draw(win)
    # then draws the hangmans head
    elif falseTotal ==6:
        rLeg.draw(win)
        lLeg.draw(win)
        rArm.draw(win)
        lArm.draw(win)
        body.draw(win)
        head.draw(win)
    # then on the final incorrect guess it draws the entire hangman
    # being hung on a rope 
    elif falseTotal==7:
        rLeg.draw(win)
        lLeg.draw(win)
        rArm.draw(win)
        lArm.draw(win)
        body.draw(win)
        head.draw(win)
        rope1.draw(win)
        rope2.draw(win)
        rope3.draw(win)

# guessedWord is the final function that controls the game of hangman
# guessedWord accepts the arguments secretWord, win, winWidth, winHeight
def guessedWord(secretWord, win, winWidth, winHeight):
    #create inital values to track the number of incorect guesses
    # and number of correct guesses
    falseTotal = 0
    trueTotal = 0
    # create a list of underscores to represent the spaces needed
    # to solve the secret word
    guessedWord = ["_"] * len(secretWord)
    # draw the list in win
    guess = Text(Point(winWidth /2, (winHeight /4) *3), guessedWord)
    guess.setSize(32)
    guess.draw(win)

    # create reference points for making boxes to display
    # number of incorect guesses
    boxPtX = winWidth / 6
    boxPtY = winHeight / 2
    halfBoxSize = 20
    
    # create the left box with a rectangle method using reference points
    leftBox = Rectangle(Point(boxPtX-halfBoxSize, boxPtY-halfBoxSize),
                        Point(boxPtX +halfBoxSize, boxPtY +halfBoxSize))
    leftBoxText = Text(Point(boxPtX, boxPtY), falseTotal)
    leftBoxText.draw(win)
    leftBoxText.setSize(14)
    # usable variable to space text below box from above
    textBuffer = 50
    # create text to inform user what is in the box
    leftText = Text(Point(boxPtX, boxPtY + textBuffer),
                      "Incorrect \nGuesses")
    leftText.draw(win)
    leftBox.draw(win)

    # create empty list to store the letters already used by player
    guessedLetters = []
    # create empty list to store letters not found in secret word
    wrongLetters =[]
    # draw the wrongLetters list so user can see their incorrect guesses
    wrongList = Text(Point(boxPtX * 5, boxPtY), wrongLetters)
    wrongtxt = Text(Point(boxPtX * 5, boxPtY + textBuffer),
                 "Wrong \nLetters")
    wrongList.draw(win)
    wrongtxt.draw(win)

    # create instructions to let the user know where the game stands
    instructPoint = Point(winWidth / 2, winHeight / 7)
    instructions = Text(instructPoint, ("The Mystery Word is "+
                                        str(len(secretWord))+
                        " letters Long\n Enter your first guess in the "+
                                     "box bellow then click anywhere"))
    instructions.draw(win)
    instructions.setSize(14)

    # create input box for user to enter data    
    inp = Entry(Point(winWidth / 2, (winHeight / 6) * 5), 15)
    inp.setText("Enter Guess Here")
    inp.draw(win)

    # while loop that will terminate if user wins (by calling endGame())
    # or if the user guesses incoret 7 times
    while endGame(secretWord, trueTotal) == False and falseTotal < 7:

        # pause program untill user clicks anywhere to accept
        # their input
        win.getMouse()
        # get data entered in input box
        letter = inp.getText()

        #test if data is correct length
        if len(letter) == 1:
            # test if data enterd has been used already
            if guessedWord.count(letter) == 0:
                # test if data entered has been incorrectly used already
                if guessedLetters.count(letter) == 0:
                    # if true add letter to the list guessedLetters
                    guessedLetters.append(letter)
                    # test if secretWord contains the user letter
                    if secretWord.count(letter) > 0:
                        # run loop through len(secretWord) to find
                        # when that letter apears in secretWord
                        for i in range(len(secretWord)):
                            # if letter is found then replace
                            # the list of underscores with that letter
                            # in that subposition
                            if secretWord[i] == letter:
                                guessedWord[i] = letter
                        #if loop completes add to trueTotal the number
                        # of times that letter apeared
                        trueTotal += secretWord.count(letter)
                        # set instructions to let user know that was
                        # a good guess
                        instructions.setText("Good Job\n" +
                                             "Keep doing that")
                        # test to see if the user has guessed all
                        # letters in the secret word by calling
                        # endGame()
                        if endGame(secretWord, trueTotal) == True:
                            instructions.setText("You win")
                    # if the entered letter was not in secret word
                    else:
                        # add to false total
                        falseTotal += 1
                        # add guess to the list of letters used
                        wrongLetters.append(letter)
                        # set instructions to let user know that value
                        # was not in the word
                        instructions.setText("WRONG!!!!\n"+
                                             "Try again")
                        # test to see if the user has used all incorret
                        # guesses and inform the user
                        if falseTotal == 7:
                            instructions.setText("You lose")
                            
                # if user enters letter that was a correct guess already
                else:
                    instructions.setText("Really? \n"+
                                         "How about we dont do that"+
                                         "\nTry again")
            # if user enters letter that has been tried incorrectly 
            else:
                instructions.setText("You tried that already\n"+
                                     "Try again")
        # if user enters more than one letter
        else:
            instructions.setText("Thats more than one letter\n"+
                                 "Try again")
        # at end of each loop
        # clear entry box
        inp.setText("")
        # show all correct letters
        guess.setText(guessedWord)
        # show incorect lettesr
        wrongList.setText(wrongLetters)
        # show number of incorect guesses
        leftBoxText.setText(falseTotal)
        # call function stickMan() to determine what part of the
        # figure should show based of off the users guess
        stickMan(win, falseTotal, winWidth, winHeight)
    
    # when loop terminates undraw every item in win
    guess.undraw()
    inp.undraw()
    wrongList.undraw()
    leftBoxText.undraw()
    leftBox.undraw()
    leftText.undraw()
    wrongtxt.undraw()
    instructions.undraw()

# function main() draws the window and controls how many times to
# play the game
def main():
    # define window
    winWidth = 1000
    winHeight = 600
    win = GraphWin("Dissapearing", winWidth, winHeight)
    
    # set instructions point to inform user on what to do
    instructPt = Point(winWidth/2, 3 * (winHeight/4))
    instructions = Text(instructPt, "Ready to play ?")
    instructions.draw(win)
    
    # create second instuction point to explain the game
    instructPt2 = Point(winWidth/2, winHeight /4)
    instructions2 = Text(instructPt2, ("Welcome to dissapearing man\n" +
    "If you chose to play,\n" +
    "the next screen will have a number of blank spaces\n" +
    "The spaces are how many letters there are in the mystery word\n" +
    "You can guess and enter one letter at a time\n" +
    "The number of your incorrect guesses will apear on the right\n" +
    "Incorrect letters will apear on the right\n" +                                     
    "If you guess all the letters before you make 7 mistakes you win"))
    instructions2.draw(win)
    instructions2.setSize(14)

    # create referenece points to draw yes and no buttons
    boxPtX = winWidth/6
    boxPtY = winHeight/6
    # create yes and no button text
    leftBoxText =  Text(Point(boxPtX * 2, boxPtY * 5), "Yes")
    rightBoxText = Text(Point(boxPtX * 4, boxPtY * 5), "No")
    # create yes and no button with rectangle methods
    leftBoxBorder = Rectangle(Point((boxPtX*2) - 25, (boxPtY*5) - 15),
                              Point((boxPtX*2) + 25, (boxPtY*5) + 15))
    rightBoxBorder = Rectangle(Point((boxPtX*4) - 25, (boxPtY*5) - 15),
                               Point((boxPtX*4) + 25, (boxPtY*5) + 15))
    # draw buttons
    rightBoxText.draw(win)
    rightBoxBorder.draw(win)
    leftBoxBorder.draw(win)
    leftBoxText.draw(win)
    
    # pause function untill user makes a decision with a click
    click = win.getMouse()
    # set conditional to make while loop run
    go = False
    while go == False:
        # find x and y of where user clicked
        cX = click.getX()
        cY = click.getY()

        # if user clicked within the box yes terminate this loop
        if (((boxPtX*2)-25) <= cX <= ((boxPtX*2)+25) and
        ((boxPtY*5)-15) <= cY <= ((boxPtY*5)+15)):
            go = True

        # if user clicked inside box no, pause and then terminate window
        elif ((boxPtX*4-25) <= cX <= (boxPtX*4+25) and
        (boxPtY*5-15) <= cY <= (boxPtY*5+15)):
            instructions.setText( "Ok then, bye!")
            time.sleep(.5)
            win.close()

        # if user clicks neither button then continue loop untill
        # user makes valid choice
        else:
            instructions.setText("How about you try clicking a button?")
            click = win.getMouse()
            go = False

    # once user make a chioce, undraw all contents in window                                  
    rightBoxText.undraw()
    rightBoxBorder.undraw()
    leftBoxText.undraw()
    leftBoxBorder.undraw()
    instructions.undraw()
    instructions2.undraw()

    # define the file of words to use for the game
    file = "wordslist.txt"
    # set conditional for second loop to play the game
    go = True
    while go == True:
        # call wordList() to turn text file into list of words
        possibleWords = wordList(file)
        # call secretWord() to pick random word from the list
        word = secretWord(possibleWords)
        # pring word in terminal for testing purposes
        print(word)
        # call guesssedWord() to play the game of hangman
        guessedWord(word, win, winWidth, winHeight)
        
        # after guessedWord() playes the game one time
        # redraw yes and no check box, then ask user if they
        # would like to play again
        rightBoxText.draw(win)
        rightBoxBorder.draw(win)
        leftBoxText.draw(win)
        leftBoxBorder.draw(win)
        instructions.draw(win)
        instructions.setText("Play again?")
        
        # pause function to see what user wants to do
        click = win.getMouse()
        # find where user clicked
        cX = click.getX()
        cY = click.getY()

        # if user clicks yes, undraw yes and no buttons,
        # then make while loop run again to replay the game and
        # pick new word
        if (((boxPtX*2)-25) <= cX <= ((boxPtX*2)+25) and
        ((boxPtY*5)-15) <= cY <= ((boxPtY*5)+15)):
            rightBoxText.undraw()
            rightBoxBorder.undraw()
            leftBoxText.undraw()
            leftBoxBorder.undraw()
            instructions.undraw()
            instructions2.undraw()
            go = True

        # if user clicks no then close the window and end loop
        elif ((boxPtX*4-25) <= cX <= (boxPtX*4+25) and
        (boxPtY*5-15) <= cY <= (boxPtY*5+15)):
            instructions.setText( "Ok then, bye!")
            time.sleep(.5)
            go = False
            win.close()

        # if user does not click a valid button
        else:
            instructions.setText("How about you try clicking a button?")
            click = win.getMouse()
            go = True
        
 


    
    
    
