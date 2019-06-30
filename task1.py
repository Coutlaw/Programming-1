def task1():
    #constants
    sSub0 = 1367
    alphaSubP = .3
    sigma = 5.67 * (10**(-8))

    #top of the atmosphere calculations (T4)
    tSub4 = (((sSub0 / 4)*(1-alphaSubP))/sigma)**(1/4)
    print("The value at the top of the atmosphere of T4 = " + str(round(tSub4,3)))
    
    #layer 4 (T3) calculations
    tSub3 = ((2*sigma*tSub4**4) / sigma)**(1/4)
    print("The value of T3 at layer 4 = " +str(round(tSub3, 3)))
 
    #layer 3 (T2) calculations
    tSub2 = (((2*sigma*tSub3**4)-(sigma*tSub4**4))/sigma)**(1/4)
    print("The value of T2 at layer 3 = " + str(round(tSub2,3)))
    
    #layer 2 (T1) calculations
    tSub1 = (((2*sigma*tSub2**4)-(sigma*tSub3**4))/sigma)**(1/4)
    print("The value of T1 at layer 2 = " + str(round(tSub1,3)))

    #layer 1 (TS) calculations
    tSubS = (((2*sigma*tSub1**4)-(sigma*tSub2**4))/sigma)**(1/4)
    print("The value of TS at layer 1 = " + str(round(tSubS,3)))

    
