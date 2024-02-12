import graphs as gr
import pq


def a_star(g, start, h):
	open = pq.PriorityQueue()
	open.push(start, [start], 0+h[start])
	explored = []

	while not open.is_empty():
		curr, path, f_cost_curr = open.pop()
		explored.append(curr)

        #Check if you want

		if h[curr]==0:
			print("\nFound BEST path - ", path)
			print("\nWith a cost = ", f_cost_curr)
			return
			
		print("\nCurrently at -", curr)
		
		for neighbour, e_cost in g.adj_list[curr]:
			n_path = path.copy()
			n_path.append(neighbour)

			g_cost_neighbour = (f_cost_curr - h[curr]) + e_cost
			f_cost_neighbour = g_cost_neighbour + h[neighbour]
			print("\t--> ", neighbour, "\t= G = ", g_cost_neighbour, "\t F = ", f_cost_neighbour)


			if neighbour not in explored:
				s = 0
				for i in range(len(open.queue)):
					
					if(open.queue[i][0] == neighbour): # Already exists, so compare gcosts (coz h is same anyway)
						previous_f = open.queue[i][2]
						if(f_cost_neighbour < previous_f):
							s = 1
							open.queue[i] = (neighbour, n_path, f_cost_neighbour)
							break
				if(s==0):
					open.push(neighbour, n_path, f_cost_neighbour)
							
						
				


if __name__ == "__main__":
	g = gr.Graph(10)
	g.define_vs(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
	edges = [('A', 'F', 3), ('A', 'B', 6), ('B', 'D', 2), ('B', 'C', 3),
			('C', 'E', 5), ('C', 'D', 1), ('E', 'J', 5), ('E', 'I', 5), 
			('E', 'D', 8), ('J', 'I', 3), ('I', 'G', 3), ('I', 'H', 2),
			('G', 'F', 1), ('F', 'H', 7)]
	for a, b, w in edges:
		g.add_edge(a, b, w)
		g.add_edge(b, a, w)

	h = {
	'A':10, 
	'B':8, 
	'C':5, 
	'D':7, 
	'E':3, 
	'F':6, 
	'G':5, 
	'H':3, 
	'I':1, 
	'J':0
	}

	a_star(g, 'A', h)