#Cass D. Outlaw
#Homework 1 CSCI 220 spring 2016
#
#   intrest.py
#   Input:  annual percentage rate, net palance,
#           number of days in billing cycle, payment ammount,
#           how many days into the cycle the payment was made
#   Output: average daily balance, monthly percentage rate,
#           interst paid in a given month

##Pseudocode:
##1. ask user to input: <annualRate>, <netBalance>, <daysInCycle>,
##                      <payment>, <paymentDay>
##2. Calculate number of days in billing cycle after payment
##3. calculate average daily balance
##4. Calculate monthly percentage rate and convert to integer
##5. Calculate monthly interest charge
##6. Round all outputs to 2 decimal places
##7. Output <averageDailyBalance>, <monthlyPercentage>, <interestCharge>


def calcInterest():
    #Statement of purpose
    print("This program calculates your monthly interest charge")
    
    #Constants are
    monthsInYear = 12
    percentageConversion = 100

    #User input step 1
    annualRate = eval(input("Enter your annual interest rate: %"))
    netBalance = eval(input("Enter your previous account balance: $"))
    daysInCycle = eval(input("Number of days in your bill cylcle: "))
    payment = eval(input("Enter your last payment amount: $"))
    paymentDay = eval(input("What day of the cycle did you pay? "))

    #calculate days left in billing cycle after payment step 2
    daysLeftInCycle = daysInCycle - paymentDay
    
    #calculate average daily balance step 3
    step1 = netBalance * daysInCycle
    step2 = payment * daysLeftInCycle
    step3 = step1 - step2
    averageDailyBalance = step3 / daysInCycle

    #calculate monthly percentage rate and convert to integer step 4
    monthlyPercentage = annualRate / monthsInYear
    monthlyRate = monthlyPercentage / percentageConversion

    #calculate monthly interest charge step 5
    interestCharge = averageDailyBalance * monthlyRate
    
    #round resluts to 2 decimal places step 6
    averageDailyBalance = round(averageDailyBalance, 2)
    monthlyPercentage = round(monthlyPercentage, 2)
    interestCharge = round(interestCharge, 2)

    #output results of calculations
    #average daily balance, montly percentage and monthly interest
    print()
    print("According to what you entered:")
    print()
    print("Your average daily balance is $"+ str(averageDailyBalance))
    print()
    print("Your monthly percentage rate is %"+ str(monthlyPercentage))
    print()
    print("Your paying $"+ str(interestCharge), "in interest a month")
    
