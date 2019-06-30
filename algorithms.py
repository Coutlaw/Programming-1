# algorithms.py
# student 1 = Zhou Ni
# student 2 = Cass Outlaw


##Code to look at runtime for linear vs. binary search.
##
##----------
##
##List with 49 elements.
##
##Find 5 - beginning of list
##Linear ->  1e-05 seconds.
##Binary -> 1e-05 seconds.
##
##Find 158 middle of list
##Linear -> 2e-05 seconds.
##Binary -> 1e-05 seconds.
##
##Find 282 - end of list
##Linear -> 4e-05 seconds.
##Binary -> 1e-05 seconds.
##
##Find  283 - not in list
##Linear -> 4e-05 seconds.
##Binary -> 1e-05 seconds.
##
##----------
##
##List with 10000950 elements.
##
##Find 57 - beginning of list
##Linear -> 1e-05 seconds.
##Binary -> 3e-05 seconds.
##
##Find 500000 - middle of list
##Linear -> 0.25047 seconds.
##Binary -> 3e-05 seconds.
##
##Find 10000999 - end of list
##Linear - 5.1425 seconds.
##Binary -> 3e-05 seconds.
##
##Find 10001000 - not in list

##Code to look at runtime for selection sort vs. Python's list sort.
##
##Sorting list with 10000 elements.
##
##Selection sort -> 8.63885 seconds.
##Python's sort -> 0.00354 seconds.

def readData(filename):
    infile = open(filename)
    data = infile.read()
    group = data.split("\n")
    newList =[]
    for i in range(len(group)):
        line = group[i]
        values = line.split()
        for j in range(len(values)):
            pos = int(values[j])
            newList.append(pos)
     
    return newList

def isInLinear(searchVal, values):
    inList = False
    i = 0
    while i < len(values) and int(values[i]) != searchVal:
        i += 1
    if i == len(values):
        inList = False
    else:
        inList == True
    return inList
        
        
def isInBinary(searchVal, values):
    low = 0
    high = len(values) -1
    while low <= high:
        mid = (low + high) //2
        item = values[mid]
        if searchVal == item:
            return True
        elif searchVal < item:
            high = mid -1
        else:
            low = mid +1
    return False

def selSort(values):
    n = len(values)
    for front in range(0, n-1):
        mins = front
        for i in range(front+1, n):
            if values[mins] > values[i]:
                mins = i
        temp = values[front]
        values[front] = values[mins]
        values[mins] = temp
     
    

def main():
    file = "dataSorted.txt"
    data = readData(file)
    searchVal = 100
    print(isInLinear(searchVal, data))

    searchVal = 5
    print(isInBinary(searchVal, data))

    values = [100, 10, 8 , 504, 12, 57, 20, 30000, 4, 19]
    selSort(values)
    print(values)
    
                       
    
