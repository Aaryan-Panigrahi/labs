import graphs as gr

# def tsp_BFS(graph, start):
#     queue = []
#     visited = []
    
#     queue.append([start, start, 0]) # [current, path, cost]
#     visited.append(start)

#     min_cost = float('inf')

#     while queue:
#         current, path, cost = queue.pop(0)

#         if len(path) == len(graph.adj_list):
#             cost += graph.adj_list[current][start]
#             min_cost = min(min_cost, cost)
#             print("Path = ", path)
#             print("Cost = ", min_cost)
#             break

#         for neighbor, edge_cost in graph.adj_list[current]:
#             if neighbor not in visited:
#                 new_path = path + neighbor
#                 new_cost = cost + edge_cost

#                 min_cost = min(min_cost, new_cost)

#                 queue.append([neighbor, new_path, new_cost])
#                 visited.append(neighbor)

def swap(s, i, j):
    temp = s[i]
    s[i] = s[j]
    s[j] = temp
    return s.copy()  

def search_bfs(g, initial_seed):
    visited = set()
    queue = []
    all_permutations = []

    all_permutations.append(initial_seed)
    queue.append(initial_seed)
    visited.add(tuple(initial_seed))

    min_cost = get_path_loop_cost(g, initial_seed)
    min_path = initial_seed

    while queue:
        current_state = queue.pop(0)

        # Generate next states by swapping elements
        for i in range(len(current_state)):
            for j in range(i + 1, len(current_state)):
                next = swap(current_state, i, j)

                if tuple(next) not in visited: 

                    cost = get_path_loop_cost(g, next)
                    if cost < min_cost:
                        min_cost = cost
                        min_path = next

                    all_permutations.append(next)
                    visited.add(tuple(next))
                    queue.append(next)
    
    print("Path = ", min_path)
    print("Cost = ", min_cost)


def get_path_loop_cost(graph, path):
    cost = 0
    for i in range(len(path) - 1):
        l = graph.adj_list[path[i]]
        for j in l:
            if j[0] == path[i + 1]:
                cost += j[1]
                break
    l = graph.adj_list[path[-1]]
    for j in l:
        if j[0] == path[0]:
            cost += j[1]
            break
    return cost
    


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


    initial_case = ['A', 'B', 'C', 'D']
    search_bfs(g, initial_case)
