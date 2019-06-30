# CSCI 220L - Lab 10 Solutions
#
# Name 1:
#
# Name 2:
#
from random import *
from math import *
def calculateSum(value, numIterations):
    iterations = 0
    total = 0
    while iterations < numIterations:
        total += value
        iterations += 1
    return total

def areEqual(num1, num2):
    result = abs(num2 - num1) < .0001
    return result

def goodInput():
    number = eval(input("Enter Number: "))
    while number <= 50 and number > 10 or number < 1 and number != -1:
        print("try again")
        number = eval(input("Enter number: "))       
    # returns the number that meets parameters
    return number
    
        
def numDigits():
    number = eval(input("Enter your number: "))
    while number > 0:
        numDigits = 0
        while number != 0:
            number = number // 10
            numDigits += 1
        print(numDigits)
        number = eval(input("Enter your number: "))
        

def hiLoGame():
    number = randint(1, 100)
    print(number)
    print("Im thinking of a number between 1 and 100")
    guess = eval(input("Enter your first guess: "))
    total = 1
    while guess != number and total < 7:
        if guess > number:
            print("You guessed too high")
        else:
            print("You guessed too low")
        total += 1
        guess = eval(input("Enter next guess: "))
    if guess == number:
        print("congrats you won in", total, "guesses")
    else:
        print("Sorry you lost in", total, "guesses")



def main():
    result = calculateSum(.1, 10)
    equals = areEqual(1.0, result)
    if equals == True:
        print("Numbers are equal")
    else:
        print("Numbers are not equal")
    
    number = goodInput()
    print(number)
    numDigits()
    hiLoGame()
    
    
