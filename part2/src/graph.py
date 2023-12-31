def newGraph(filename):
	edges = []
	size = 0
	with open(filename, 'r') as f:
		lines = f.readlines()
		for line in lines:
			if line[0] == 'e':
				edges.append((int(line.split()[1]), int(line.split()[2])))
			if line[0] == 'p':
				size = int(line.split()[2])
	return [size, edges, [set([j for j in range(size) if (i, j) in edges or (j, i) in edges]) for i in range(size)]]


def extract3SAT(filename):
	logicExps = []
	with open(filename, 'r') as f:
		lines = f.readlines()
		nbVar = int(lines[0])
		for line in lines[1:]:
			logicExps.append([int(v) for v in line.split(" ")])
	return [nbVar, logicExps]
