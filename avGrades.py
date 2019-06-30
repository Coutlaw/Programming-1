def avGrades():
    numGrades = 30
    gradeTotal = 0
    for i in range(numGrades):
        grade = eval(input("Enter grade" +str(i+1) +": "))
        gradeTotal += grade

    average = gradeTotal / numGrades

    print("Your average is:", average)
