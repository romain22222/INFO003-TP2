import sys
from pycosat import solve
from pysat.card import CardEnc, EncType

from graph import newGraph
from verificateur import verificateur3Coloration


def solve3Coloration(graph, isVerbose):
	"""
	Résout le problème 3-Coloration
	:param isVerbose: 
	:param graph: graphe G
	:return: cherche s'il existe une clique de taille
	`size' dans G.
	"""

	if isVerbose:
		print("Graphe d'entrée")
		print(graph)

	n = graph[0]

	"""
	Mets dans cnf une double variable par paire de couleur / sommet
	0n+1 -> 1n = rouge
	1n+1 -> 2n = bleu
	2n+1 -> 3n = vert
	"""
	cnf = CardEnc.equals([i for i in range(1, 3 * n + 1)], bound=n, top_id=n, encoding=EncType.seqcounter)

	"""
	Pour chaque sommet, on ajoute la contrainte qu'il ne peut pas avoir deux couleurs
	"""
	for i in range(1, n + 1):
		cnf.append([-i, -(i + n)])
		cnf.append([-i, -(i + 2 * n)])
		cnf.append([-(i + n), -(i + 2 * n)])

	"""
	Pour chaque paire de sommets (u,v), si (u,v) est une arête,
	on ajoute la contrainte qu'ils ne peuvent pas avoir la même couleur
	"""
	for e in graph[1]:
		cnf.append([-(e[0]+1), -(e[1]+1)])
		cnf.append([-(e[0]+1 + n), -(e[1]+1 + n)])
		cnf.append([-(e[0]+1 + 2 * n), -(e[1]+1 + 2 * n)])

	if isVerbose:
		print("Entrée pour le SAT solveur")
		print(cnf)

	solutionSAT = solve(cnf)
	if isVerbose:
		print("Solution pour SAT")
		print(solutionSAT)

	return [] if solutionSAT == "UNSAT" else translateSolution(solutionSAT[:3*n], n)


def translateSolution(sol, n):
	colors = [-1] * n
	for v in sol:
		if v > 0:
			colors[(v - 1) % n] = (v - 1) // n
	return colors


if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("usage : python3 solve3Coloration.py <filename> [-v]")
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

	solution = solve3Coloration(g, verbose)

	print("Solution pour le problème 3-Coloration :")
	if solution:
		print(solution)
		print("Vérification de la solution : " + str(verificateur3Coloration(g, solution)) + ".")
	else:
		print("Pas de coloration.")
