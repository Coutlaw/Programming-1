class Point:
    def --init--(self):
        self.x = 0
        self.y = 0

    def setX(self,xValue):
        if type(xValue) == int:
            self.x = xValue

    def setY(self, yValue):
        if type(yValue) == int:
                self.y = yValue
                
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
