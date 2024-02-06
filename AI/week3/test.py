import graphs as gr

def find_cycles(g):
    visited = [False] * g.n
    cycle_rn = []

    for vno in range(g.n):
        if not visited[vno]:
            search(g, vno, visited, cycle_rn)

def search(g, vno, visited, cycle_rn):
    visited[vno] = True
    cycle_rn.append(vno)

    for adj in g.adj_list[vno]:
        if not visited[adj]:
            search(g, adj, visited, cycle_rn)
        elif adj in cycle_rn and cycle_rn.index(adj) == len(cycle_rn) - 1:
            print('Found a cycle')
            print(cycle_rn[cycle_rn.index(adj):])
    cycle_rn.pop()
    visited[vno] = False

if __name__ == "__main__":
    g = gr.Graph(4)
    g.define_vs([0, 1, 2, 3])
    g.add_unw_edge(0, 1)
    g.add_unw_edge(0, 2)
    g.add_unw_edge(1, 2)
    g.add_unw_edge(2, 0)
    g.add_unw_edge(2, 3)
    g.add_unw_edge(3, 3)

    find_cycles(g)
