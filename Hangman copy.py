import random
def secretWord(file):
    infile = open(file)
    data = infile.read()
    line = data.split("\n")
    word = random.choice(line)

    return word

from graphics import *
from math import *
import time
def guessedWord(secretWord):
    alphabetLen = 24
    guessedWord = " _ a" * len(secretWord)
    guessedWord = guessedWord.split("a")
    guessedWord = guessedWord[:(len(guessedWord) - 1)]
    print(guessedWord)
    falseTotal = 0
    trueTotal = 0
    while trueTotal < len(secretWord) or falseTotal < 7:
        letter = input("Enter guess letter: ")
        if len(letter) == 1:
            if secretWord.count(letter) > 0:
                for i in range(len(secretWord)):
                    if secretWord[i] == letter:
                        guessedWord[i] = letter
                trueTotal += secretWord.count(letter)
                print(guessedWord)
                if trueTotal == len(secretWord):
                    print("you win")
            else:
                falseTotal += 1
                print("Number of wrong answers =", falseTotal)
                if falseTotal == 7:
                    print("you lose")

        else:
            print("thats more than one letter")
    
        


def main():
    file = wordslist.txt
    guessedWord(secretWord(file))
    
    
               
