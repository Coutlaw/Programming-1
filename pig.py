#   Name: Cass Outlaw 
#   pig.py
#
#   Problem: Creating a dice game of pig where the user rolls 2 dice
#           to try and get 100 points before the computer
#           if the user or computer roll a 1 they lose all points that
#           round, if you roll two 1's then you lose all your points
#
#   Certification of Authenticity:
#   I certify that this lab is entirely my own work.




# import libraries
from math import *
from random import *
import time

# create a function that generates a random number between 1 and 6
def roll():
    rolledNumber = randint(1, 6)
    # return the number selected at the end of the function
    return rolledNumber

# create the function that simulates the players turn
def playerPlays(totalPlayerPoints):
    #initialize variables for while loop
    # total points in the round
    roundTotal = 0
    # starting dice values
    die1 = 0
    die2 = 0
    # let the user know its his turn (Sarcastically of course)
    print("HUMANS TURN")
    # ask the user if he would like to roll
        # go variable will become conditional variable
    go = input("Ready to roll? (yes or no): ")
    # incase the user capitolizes his input
    go = go.lower()
    # conditional that determins if the user entered a valid input
    if go == "yes":
        # if user entered valid input, set conditions for the while loop
        while roundTotal < 100 and go == "yes":
            # roll 2 dice
            die1 = roll()
            die2 = roll()
            # let the user know what they rolled
            print("You rolled a", die1, "and a", die2)
            # conditions for the results of the roll
                # if the user rolled snake eyes
            if die1 == 1 and die2 == 1:
                # snake eyes results in a loss of total points thus far
                roundTotal = 0
                totalPlayerPoints = 0
                print("You rolled snake eyes, you lose all points")
                # change conditional variable to "no" so loop will end
                go = "no"

            #if user rolled a 1 (not snake eyes)
            elif die1 == 1 or die2 ==1:
                #user looses all points this round
                roundTotal = 0
                print("You rolled a 1 your turn is over")
                # set conditional to end loop
                go = "no"

            # if user rolled good numbers
            else:
                # add result to round total
                roundTotal = roundTotal + (die1 + die2)
                print("Your round total so far is =", roundTotal)
                # ask user if they would like to roll again
                go = input("Roll again? (yes or no): ")
                go = go.lower()
    # if user wants to skip his turn before rolling
    elif go == "no":
        print("ok fine, skip your turn then")
    # if the user is a child and cant follow instructions
    # for any non valid input the user will forfeit his turn
    else:
        print("because you can't read instructions you forfeit your turn")
    print("This round you earned", roundTotal, "points")
    
    #tally and return the total points the user has by adding roundTotal
    totalPlayerPoints += roundTotal
    print()
    print("*" * 12)
    print()
    return totalPlayerPoints
# create function to simulate computer turn
def computerPlays(totalComputerPoints):
    # initilize variables for computer
    roundTotal = 0
    die1 = 0
    die2 = 0
    # let user know its the computers turn
    print("Computers turn")
    go = "yes"
    # create while loop
        # if computer has not rolled a 1 and has less than 20 points in
        # this round then it will keep rolling
    while roundTotal < 20 and go == "yes":
        # call roll function to simulate dice roll
        die1 = roll()
        die2 = roll()
        print("The computer rolled", die1, "and a", die2)
        # if computer rolls snake eyes it looses all points
        if die1 == 1 and die2 == 1:
            roundTotal = 0
            totalComputerPoints = 0
            go = "no"
        # if computer rolls a 1 it looses its points in the round
        elif die1 == 1 or die2 ==1:
            roundTotal = 0
            go = "no"
        # if computer rolls good numbers           
        else:
            # add numbers to round total
            roundTotal = roundTotal + (die1 + die2)
        print("The computer has", roundTotal, "points this round")
    # add roundTotal to totalComputerPoints
    totalComputerPoints += roundTotal
    # inform the user how many points the computer gained that round
    print("The computer now has", totalComputerPoints, "points")
    print()
    print("*" * 12)
    print()
    # return totalComputerPoints
    return totalComputerPoints

#define a funciton to play pig untill someone wins
def playPig():
    # let the user know what they are playing
    print("Welcome to pig, the object of the game is to get 100 points!")
    # initialize total points for user and the computer
    totalPlayerPoints = 0
    totalComputerPoints = 0
    # create loop to run untill someone has more than 100 points
    while totalPlayerPoints < 100 and totalComputerPoints < 100:
        totalPlayerPoints = playerPlays(totalPlayerPoints)
        print("The Human has", totalPlayerPoints, "points")
        # if the human wins on the first try end the game
        if  totalPlayerPoints < 100:
            totalComputerPoints = computerPlays(totalComputerPoints)
    # if user wins then end the loop and tell the user they won
    if totalPlayerPoints >= 100:
        print("The human wins with", totalPlayerPoints, "points" )
    # if computer wins let the user know
    elif totalComputerPoints >= 100:
        print("The computer wins with", totalComputerPoints, "points")
    # IF THERE IS A FLAW in the logic you will get this error message!!!
    else:
        print("Good job you managed to break the game")

# define a main funciton to call the play function and begin the game
def main():
    # ask user to play
    go = input("ready to play pig? (yes or no): ")
    go = go.lower()
    # if user says yes then begin loop with play function to start game
    while go == "yes":
        playPig()
        go = input("Would you like to play again? (yes or no): ")
    print("Thanks for playing!")
    
            
        
    
    
