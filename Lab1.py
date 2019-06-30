## Lab1.py
## <Cass Outlaw>

##This function calculates the area of a rectangle
def calcRecArea():
    lenght = eval(input("Enter the lenght: "))
    width = eval(input("Enter the width: "))
    area = lenght * width
    print ("Area = ", area)

## This function calculates the volume of a rectangle
def calcVolRec():
    lenght = eval(input("Enter the lenght: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = lenght * width * height
    print = ("Volume =", volume)
    
##This function is to calculate shooting percentages
def shootingPercentage():
    taken = eval(input("Enter number of shots taken: "))
    made = eval(input("Enter number of shots made: "))
    percentage = made / taken * 100
    # round function rounds the total number of units displayed
    percentage = round(percentage, 2)
    print ("Your shooting percentage is = %"+ str(percentage))
    
##This function is to calculate shipping costs on a coffee order
def coffee():
    COST_PER_POUND = 10.50
    SHIPPING_COST = .86
    OVERHEAD = 1.50
    pounds = eval(input("How many pounds of coffee? "))
    cost = pounds * COST_PER_POUND
    shipping = pounds * SHIPPING_COST
    total = cost + shipping + OVERHEAD
    #str function turns the calculated int into a string and takes away the gap
    print ("If you order that many pounds of coffee it will cost $"+ str(total))
    
##This formula is to convert kilometers to miles
def kilometersToMiles():
    RATIO = 1.61
    kilometers = eval(input("Enter distance in kilometers "))
    miles = kilometers / RATIO
    print ("If you travel that many kilometers then you traveled", miles, "miles")
