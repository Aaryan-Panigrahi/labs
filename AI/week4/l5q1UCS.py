class GraphAdjacencyList:
    def __init__(self,V):
        self.V=V
        self.graph = {}

    def add_edge(self, u, v,weight):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v,weight))

    def print_graph(self):
        for node in self.graph:
            print(node, "->", " -> ".join(str(adj_node) for adj_node in self.graph[node]))

    def UCS(self, start, end):
        priq = []
        visited = [0 for _ in range(self.V)]
        print(visited)
        priq.append([0,start])
        path_followed = []
        while(priq):
            priq=sorted(priq)
            print('priorit Q: ',priq)

            [current_cost,current_node] = priq.pop(0)
            print ('curr node', current_node)
            path_followed.append(current_node)

            if current_node == end:
                print('path followed: ')
                print(path_followed)
                print('total cost: ',current_cost)

                break


            for (neighbour_node, neighbour_cost) in self.graph[current_node]:
                print('neighbour node: ',neighbour_node, 'neighbour cost: ',neighbour_cost)
                priq.append([neighbour_cost+current_cost,neighbour_node])
                # if 




# Example usage:
graph_adj_list = GraphAdjacencyList(7)
graph_adj_list.add_edge(0,1,2)
graph_adj_list.add_edge(0,3,5)
graph_adj_list.add_edge(3,1,5)
graph_adj_list.add_edge(1,6,1)
graph_adj_list.add_edge(3,6,6)
graph_adj_list.add_edge(3,4,2)
graph_adj_list.add_edge(2,1,4)
graph_adj_list.add_edge(6,4,7)
graph_adj_list.add_edge(4,2,4)
graph_adj_list.add_edge(4,5,3)
graph_adj_list.add_edge(5,2,6)
graph_adj_list.add_edge(5,6,3)
# graph_adj_list.add_edge(0,1,2)
# graph_adj_list.add_edge(0, 2,5)
# graph_adj_list.add_edge(0, 3,2)
# graph_adj_list.add_edge(2, 4,7)
# graph_adj_list.add_edge(2, 3,3)
# graph_adj_list.add_edge(1, 3,1)
# graph_adj_list.add_edge(3, 4,1)
# graph_adj_list.add_edge(3, 3)

graph_adj_list.print_graph()
graph_adj_list.UCS(0,6)