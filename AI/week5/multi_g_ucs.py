import ucs
import graphs as gr

if __name__ == '__main__':
    g = gr.Graph(10)
    g.define_vs(['S', 'A', 'B', 'C', 'D', 'E', 'F', 'G1', 'G2', 'G3'])
    g.add_edge('S', 'A', 5)
    g.add_edge('S', 'B', 9)
    g.add_edge('C', 'S', 6)
    g.add_edge('S', 'D', 6)
    g.add_edge('A', 'B', 3)
    g.add_edge('B', 'A', 2)
    g.add_edge('B', 'C', 1)
    g.add_edge('D', 'C', 2)
    g.add_edge('D', 'E', 2)
    g.add_edge('C', 'F', 7)
    g.add_edge('F', 'D', 2)
    g.add_edge('A', 'G1', 9)
    g.add_edge('C', 'G2', 5)
    g.add_edge('E', 'G3', 7)
    g.add_edge('F', 'G3', 8)

    for k, v in g.adj_list.items():
        print(k, v)
    

    ucs.ucs(g, 'S', ['G1', 'G2', 'G3'])

