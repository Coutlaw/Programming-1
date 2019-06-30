def main():
    infile = open("testText.txt")
    file = infile.read()
    lines = file.split("\n")
    print(lines)
    for i in range(len(lines)-1):
        data = lines[i]
        words = data.split()
        first = words[0]
        print(first)
