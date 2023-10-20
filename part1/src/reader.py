def reader(filename):
	edges = []
	size = 0
	with open(filename, 'r') as f:
		lines = f.readlines()
		for line in lines:
			if line[0] == 'e':
				edges.append((int(line.split()[1]), int(line.split()[2])))
			if line[0] == 'p':
				size = int(line.split()[2])
	return [size, edges]