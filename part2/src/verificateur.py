def verificateurClique(graph, vertexOfClique):
	sets = [v for i, v in enumerate(graph[2]) if i in vertexOfClique]
	for i, s in enumerate(sets):
		s.add(vertexOfClique[i])
	for i, s in enumerate(sets[1:]):
		sets[0].intersection_update(s)
	return set(vertexOfClique).issubset(sets[0])


def verificateur3Coloration(graph, colorationByVertex):
	for edge in graph[1]:
		if colorationByVertex[edge[0]] == colorationByVertex[edge[1]] and all(colorationByVertex[v] != -1 for v in edge):
			return False, edge
	return True, ()
