import sys
from graph import extract3SAT
from solve3Coloration import solve3Coloration
from verificateur import verificateur3SAT


def solve3SAT(problem, isVerbose):
	"""
	Résout le problème 3-SAT en utilisant le problème 3-Coloration
	:param isVerbose: 
	:param problem:
	:return:
	"""
	nbVar = problem[0]
	V = 0
	F = 1
	N = 2
	edges = [(V, F), (V, N), (F, N)]
	countNodes = 3
	#     0 ->   nbVar-1 : Val_i
	# nbVar -> 2*nbVar-1 : Opp_i
	for v in range(3, nbVar + 3):
		edges.append((v, v + nbVar))
		edges.append((v, N))
		edges.append((v + nbVar, N))
	countNodes += nbVar*2
	for i, exp in enumerate(problem[1]):
		for j in range(3):
			edges.append((N, countNodes + j))
		for j, v in enumerate(exp):
			if v > 0:
				edges.append((countNodes + j, nbVar + v + 2))
			else:
				edges.append((countNodes + j, -v + 2))
		"""
		a = 0, b = 1, c = 2
		U = 3, V = 4, W = 5
		X = 6, Y = 7, Z = 8
		"""
		edges.append((countNodes, countNodes + 3))
		edges.append((countNodes + 1, countNodes + 4))
		edges.append((countNodes + 2, countNodes + 7))
		edges.append((countNodes + 3, countNodes + 4))
		edges.append((countNodes + 3, countNodes + 5))
		edges.append((countNodes + 4, countNodes + 5))
		edges.append((countNodes + 5, countNodes + 6))
		edges.append((countNodes + 6, countNodes + 7))
		edges.append((countNodes + 6, countNodes + 8))
		edges.append((countNodes + 7, countNodes + 8))
		edges.append((countNodes + 8, F))
		edges.append((countNodes + 8, N))
		countNodes += 9
	graph = [countNodes, edges, [set([j for j in range(countNodes) if (i, j) in edges or (j, i) in edges]) for i in range(countNodes)]]
	res = solve3Coloration(graph, isVerbose)
	return [] if not res else [i-2 if res[i] == res[0] else -i+2 for i in range(3, nbVar + 3)]


if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("usage : python3 solve3SAT.py <filename> [-verif] [-v]")
		exit(1)
	filename = sys.argv[1]
	if len(sys.argv) > 3 and sys.argv[2] in ["-verif", "--verif"]:
		solveToCheck = eval(sys.argv[3])
		print("Solution à vérifier : " + str(solveToCheck) + ".")
		print("Vérification de la solution : " + str(verificateur3SAT(extract3SAT(filename), solveToCheck)) + ".")
		exit(0)
	if len(sys.argv) > 2 and sys.argv[2] in ["-v", "--verbose"]:
		verbose = True
	else:
		verbose = False

	"""
	Récupérer le graphe stocké dans le fichier <filename>
	"""
	prob = extract3SAT(filename)
	print("Problème 3SAT :", prob)

	solution = solve3SAT(prob, verbose)

	print("Solution pour le problème 3SAT :")
	if solution:
		print(solution)
		print("Vérification de la solution : " + str(verificateur3SAT(prob, solution)) + ".")
	else:
		print("Pas de solution.")
