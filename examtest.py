def average():
    infile = open("shotData.txt")
    outfile = open("average.txt", "w")
    file = infile.read()
    lines = file.split("\n")
    
    for i in range(len(lines) - 1):
        info = lines[i]
        data = info.split()
        print(data)
        name = data[0] + " " + data[1]
        points = data[3:]
        total = 0
        average = 0
        for j in range(len(points) -1):           
            total += int(points[j])
            average = total / len(points)
        print(name + ":", average, file = outfile)

    infile.close()
    outfile.close()

def test():
    word = "python"
    for ch in word:
        print(ch, end = " ")
