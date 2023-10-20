from random import randrange

from graphDeep import findAllMaximumIndependantSets, isBipartite
from reader import reader
from verificateur import verificateur


def solvBackTrackingRec(graph, k, color):
	if k == graph[0]:
		return True
	for i in range(3):
		color[k] = i
		if verificateur(graph, color)[0]:
			if solvBackTrackingRec(graph, k + 1, color):
				return True
	color[k] = -1
	return False

def colorInitializer(size):
	return [-1 for _ in range(size)]

def solvBackTracking(graph_filename):
	graph = reader(graph_filename)
	color = colorInitializer(graph[0])
	return solvBackTrackingRec(graph, 0, color), color

def colorRandomizer(size):
	return [randrange(3) for _ in range(size)]


def findWrongEdges(graph, color):
	wrongEdges = []
	for edge in graph[1]:
		if color[edge[0]] == color[edge[1]]:
			wrongEdges.append(edge)
	return wrongEdges


def solvRandom(graph_filename):
	graph = reader(graph_filename)
	for _ in range(3):
		color = colorRandomizer(graph[0])
		for i in range(len(graph[1])*2):
			K = findWrongEdges(graph, color)
			if len(K) == 0:
				return True, color
			r = randrange(len(K))
			color[K[r][randrange(2)]] = randrange(3)
	return False, []


def solvLawler(graph_filename):
	graph = reader(graph_filename)
	for n in findAllMaximumIndependantSets(graph):
		testG = [graph[0], [e for e in graph[1] if e[0] not in n and e[1] not in n]]
		isB, foundColoration = isBipartite(testG)
		if isB:
			return True, [2 if v in n else (foundColoration[v] if foundColoration[v] != -1 else 0) for v in range(graph[0])]
	return False, []
