def verificateur(graph, colorationByVertex):
	for edge in graph[1]:
		if colorationByVertex[edge[0]] == colorationByVertex[edge[1]] and all(colorationByVertex[v] != -1 for v in edge):
			return False, edge
	return True, ()
