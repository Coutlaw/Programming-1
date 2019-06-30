## lab2.py
## Purpose: Solves problems assigned in Lab 2
## Name: Cass Outlaw 
import math
def helloWorld():
    print("Hello, world!")

def sumOfThrees():
    print("This function sums multiples of three.")
    
    ## Variables
    startingPoint = 0
    upBound = eval(input("Enter the upperbound "))
    step = 3
    
    total = 0
    for i in range(startingPoint, upBound + 1, step):
        total = total + i

    print("Summation by mutiples of 3 to your upper bound =", total)
    

def triangleArea():
    print("This function calculates the area of a triangle")
    print()

#enter sides
    a = eval(input("Enter the legnth of side a "))
    b = eval(input("Enter the legnth of side b "))
    c = eval(input("Enter the legnth of side c "))
    
#calculatons
    s = (a + b + c) / 2
    #math under sqrt
    step1 = s - a
    step2 = s - b
    step3 = s - c
    step4 = step1 * step2 * step3 * s
    area = math.sqrt(step4)

    print("The area of your triangle is =", area)
    

def sumSquares():
    print("This function calculates the sum of square roots")
    print("from an upper and lower bound designated by you")
    print()

    upperBound = eval(input("Enter your upperbound "))
    lowerBound = eval(input("Enter your lowerboud "))

    total = 0
    for i in range(lowerBound, upperBound +1):
        squareValue = (i ** 2)
        print("i =", i)
        print("i**2 =", squareValue)
        total = total + squareValue
        

    print("Summation of squares =", total)

def power():

    base = eval(input("Enter the base number "))
    power = eval(input("Enter the power of the base "))

    total = 1
    for i in range(power):
        total = base * total

    print("Value of", base, "to a power of", power, "is", total)

def multiplicationTable():

    total = 1
    for i in range(1 , 13):
        print("\n", i, ":", end = " ")
        for j in range(1 , 13):
            print (i * j, end = "\t")
            
        

#Type each function here then call the function from main() below.
#Once the function is working correctly, you can put a comment symbol
#in front of the call in main() so that you don't have to see it run over
#and over.  An example helloWorld function is above with a commented out
#call to the working function below.

def main():
    #helloWorld()  
    #sumOfThrees()
    #triangleArea()
    #sumSquares()
    #power()
    multiplicationTable()
