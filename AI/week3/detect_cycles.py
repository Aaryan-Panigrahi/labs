import graphs as gr

def find_cycles(g):
	visited = []
	cycle_rn = []

	for vno in range(g.n):
		if vno not in visited:
			search(g, vno, visited, cycle_rn)

def search(g, vno, visited, cycle_rn):

	visited.append(vno)
	cycle_rn.append(vno)

	for adj in g.adj_list[vno]:
		if adj not in visited:
			search(g, adj, visited, cycle_rn.copy())
		else:
			#we reached something we already visited
			#check if it's in the cycle_rn
			if adj in cycle_rn:
				print('Found a cycle')
				print(adj)
				print(cycle_rn[cycle_rn.index(adj):])
				cycle_rn.clear()
				return
				

			

if __name__ == "__main__":
	g = gr.Graph(4)
	g.define_vs([0, 1, 2, 3])
	g.add_unw_edge(0, 1)
	g.add_unw_edge(0, 2)
	g.add_unw_edge(1, 2)
	g.add_unw_edge(2, 0)
	g.add_unw_edge(2, 3)
	g.add_unw_edge(3, 3)

	# g.p_adj_list()

	find_cycles(g)



