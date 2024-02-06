import graphs as gr

def topo(g):
    n = g.n
    #Caluculate indegrees for all
    indegs = [0 for i in range(n)]
    for i in range(n):
        for adj in g.adj_list.get(i):
            indegs[adj] += 1

    # add vertices of indegtree 0 to queue
    queue = []
    for i in range(n):
        if indegs[i] == 0:
            queue.append(i)

    print("Indegs = ", indegs)
    print("Initial Queue - ", queue)
    topo = []
    while(len(queue) > 0):
        e = queue.pop(0)
        topo.append(e)
        for adj in g.adj_list.get(e):
            indegs[adj] -=1
            if indegs[adj] == 0:
                queue.append(adj)
    print(topo)

if __name__ == "__main__":
    g = gr.Graph(6)

    g.define_vs([0, 1, 2, 3, 4, 5])
    g.add_unw_edge(5, 2)
    g.add_unw_edge(5, 0)
    g.add_unw_edge(4, 0)
    g.add_unw_edge(4, 1)
    g.add_unw_edge(3, 1)
    g.add_unw_edge(2, 3)
    
    topo(g)


