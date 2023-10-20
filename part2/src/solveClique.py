import sys
from pycosat import solve
from pysat.card import CardEnc, EncType

from graph import newGraph
from verificateur import verificateurClique


def solveClique(graph, sizeCliqueWanted, isVerbose):
	"""
	Résout le problème Clique
	:param isVerbose: 
	:param graph: graphe G
	:param sizeCliqueWanted: taille de la clique recherchée
	:return: cherche s'il existe une clique de taille
	`size' dans G.
	"""

	#  La suite est à compléter/modifier
	#  (décommentez petit à petit les lignes commençant par #)

	"""
	Si c'est possible pour votre structure de données, vous pouvez afficher le graphe
	"""
	if isVerbose:
		print("Graphe d'entrée")
		print(graph)

	"""
	Mettre dans n le nombre de sommets du graphe
	"""
	n = graph[0]
	"""
	Supprimer la ligne suivante :
	elle sert juste à ce que ça compile tant que la ligne d'avant n'est pas traitée
	"""
	# n = size + 1

	"""
	Nos variables seront X1,...,Xn
	On voudrait que Xi soit vraie si la clique contient le sommet (i-1)
	"""

	"""
	On veut que la clique soit de taille `size'.
	Donc parmi les n variables X1,...,Xn, exactement `size' doivent
	être vraies.
	Déjà n variables sont utilisées, donc les nouvelles variables
	commenceront à n+1.
	"""
	cnf = CardEnc.equals([i for i in range(1, n + 1)], bound=sizeCliqueWanted, top_id=n, encoding=EncType.seqcounter)

	"""
	Pour chaque paire de sommets (u,v), si (u,v) n'est pas une arête,
	on rajoute la contrainte qu'une des extrémités ne doit pas appartenir
	à la clique.
	"""
	for u in range(1, n+1):
		for v in range(u+1, n+1):
			if not (u-1, v-1) in graph[1]:
				cnf.append([-u, -v])

	if isVerbose:
		print("Entrée pour le SAT solveur")
		print(cnf)

	solutionSAT = solve(cnf)
	if isVerbose:
		print("Solution pour SAT")
		print(solutionSAT)

	"""
	Si le SAT-solver n'a pas trouvé de solution, il renvoit "UNSAT".
	Sinon, il renvoit une liste d'entiers [l1, l2, l3, ...]
	Si l1 = 1 alors X1 est True
	Si l1 = -1 alors X1 est False
	Les variables l(n+1), l(n+2), ... ont été créées pour la contrainte de
	cardinalité et ne nous intéressent pas.
	En conclusion, le noeud i-1 est dans la clique si i est dans solutionSAT
	"""
	return [] if solutionSAT == "UNSAT" else solutionSAT[:n]


if __name__ == '__main__':
	if len(sys.argv) < 3:
		print("usage : python3 solveClique.py <filename> <size_clique> [-v]")
		exit(1)
	filename = sys.argv[1]
	size = None
	try:
		size = int(sys.argv[2])
	except ValueError:
		print("Le deuxième argument <size_clique> doit être un entier.")
		exit(1)
	if len(sys.argv) > 3 and sys.argv[3] in ["-v", "--verbose"]:
		verbose = True
	else:
		verbose = False

	"""
	Récupérer le graphe stocké dans le fichier <filename>
	"""
	g = newGraph(filename)

	solution = solveClique(g, size, verbose)

	print("Solution pour le problème Clique")
	if solution:
		cliqueFound = [i for i in range(len(solution)) if solution[i] > 0]
		print(cliqueFound)
		print("Vérification de la solution : " + str(verificateurClique(g, cliqueFound)) + ".")
	else:
		print("Pas de clique de taille " + str(size) + ".")

