import graphs as gr

class PriorityQueue:
    def __init__(self):
        self.queue = []
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def push(self, item, path, cost):
        self.queue.append((item, path, cost))
    
    def pop(self):
        min_cost = float('inf')
        min_item = None
        for i in range(len(self.queue)):
            if self.queue[i][2] < min_cost:
                min_cost = self.queue[i][2]
                min_item = i
        return self.queue.pop(min_item)
    
    def print_queue(self):
        for item, cost in self.queue:
            print(item, cost)
        print()

def ucs(graph, start, goals):
    q = PriorityQueue()
    q.push(start, [start,], 0)
    visited = []

    while not q.is_empty():
        curr, path, cost = q.pop()
        visited.append(curr)

        if curr in goals:
            print('Path: ', path)
            print('Cost: ', cost)
            return path, cost
        
        for neighbor, edge_cost in graph.adj_list[curr]:
            np = path.copy()
            np.append(neighbor)
            # print("Considerign neighbor: ", neighbor)
            # print('Path: ', np)

            if neighbor not in visited:
                q.push(neighbor, np, cost + edge_cost)
            else:
                path_cost = cost + edge_cost
                for i in range(len(q.queue)):
                    if q.queue[i][0] == neighbor and q.queue[i][2] > path_cost:
                        q.queue[i] = (neighbor, np, path_cost)



if __name__ == '__main__':
    g = gr.Graph(7)
    g.define_vs([0,1,2,3,4,5,6])
    g.add_edge(0,1,2)
    g.add_edge(0,3,5)
    g.add_edge(3,1,5)
    g.add_edge(1,6,1)
    g.add_edge(3,6,6)
    g.add_edge(3,4,2)
    g.add_edge(2,1,4)
    g.add_edge(6,4,7)
    g.add_edge(4,2,4)
    g.add_edge(4,5,3)
    g.add_edge(5,2,6)
    g.add_edge(5,6,3)

    ucs(g, 0, [6])