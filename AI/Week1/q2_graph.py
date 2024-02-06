class edge:
	def __init__(self):
		self.v_from = None
		self.v_to = None
		self.cost = None

def get_edge(fr, to, c):
	e = edge()
	e.v_from = fr
	e.v_to = to
	e.cost = c

class Graph:
	def __init__(self):
		self.vertices = []
		self.edges = []
		self.adj_list = {}
		self.adj_mat = [[0 for i in range(4)] for j in range(4)]

	
	def add_edge(self, fr, to, c):
		self.edges.append(get_edge(fr, to, c))
		if fr not in self.adj_list:
			self.adj_list[fr] = []
		self.adj_list[fr].append([to, c])
		self.adj_mat[fr-1][to-1] = c
		if to not in self.vertices:
			self.vertices.append(to)
		if fr not in self.vertices:
			self.vertices.append(fr)
	
	def print_adj_list(self):
		for k, v in self.adj_list.items():
			print(k, v)
	
	def print_adj_mat(self):
		for row in self.adj_mat:
			print(row)
	
def main():
	g = Graph()
	g.add_edge(1, 2, 1)
	g.add_edge(2, 3, 3)
	g.add_edge(3, 4, 4)
	g.add_edge(4, 1, 5)
	g.add_edge(1, 3, 1)
	print("Adjacency List:")
	g.print_adj_list()
	print("Adjacency Matrix:")
	g.print_adj_mat()

if __name__ == "__main__":
	main()
	


