import graphs as gr

def find_cycles_bfs(g):
    f = 0
    for vno in range(g.n):
        if(search_bfs(g, vno, vno)):
            print('Found a cycle at ', vno)
            f+=1
    if f==0: 
        print("No cycles were found")
    

def search_bfs(g, start, target):
    visited = []
    queue = []
    queue.append(start)
    visited.append(start)

    while queue:
        e = queue.pop(0)
        visited.append(e)
        
        for adj in g.adj_list.get(e):
            queue.append(adj)
            if adj == target:
                return True

    return False    
      

if __name__ == "__main__":
    g = gr.Graph(4)
    g.define_vs([0, 1, 2, 3])
    g.add_unw_edge(0, 1)
    g.add_unw_edge(0, 2)
    g.add_unw_edge(1, 2)
    g.add_unw_edge(2, 0)
    g.add_unw_edge(2, 3)
    g.add_unw_edge(3, 3)
    
    print("\n1st Graph - ")
    find_cycles_bfs(g)

    g2 = gr.Graph(3)
    g2.define_vs(range(3))
    g2.add_unw_edge(0, 1)
    g2.add_unw_edge(0, 2)
    g2.add_unw_edge(1, 2)
    print("\n2nd Graph - ")
    find_cycles_bfs(g2)