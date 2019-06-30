#chapter 3 covered sigma function and loops
#sigma function is to calculate the sum of all integers in a range
#it adds all the number on a number line
def sigmaFunction():
    print("code to calculate sumation between")
    print("zero and upper bound specified")
    print("by user")
    print()

    upBound = eval(input("enter upperbound: "))

    total = 0
#for loop
    for i in range(upBound + 1):
        total = total + i
        print("i = ", i)
        print("total =", total)

    print("summation:", total)
#for loops - for <variable> in <sequence>:


#same sigma function with user specified lower bound
def sigmaFunction2():
    print("code to calculate sumation between")
    print("specified lower and upper numbers")
    print("by user")
    print()

    lowbound = eval(input("enter lowerbound: "))
    upBound = eval(input("enter upperbound: "))

    total = 0
    for i in range(lowbound, upBound + 1):
        total = total + i
        print("i = ", i)
        print("total =", total)

    print("summation:", total)

#same sigma function with user specified inputs counting by steps
    #the step is how many spaces the function is skipping
def sigmaFunction3():
    print("code to calculate sumation between")
    print("two numbers by a certian interval")
    print("by user")
    print()

    lowbound = eval(input("enter lowbound: "))
    upBound = eval(input("enter upperbound: "))
    step = eval(input("enter the interval: "))

    total = 0
    for i in range(lowbound, upBound + 1, step):
        total = total + i
        print("i = ", i)
        print("total =", total)

    print("summation:", total)

#finding the total number of syblings in a room
def sibCount():

    numPeople = eval(input("How many people are you asking? "))
    
#looping function
    #A. initilize
    #B. loop
    #C. get value
    #D. adjust accumulation
    total = 0 #A
    for i in range(numPeople):  #B
        numSib = eval(input("how many siblings do you have? "))  #C
        total = total + numSib  #D
        # also written as [total += numbSib]

    print("Total of siblings,", total)
    print()
#when calculating average put calc after loop function not attached
    sibAverage = total / numPeople
    print("Average number of siblings:", sibAverage)

#calculating factoraial functions with loop command
def factorial():
    upBound = eval(input("what number to find factorials? "))

    fact = 1
    for i in range(upBound):
        fact = fact * (i + 1)

    print(upBound, "! =", fact)

#same function when you define a parameter and input an argument
    #parameter is set in parenteseis
    #argument is inputed by the user
def factorial2(upBound):
    
    fact = 1
    for i in range(upBound):
        fact = fact * (i + 1)

    print(upBound, "! =", fact)


#   
def series1():
    numTerms = eval(input("num terms in serries: "))

    total = 0
    for i in range(numTerms):
        num = 2*(i+1)
        denom = 3 ** i
        value = num / denom
        total += value
    print("total:", total)

def series2():
    numTerms = eval(input("num terms in series "))

    total = 1
    for i in range(numTerms):
        num = 2 * i + 1
        denom = 2 ** (i + 1)
        value = num / denom
        total *= value
    print("total:", total)
    
#specifying print commands
def printExample():
    for i in range(5):
        print(i, end = " ")
        # specifying end command will not force a page break unless
        # you type \n for the new line
        # \n - escape sequence for new line
    print("\nHow are you?")
        # \t is tabe escape sequence
    print("\tintented stuff")
    # \" or \' prints quotes
    print("\"someone said this\"")
    print()



##math lab always goes at header of code
import math                   
def circArea():
## importing math lab
## libraryName.functionName()
    Pi = 3.14
    rad = eval(input("enter radius: "))

    area = math.pi * rad ** 2

    print("/ncircle Area: " + str(area))

def mathFun():
    value = eval(input("Number: "))
    print("Square root", math.sqrt(value))
    print("\nsin", math.sin(value))
    print("\nceiling", math.ceil(value))
    print("\nfloor", math.floor(value))
               
