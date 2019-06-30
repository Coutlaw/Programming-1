#Cass D. Outlaw
#Homework 2 CSCI 220 spring 2016
#
#   cdTime.py
#   Input:  number of track on album, time of track in minutes
#           time of track in seconds
#   Output: sum of time on all tracks

##Pseudocode:
##1. Ask user to input: <tracks> <timeMin> <timeSec>
##2. Run loop summation for minutes and seconds of songs
##3. User input: <timeMin>, <timeSec>
##4. Take summation of user input
##5. Find extra number of minutes from the total seconds entered
##5. Calculate total number of minutes and seconds
##6. Output <totalMin>, <totalSec>

def cdTime():
    #statement of purpose
    print("the purpose of this program is to calculate", end = " ")
    print("the amount of time on a CD")
    
    #user input step 1
    tracks = eval(input("Enter the nubmer of tracks on your CD: "))
    
    minutes = 0
    seconds = 0
    #user input into loop step 2
    for i in range(tracks):
        #user input and convert data to time in seconds step 3
        timeMin = eval(input("Enter track time minutes: "))
        timeSec = eval(input("Enter track time seconds: "))
        #total user input
        minutes = timeMin + minutes
        seconds = timeSec + seconds

    #find extra minutes from total seconds
    plusMin = seconds // 60
    
    #calculate total number of minutes and seconds remaining
    totalMin = minutes + plusMin
    totalSec = seconds % 60

    #output results of calculations
    print("Total Playing time on the CD is:", totalMin, end = " " )
    print("Minutes and", totalSec, "seconds")
    
def cdTime2():
    #statement of purpose
    print("the purpose of this program is to calculate", end = " ")
    print("the amount of time mutiple CDs")
    
    #user input step 1
    cds = eval(input("Enter the total number of CDs: "))
    
    totalMin = 0
    totalSec = 0
    for j in range(cds):
        tracks = eval(input("Enter the nubmer of tracks this CD: "))
        #user input into loop step 2
        minutes = 0
        seconds = 0
        for i in range(tracks):
            #user input and convert data to time in seconds step 3
            timeMin = eval(input("Enter track time minutes: "))
            timeSec = eval(input("Enter track time seconds: "))
            #total user input
            minutes = timeMin + minutes
            seconds = timeSec + seconds
            plusMin = seconds // 60
            minutes = minutes + plusMin
            seconds = seconds % 60
                  
        totalMin = totalMin + minutes
        totalSec = totalSec + seconds
        print("CD" +str(j + 1), "Total Time:", minutes, end = " ")
        print("Minutes and", seconds, "Seconds")  

    plusTotalMin = totalSec // 60
    totalMin = totalMin + plusTotalMin
    totalHours = totalMin // 60
    totalMin = totalMin % 60
    totalSec = totalSec % 60
            

    #output results of calculations
    print("Total Playing time on the CD is:",totalHours, end = " ")
    print("Hours", totalMin, "Minutes and", totalSec, "Seconds")
    
