import networkx as nx


def main():
    n, m, s, f = map(int, input().split())  # 2 1 0 1
    edges = []

    for _ in range(m):  # 1 0 5
        edges.append(tuple(map(int, input().split())))

    gr = nx.Graph()
    gr.add_nodes_from(list(range(n)))
    gr.add_weighted_edges_from(edges)
    print(nx.shortest_path_length(gr, s, f) + 1)


if __name__ == '__main__':
    main()
