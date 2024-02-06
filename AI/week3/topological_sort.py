import graphs as gr

def topological_sort(g):

	visited = [False]*g.n
	stack = []

	for i in range(g.n):
		if visited[i] == False:
			go_search(g, i, visited, stack)

	print(stack[::-1])


def go_search(g, vno, visited, stack):

	visited[vno] = True

	for v in g.adj_list[vno]:
		if visited[v[0]] == False:
			go_search(g, v[0], visited, stack)

	stack.append(vno)

if __name__ == "__main__":
	g = gr.Graph(6)
	g.define_vs([0, 1, 2, 3, 4, 5])
	g.add_edge(5, 2)
	g.add_edge(5, 0)
	g.add_edge(4, 0)
	g.add_edge(4, 1)
	g.add_edge(2, 3)
	g.add_edge(3, 1)

	topological_sort(g)