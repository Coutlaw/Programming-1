def calcChange():

    #input cost and payment made
    cost = eval(input("Enter how much the purchase was for $"))
    payment = eval(input("Enter payment ammount $"))

    #calculate change amount
    changeAmount = payment - cost
    changeAmount = round(changeAmount, 2)
    print("your change is $"+ str(changeAmount))

    #axx = amount of currency given back
    #rxx = remainder after division 
    a20s = changeAmount // 20
    r20s = changeAmount % 20
    a10s = r20s // 10
    r10s = r20s % 10
    a5s = r10s // 5
    r5s = r10s % 5
    a1s = r5s // 1
    r1s = r5s % 1
    aQs = r1s // .25
    rQs = r1s % .25
    aDs = rQs // .10
    rDs = rQs % .10
    

    print("Number of 20s given back:", a20s)
    print("Number of 10s given back:", a10s)
    print("Number of 5s given back:", a5s)
    print("Number of 1s given back:" , a1s)
    print("Number of quarters given back:", aQs)
    print("Number of dimes given back:", aDs)
    
    

    
    
