def numerology(name):
#    name = input("enter your name ")
    name = name.lower()
    total = 0
    for i in range(len(name)):
        value = ord(name[i]) - (ord("a") - 1)
        total += value
        
    return total
        

def main():
    score = numerology("cass")
    print(score)
