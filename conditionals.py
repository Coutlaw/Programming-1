def vote():
    age = eval(input("Enter your age: "))
    #called a two way conditional
    if age >= 18:
        print("You can vote")
    else:
        print("No you cant vote")

#nested ifs
def vote2():
    age = eval(input("Enter your age: "))
    #multiple if statements
    if age >= 18:
        print("You can vote")
        #nested if statements
        if age >= 21:
            print("your can buy beer")
        else:
            print("you cant buy beer")
    else:
        print("No you cant vote")

#complex conditional
def vote2():
    age = eval(input("Enter your age: "))
    #multiple if statements
    if age >= 18 and age >= 21:
        print("beer and vote")
    else:
        if age >= 18:
            print("vote")
        else:
            print("neither")
            
def even():
    num = eval(input("Enter number: "))
    #program will do modd operator first before running code
    if num % 2 == 0:
        print("even")
    else:
        print("odd")
        
def even2():
    num = eval(input("enter number: "))

    if type(num) == int and num % 2 == 0:
        print("even")
    elif type(num) == int and num % 2 != 0:
        print("odd")
    else:
        print("you did not enter an integer")

def avg():
    data = input("Enter your average: ")
    if type(eval(data)) == int:
        
        avg = eval(data)
        if avg > 100:
            print("cannot exceede 100")
        elif avg >= 90 and avg <= 100:
            print("A")
        elif avg >= 80:
            print("B")
        elif avg >= 70:
            print("C")
        elif avg >= 60:
            print("D")
        elif avg >= 0:
            print("F")
        elif avg < 0:
            print("less than zero")
    else:
        print("You did not enter a valid number!")
        
        
        
            
    

