#Cass D. Outlaw
#Homework 2 CSCI 220 spring 2016
#
#   cdTime.py
#   Input:  number of track on album, time of track in minutes
#           time of track in seconds
#   Output: sum of time on all tracks

##Pseudocode:
##1. ask user to input: <tracks> <timeMin> <timeSec>
##2. Run loop summation for number of seconds on track
##3. Calculate total number seconds on cd
##4. Convert seconds to minutes and seconds 
##5. Calculate monthly interest charge
##6. Round all outputs to 2 decimal places
##7. Output <averageDailyBalance>, <monthlyPercentage>, <interestCharge>

def cdTime():
    #statement of purpose
    print("the purpose of this program is to calculate", end = " ")
    print("the amount of time on a CD")
    
    #user input step 1
    tracks = eval(input("Enter the nubmer of tracks on your CD: "))

    #initilize loop
    totalTime = 0
    #user input into loop step 2
    for i in range(tracks):
        #user input and convert data to time in seconds
        timeMin = (eval(input("Enter track time minutes: "))
        timeSec = eval(input("Enter track time seconds: "))
        #calculate total time in seconds
        extraMinutes = timeSec // .60
        time
        totalTime = 
                
        #display running total after input

    #convert total time in seconds to refined time
    totalMin = totalTime // .60
    totalSec = totalTime % .60
    totalMin = round(totalMin, 0)
    totalSec = round(totalSec, 2)

    print("Total Playing time on the CD is:", totalMin, end = " " )
    print("Minutes and", totalSec, "seconds")
