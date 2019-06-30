from math import *
def main():
    num1 = 1.o
    num2 = .9999999
    if abs(num1 - num2) < .0001:
        print("equal")

    else:
        print("not")

def infinityLoops():
    num = 15
    #without the statement making the loop false this is an infinate loop
    while num > 10:
        print(num)
        
    print("done")

def indefinateLoop():
    num = 15
    while num > 10:
        print(num)
        num -= 1
        
    print("done")
def password():
    #demorgans's law
    # not x > 5 == x <= 5
    pwd = input("Enter password")
    while not(len(pwd) >= 10):
        print("must be longer")
        pwd = input("Enter password")
        
def passNoA():
    pwd = input("Enter password")
    while pwd[0] != "a":
        
