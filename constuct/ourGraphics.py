# creating a point object
#   properties - x, y
#   methods - getX, getY, setX, setY, Str
#   Constructor
class Point:        #classes are upper cammel case
    # consturctor - sets inital values for all properties
    def __init__(self):     #self is the memory address when ovject is created
        self.x = 0
        self.y = 0

    # setter method is a mutater method
    # methods mutates the object by chaning a property
    # should only set legitamete values (should test)
    
    def setX(self, xValue):
        if type(xValue) == int:
            self.x = xValue
    # getter method aka accessor method
    #   returns value of property
    def getX(self):
        return self.x
        
