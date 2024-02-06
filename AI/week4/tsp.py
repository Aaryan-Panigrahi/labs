import graphs as gr

def tsp_BFS(graph, start):
    queue = []
    visited = []
    
    queue.append([start, start, 0]) # [current, path, cost]
    visited.append(start)

    min_cost = float('inf')

    while queue:
        current, path, cost = queue.pop(0)

        if len(path) == len(graph.adj_list):
            cost += graph.adj_list[current][start]
            min_cost = min(min_cost, cost)
            continue

        for neighbor, edge_cost in graph.adj_list[current]:
            if neighbor not in visited:
                new_path = path + neighbor
                new_cost = cost + edge_cost

                min_cost = min(min_cost, new_cost)

                queue.append([neighbor, new_path, new_cost])
                visited.append(neighbor)


if __name__ == '__main__':
    g = gr.Graph(4)
    g.define_vs(['A', 'B', 'C', 'D'])
    g.add_edge('A', 'B', 2)
    g.add_edge('A', 'C', 3)
    g.add_edge('A', 'D', 1)
    g.add_edge('B', 'A', 2)
    g.add_edge('B', 'C', 4)
    g.add_edge('B', 'D', 2)
    g.add_edge('C', 'A', 3)
    g.add_edge('C', 'B', 4)
    g.add_edge('C', 'D', 3)
    g.add_edge('D', 'A', 1)
    g.add_edge('D', 'B', 2)
    g.add_edge('D', 'C', 3)

    for k, v in g.adj_list.items():
        print(k, v)
    
    print(g.adj_list['A'])


    print(tsp_BFS(g, 'A')) 