#   Name: Cass Outlaw 
#   weightedAverage.py
#
#   Problem: create a program that the user can specify a file and have
#           and created a weighted average of various grades
#
#   input: <file> for the file name
#   output: <average> the weighted average for the student
#
#   Certification of Authenticity:
#   I certify that this homework is entirely my own work.

#define equation
def weightedAverage(file):
    #open the argument file specified by the user in the main funciton
    infile = open(file)
    #return file as a string
    data = infile.read()
    #turn file into list by the lines in the file
    line = data.split("\n")
    #count length of the list subracting the carraige return at the end
    lines = len(line) - 1
    #initilize the loop and repeat for the lenght of the file
    averages = 0
    for i in range(lines):
        # specify what line to modify
        content = line[i]
        # turn line into list of strings
        info = content.split()
        # create the name of the student from the list
        name = info[0] + " " + info[1]
        # create list of weights and grades
        grades = info[2:]
        #count how many grades are in list
        numGrades = int(len(grades) / 2)
        #initilize accumulation variable
        total = 0
        for j in range(numGrades):
            #first string in list is weight
                #j * 2 to access every other string in the list
            weight = eval(grades[j * 2])
            #second string in list is grade (and repeat)
                #j*2 + 1 to get every other string after the weight
            grade = eval(grades[(j * 2) + 1 ])
            # accumulate the grade * weight
            total += (weight * grade)

        # find weighted average and return the students name     
        average = total / 100
        
        print(name + str("'s average: "), round(average, 1))

        #create sumation of all averages
        averages += average
        #calculate the class average
        classAverage = averages / lines
    print("Class Average:", round(classAverage,1))

    infile.close()

#define a main function
def main():
    #ask user to specify what file to use
    file = input("Enter file name: ")
    # run weighted average with file name as the argument
    weightedAverage(file)
              
        
