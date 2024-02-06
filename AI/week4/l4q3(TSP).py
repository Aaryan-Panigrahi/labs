from itertools import permutations


class GraphAdjacencyMatrix:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]
        

    def add_edge(self, u, v,weight):
        self.graph[u][v] = weight

    def print_graph(self):
        for row in self.graph:
            # print(" ".join(map(str, row)))
            # print(row)
            print(str(row))

    def solveTSP(self,start):
        vertices1=[]
        minpath=1000
        for i in range (self.V) :
            if i!=start:    
                vertices1.append(i)
        
        permu=permutations(vertices1)

        for i in permu:

            currentCost=0

            k=start
            for j in i:
                currentCost+=self.graph[k][j]
                k=j
            currentCost+=self.graph[k][start]

            minpath=min(minpath,currentCost)

        return minpath
    
    def performBFS(self, start):
        visited=[False]*self.V
        q=[]
        q.append(start)
        visited[start]=True

        while q:
            curr=q.pop()
            print(curr,end=' ')

            for neighbor in range(self.V):
                if self.graph[curr][neighbor]==1 and not visited[neighbor]:
                    q.append(neighbor)
                    visited[neighbor]=True

                elif self.graph[curr][neighbor]==1 and  visited[neighbor]:
                    print('cycle detected!')




# Example usage:
graph_adj_matrix = GraphAdjacencyMatrix(4)
graph_adj_matrix.add_edge(0, 1,2)
graph_adj_matrix.add_edge(0, 2,3)
graph_adj_matrix.add_edge(0, 3,1)

graph_adj_matrix.add_edge(1,0, 2)
graph_adj_matrix.add_edge(1,2,4)
graph_adj_matrix.add_edge(1,3,3)

graph_adj_matrix.add_edge(2,0, 3)
graph_adj_matrix.add_edge(2,1,4)
graph_adj_matrix.add_edge(2,3,3)


graph_adj_matrix.add_edge(3,0, 1)
graph_adj_matrix.add_edge(3,1,2)
graph_adj_matrix.add_edge(3,2,3)


print(f"cost for tsp is: {graph_adj_matrix.solveTSP(0)}")

graph_adj_matrix.print_graph()