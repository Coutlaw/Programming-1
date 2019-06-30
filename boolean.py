def isEven(num):
    # this is what the boolean function does
##    if num % 2 == 0
##        rtnVal = True
##    else:
##        rtnVal = False
    
    return num % 2 == 0

def countVowels(msg):
    text = msg.lower()
    total = 0
    for ch in text:
        if ch in "aeiou":
            total += 1
    return total

def counts(msg):
    text = msg.lower()
    counts = [0, 0, 0,]
    for ch in text:
        if ch in "aeiou":
            counts[0] += 1
        elif ch in " ":
            counts[1] += 1
        else:
            counts[2] += 1
    return counts
        
            


    
def main():
    sent = input("Enter sentence: ")
    info = counts(sent)
    print(info[0], "vowels \n", info[1], "spaces \n", info[2], "constas")

    
##    sent = input("enter sentence: ")
##    numVowels = countVowels(sent)
##    print(str(numVowels) + "in \"" + sent + "\"")



##    for i in range(5):
##        even = isEven(i)
##        print(i, even)
