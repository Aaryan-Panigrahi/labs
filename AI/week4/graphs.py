class Graph:
	def __init__(self, n):
		self.n = n
		self.vertices = {}
		self.edges = []
		self.adj_list = {}
		self.adj_mat = [[0 for i in range(n)] for j in range (n)]

	def define_vs(self, L):
		for i in range(self.n):
			self.vertices[L[i]] = i
			self.adj_list[i] = []

	def add_edge(self, v1, v2, w=1):

		#Adj Matrix - 
		self.adj_mat[self.vertices[v1]][self.vertices[v2]] = w

		#Adj List
		# self.adj_list[self.vertices[v1]].append([self.vertices[v2], w])
		self.adj_list[self.vertices[v1]].append([v2, w])

		self.edges.append([v1, v2, w])


	def add_unw_edge(self, v1, v2):

		#Adj Matrix - 
		self.adj_mat[self.vertices[v1]][self.vertices[v2]] = 1

		#Adj List
		if v1 not in self.adj_list:
			self.adj_list[v1] = []
		self.adj_list[v1].append(v2)

		self.edges.append([v1, v2, 1])


	def p_adj_list(self):
		for k, v in self.adj_list.items():
			print(k, v)


