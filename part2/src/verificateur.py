def verificateurClique(graph, vertexOfClique):
	sets = [v for i, v in enumerate(graph[2]) if i in vertexOfClique]
	for i, s in enumerate(sets):
		s.add(vertexOfClique[i])
	for i, s in enumerate(sets[1:]):
		sets[0].intersection_update(s)
	return set(vertexOfClique).issubset(sets[0])


def verificateur3Coloration(graph, colorationByVertex):
	for edge in graph[1]:
		if colorationByVertex[edge[0]] == colorationByVertex[edge[1]] and all(
				colorationByVertex[v] != -1 for v in edge):
			return False, edge
	return True, ()


def verificateur3CliquesCoverage(graph, cliques):
	allV = set(range(graph[0]))
	for clique in cliques:
		allV.difference_update(clique)
	if len(allV) != 0:
		return False, "Not all vertices are covered"
	for clique in cliques:
		if not verificateurClique(graph, clique):
			return False, "The clique " + str(clique) + " is not a clique"
	return True


def verificateur3SAT(problem, solution):
	for clause in problem[1]:
		if all(solution[abs(litteral) - 1] != litteral for litteral in clause):
			return False, clause
	return True, ()
