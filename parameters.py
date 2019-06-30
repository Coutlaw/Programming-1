# input - 2 numbers through parameters
# output - sum returned
def add(op1, op2):
    total = op1 + op2
    # stores total as local value
    return total

def main():
    answer = add(4,7)
    print(answer)

#creating a program that calls another program to do the math and work
def power(op1, op2):
    total = op1 ** op2
    return total
def main2():
    num1 = eval(input("Enter the number: "))
    num2 = eval(input("Enter the power: "))
    
    answer = power(num1, num2)
    print(answer)

    #creating a program that will take what you enter
        #run it through another program and modify it
def sent(text):
    sent = text.lower()
    words = sent.split()
    return words
def main3():
    message = input("Enter your sentence: ")
    words = sent(message)
    print(words)

# program that accepts a list and returns a product

def func(group):
    ints = group.split()
    total = 1
    for i in range(len(ints)):
        total *= int(ints[i])
    return total

def main4():
    inputs = input("Enter numbers separated by a space: ")
    summation = func(inputs)
    print(summation)

#concatination program
def in(
