from itertools import combinations


def isIndependentSet(edges, nodes):
	for u, v in combinations(nodes, 2):
		if (u, v) in edges or (v, u) in edges:
			return False
	return True


def findAllMaximumIndependantSets(graph):
	tempSets = []
	for node in range(graph[0]):
		isStable = True
		storage = []
		for v in tempSets:
			newSet = v.copy()
			newSet.add(node)
			if isIndependentSet(graph[1], newSet):
				isStable = False
				storage.append(newSet)
		tempSets.extend(storage)
		if isStable:
			tempSets.append({node})
	for x in tempSets:
		isStable = True
		for y in tempSets:
			if x != y and x.issubset(y):
				isStable = False
				break
		if isStable:
			yield x


def findCheckable(edgesToCheck, colorToCheck):
	areCheckable = set()
	for i, edge in enumerate(edgesToCheck):
		if edge[0] in colorToCheck:
			areCheckable.add(edge[1])
		if edge[1] in colorToCheck:
			areCheckable.add(edge[0])
	return areCheckable


def isBipartite(graph):
	evenColor = {graph[1][0][0]}
	oddColor = {graph[1][0][1]}
	edgesToCheck = graph[1][1:]
	edges = graph[1][:]
	while len(edgesToCheck) > 0:
		areCheckableOdd = findCheckable(edges, evenColor)
		areCheckableEven = findCheckable(edges, oddColor)
		if areCheckableOdd == oddColor and areCheckableEven == evenColor:
			oneEdge = edgesToCheck.pop()
			evenColor.add(oneEdge[0])
			oddColor.add(oneEdge[1])
			continue
		evenColor.update(areCheckableEven)
		oddColor.update(areCheckableOdd)
		if evenColor.intersection(oddColor) != set():
			return False, []
		edgesToCheck = [edge for edge in edgesToCheck if len(areCheckableOdd.union(areCheckableEven).intersection(edge)) < 2]
	return True, [1 if i in evenColor else (0 if i in oddColor else -1) for i in range(graph[0])]

