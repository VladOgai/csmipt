import networkx as nx
import matplotlib.pyplot as plt


def main():
    # 6 5 mendeleevskaya serpukhovskaya
    # mendeleevskaya tsvetnoy_bulvar 4
    # tsvetnoy_bulvar chekhovskaya 3
    # chekhovskaya borovitskaya 4
    # borovitskaya polyanka 3
    # polyanka serpukhovskaya 3
    v, e, start, end = input().split()
    v, e = map(int, (v, e))
    edges = []
    for _ in range(e):
        name_1, name_2, time = input().split()
        edges.append((name_1, name_2, int(time)))
    gr = nx.Graph()
    gr.add_weighted_edges_from(edges)
    shp = nx.shortest_path(gr, start, end, weight='weight')
    shpl = nx.shortest_path_length(gr, start, end, weight='weight')
    print(f'Кратчайший путь от {start} к {end}:')
    print(' -> '.join(shp))
    print(f'Длина: {shpl}')

    pos = nx.spring_layout(gr, seed=7)
    nx.draw_networkx_nodes(gr, pos, node_size=700)
    nx.draw_networkx_edges(gr, pos)
    nx.draw_networkx_labels(gr, pos, font_size=20, font_family='Comic Sans MS')
    edge_labels = nx.get_edge_attributes(gr, "weight")
    nx.draw_networkx_edge_labels(gr, pos, edge_labels)

    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()