import graphs as gr
import ucs

if __name__ == '__main__':
    g = gr.Graph(7)
    cities = ['Dunwich', 'Blaxhall', 'Feering', 'Tiptree', 'Harwich', 'Meldone', 'Clatcon']
    g.define_vs(cities)
    g.add_edge('Dunwich', 'Blaxhall', 17)
    g.add_edge('Blaxhall', 'Dunwich', 15)
    g.add_edge('Feering', 'Blaxhall', 46)
    g.add_edge('Feering', 'Meldone', 11)
    g.add_edge('Tiptree', 'Feering', 3)
    g.add_edge('Tiptree', 'Clatcon', 29)
    g.add_edge('Harwich', 'Tiptree', 31)
    g.add_edge('Harwich', 'Blaxhall', 40)
    g.add_edge('Harwich', 'Dunwich', 53)
    g.add_edge('Meldone', 'Tiptree', 8)
    g.add_edge('Clatcon', 'Meldone', 40)

    for k, v in g.adj_list.items():
        print(k, v)

    ucs.ucs(g, 'Meldone', ['Dunwich', ])