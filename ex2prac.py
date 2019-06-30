def getGrades():
    numGrades = eval(input("Enter number of grades: "))
    grades = ""
    for i in range(numGrades):
        grade = input("Enter grade " + str(i+1) + ": ")
        grades += grade + " "

    print("Your grades are:", grades)

    score = grades.split()
    total = 0
    for i in range(len(score)):
        total += int(score[i])

    average = total / len(score)
    print("Your average is:", average)

def main():
    text = "i see 4 of u"
    x = text[:3]
    print(x)
