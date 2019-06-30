#Cass D. Outlaw
#Homework 2 CSCI 220 spring 2016
#
#   cdTime.py
#   Input:  number of CDs, number of tracks per cd, time in minutes
#           time in seconds 
#   Output: sum of time per cd, sum of ttotal play time

##Pseudocode:
##1. Ask user to input: <cds>
##2. Initilize outer loop with range <cds>
##3. User input: <tracks>
##4. Initilize inner loop wiht range <tracks>
##5. User input: <timeMin> <timeSec> per track
##6. Calculate Summation of inputs from step 5 per CD
##7. Calculate total number of minutes and seconds per CD
#### loop will repeat calculations per cd and track specified by user
##8. Calculate total time from all CDs
##9. Display summation per CD as entered
##10.Convert results from step 8 to hours, minutes, seconds



def cdTime():
    #statement of purpose
    print("the purpose of this program is to calculate", end = " ")
    print("the amount of time on mutiple CDs")
    
    #Step 1  ask user for number cd's
    cds = eval(input("Enter the total number of CDs: "))

    #Step 2 initilize outer loop variables at 0
    totalMin = 0
    totalSec = 0
    for j in range(cds):
        #Step 3 ask user for number of tracks
        tracks = eval(input("Number of tracks on CD"+str(j+1) +": "))
        #Step 4 initilize inner loop
        minutes = 0
        seconds = 0
        for i in range(tracks):
            #Step 5 ask user for minutes and seconds per track
            timeMin = eval(input("Minutes on track "+str(i+1)+ ": "))
            timeSec = eval(input("Seconds on track "+str(i+1)+ ": "))
            #Step 6 take summation of inputs
            minutes = timeMin + minutes
            seconds = timeSec + seconds
            #Step 7 calculate extra minutes from entered seconds
            plusMin = seconds // 60
            minutes = minutes + plusMin
            seconds = seconds % 60

        #Step 8 take running total of time from all entered CDs
        totalMin = totalMin + minutes
        totalSec = totalSec + seconds
        
        #Step 9 display time per CD as entered
        print("CD" +str(j + 1), "Total Time:", minutes, end = " ")
        print("Minutes and", seconds, "Seconds")  

    #Step 10 take totals from step 8 and convert to
        #hours, minutes, seconds
    plusTotalMin = totalSec // 60
    totalMin = totalMin + plusTotalMin
    totalHours = totalMin // 60
    totalMin = totalMin % 60
    totalSec = totalSec % 60

    #Output results of calculations
    print("Total playing time for", str(j+1), "CD(s) is:", end = " ")
    print(totalHours,"Hours", totalMin, end = " ")
    print("Minutes and", totalSec, "Seconds")
    
