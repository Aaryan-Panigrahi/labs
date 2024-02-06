p_BFS(graph, start):
    queue = []
    visited = []
    
    queue.append([start, start, 0]) # [current, path, cost]
    visited.append(start)

    min_cost = float('i