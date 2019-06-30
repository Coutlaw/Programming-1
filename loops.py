#Lecutre of chapter 1

#function to calculate area of a rectangle
def calcArea():
    print("Calculates the area of a rectangle")
    print()

    #get lenght and width
    lenght = eval(input("Enter the lenght: "))
    width = eval(input("enter the width: "))

    #calculate area
    area = lenght * width

    #display results
    print("Area of the rectangle =", area)

#class examples
def example():
    name = input("Enter your name: ")
    print("Hello,", name)
    
def calcFloat():    
#Running a float * int and it repeates the int 5 times
    
    number = input("Enter number: ")
    print("You entered:", number)
    print("mutiplied * 5 =", number * 5)
    print("<That calculation comes when you dont use the eval command>")

#Running the same code with the eval command to evaluate the int when entered
    
    number1 = eval(input("Enter number: "))
    print("you entered: ", number1)
    print("mutiplied * 5 =", number1 * 5)
                   
#purpose: convert cups to ounces and milliliters
#input: cups
#output: ounces and milliliters [c cups = o oz = m mL]

def cupConverter():
    
    #CONVERSION FACTOR
    CUPS_TO_OUNCES = 8
    OZ_TO_MIL = 29.57

    #Display name of program
    print("Cup Converter")
    print()

    #ask user for number of cups
    cups = eval(input("Enter numbeber of cups: "))

    #calc number of ounces
    ounces = cups * CUPS_TO_OUNCES

    #calc number of milliliters
    ml = ounces * OZ_TO_MIL

    #display results of calculation
    print(cups, "cups =", ounces, "ounces =", ml, "milliliters")
    
    
    
    
    
    
    
