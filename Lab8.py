# CSCI 220L - Lab 8 Solutions
#
# Name 1: Vasily Kichigin
#
# Name 2:Cass Outlaw
#

#function to test code in problem 4.  Do not run
#until addTen() is written
def testTens():
    values = [5, 2, -3]
    print(values)
    addTen(values)
    print(values)
def formatPractice ():
    print ("It's raining {1} and {0}.".format("dogs", "cats"))
    ## B
    print ("{0:3.2f}, {1:5}".format(2.3, .4567))
    ## C
    print ("Time left {0:02}:{1:05.2f}".format(3, 7.4589))
    ## D
    print ("{0} {1}: {2:5.2f}".format("Steph", "Curry", 43.75432))

def encode(word, key):
    numReps = len(word)
    for i in range(numReps):
        value = ord(word[i]) + key
        print(chr(value), end = "")

def encodeBetter():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    size = len(alphabet)
    word = input("enter your word: ")
    key = eval(input("Enter your key: "))
    numReps = len(word)
    word = word.lower()

    for i in range(numReps):
        letter = word[i]
        position = alphabet.find(letter)
        newValue = position + key
        adjust = newValue % size
        newLetter = alphabet[adjust]
        print(newLetter, end = "")
        
        
def addTen (nums):
    numReps = len(nums)
    for i in range(numReps):
        nums[i] += 10

def chaos(x1, x2, iteration):
    k = 3.9
    print("index \t", x1, "\t", x2)
    print("-" * 30)


    for i in range(1, iteration):
        value = k*(x1)*(1-x1)
        value2 = k*(x2)*(1-x2)
        
        print(i, "\t", value, "\t", value2)

##def squareEach(nums):
##    numReps = len(nums)
##    for i in range(numReps):
##        nums[i] *= nums[i]

def sumList(nums):
    numReps = len(nums)
    total = 0
    for i in range(numReps):
        total += nums[i]
    return total
        
        


def toNumbers(strList):
    numReps = len(strList)
    for i in range(numReps):
        strList[i] = eval(strList[i])
    print(strList)
        
        

        
def sumOfSquares():
    
    nums = [5, 12]
    print(sumList(nums))
    
 #   print(nums)
        
        
    

def main():
    nums = [5, 12]
    squareEach(nums)
    print(nums)
    
##    nums = [5,2,-3]
##    addTen (nums)
##    print (nums)
##    encode("hello", 3)
