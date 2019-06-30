#creating dice with opject oreinted programming
from random import *
class Die:
    def __init__(self, numSides):         # constucter call
        # should set legitamte values for properties
        if type(numSides) == int and numSides >= 2:
            self.numSides = numSides
        # sets defalut if user doesnt input a value
        else :
            self.numSides = 6

        
        self.faceValue = 1

    # getter methods
    def getFaceValue(self):
        return self.faceValue

    def getNumSides(self):
        return numSides
    
    # setter methods
    # should accept legit values for properties
        # setters usually accept one value other than self
    
    def setFaceValue(self, value):
        if type(value) == int and self.numSides >= value and value >= 1:
            self.faceValue = faceValue
        # no need for else bacasue it will just leave faceValue same
        
    

    # extra methods

    # roll sets face value to rand int between 1 and num sides
    def roll(self):
        # you dont have to use numSides as a peramiter buecause it is
        # already a property of Die
        self.faceValue = randint(1, self.numSides)


    #__str__(self) is string method
    # - returns a string representation of an object

    def __str__(self):
        msg = "num Sides = " +str(self.numSides) + "\n"
        msg += "Face value = " +str(self.faceValue)
        return msg

        
        
