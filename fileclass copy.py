#file usages
#using file.txt on desktop
#files for use have to be in the same folder as the program

def readFile():

    #creating a variable that connects to a file
    infile = open("data.txt")

    #ignorning lines
    numHeader = 3
    for i in range(numHeader):
        line = infile.readline()
        print(line)
    
    total = 0
    for line in infile:
        parts = line.split()
        name = parts[0]
        sibs = eval(parts[1])
        print(name + " has " + str(sibs) + " siblings")
        total += sibs

    print("\nTotal num sibs: " + str(total))
    #when this code is run it will leave white space because the file is
        #read as name\t to create a carridge return
    
def grades():

    infile = open("grades.txt")

    numHeader = 2
    for i in range(numHeader):
        line = infile.readline()

    for line in infile:
        total = 0
        average = 0
        parts = line.split()
        name = parts[0]
        grades = parts[1:]
        # will turn grade into a variable in the list grades
        for grade in grades:
            total += eval(grade)
        average = total/len(grades)

        print(name + " average " + str(round(average, 2)))
        
    
        
def encrypt():
    name = input("enter your name: ")

    for letter in name:
        print(ord(letter), end = " ")
        
        
