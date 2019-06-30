# algorithms.py
# lap 13
# sorted data file : dataSorted.txt
def readData(filename):
	infile = open(filename)
	data = infile.read()
	group = data.split("\n")
	dataList = []
	for i in range(len(group)):
		line = group[i]
		values = line.split()
		for j in range(len(values)):
			pos = values[j]
			dataList.append(pos)
			
	return dataList