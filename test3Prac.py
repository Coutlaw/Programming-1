def main():
    s = 0
    n = 2
    while s < 30 and n < 7:
        count = 0
        while count < 2:
            s += count
            count += 1
            print("s = " + str(s) , "count = " + str(count))
        n += 2
        print("num = " + str(n))
