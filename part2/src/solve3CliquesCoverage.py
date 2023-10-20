import sys
from graph import newGraph
from solve3Coloration import solve3Coloration
from verificateur import verificateur3CliquesCoverage


def solve3CliquesCoverage(graph, isVerbose):
	"""
	Résout le problème 3-Cliques Coverage
	:param isVerbose: 
	:param graph: graphe G
	:return:
	"""
	tempGraph = [graph[0], [], [set(range(graph[0])).difference(graph[2][i]) for i in range(graph[0])]]
	for i in range(graph[0]):
		for v in set(range(graph[0])).difference(graph[2][i]):
			if v > i:
				tempGraph[1].append((i, v))
	res = solve3Coloration(tempGraph, isVerbose)
	return res if res == [] else [[i for i in range(graph[0]) if res[i] == j] for j in range(3)]


if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("usage : python3 solve3CliquesCoverage.py <filename> [-v]")
		exit(1)
	filename = sys.argv[1]
	if len(sys.argv) > 2 and sys.argv[2] in ["-v", "--verbose"]:
		verbose = True
	else:
		verbose = False

	"""
	Récupérer le graphe stocké dans le fichier <filename>
	"""
	g = newGraph(filename)

	solution = solve3CliquesCoverage(g, verbose)

	print("Solution pour le problème 3-Cliques Coverage :")
	if solution:
		print(solution)
		print("Vérification de la solution : " + str(verificateur3CliquesCoverage(g, solution)) + ".")
	else:
		print("Pas de cliques coverage.")
