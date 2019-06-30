# Lab7.py
# Name 1:
# Name 2:



def numberWords():
    infile = open("rawWords.txt")
    outfile = open("rawWordsOut.txt", "w")
    text = infile.read()
    
    info = text.split()

    for i in range(len(info)):
        print(str(i+1) + ".", info[i], file = outfile)

    infile.close()
    outfile.close()
    

def hourlyWages(infilename, outfilename):
    infile = open(infilename)
    outfile = open(outfilename, "w")
    text = infile.read()
    lines = text.split("\n")
    
    for i in range(len(lines)):
        
        info = lines[i]
        data = info.split()
        print(data[2])
        newWage = 1.65 + int(data[2])
        payment = newWage * int(data[3])
        print(data[0], data[1], newWage, payment, file = outfile)
        
    infile.close()
    outfile.close


    
    

