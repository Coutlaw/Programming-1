def classwork():
    n = 4
    total = 0
    for i in range(n):
        total = (i +1) **2
        print(total)

def average():
    numInt = eval(input("amount of numbers to be averaged: "))

    total = 0
    for i in range(numInt):
        integers = eval(input("Number: "))
        total = integers + total

    average = total / 2
    print(average)
    
