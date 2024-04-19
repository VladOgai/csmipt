import networkx as nx


def find_mst_with_edge(graph, edge):
    real_weight = edge[2]
    graph.remove_edge(edge[0], edge[1])
    graph.add_edge(edge[0], edge[1], weight=-float('inf'))
    mst = nx.minimum_spanning_tree(graph, weight='weight')
    mst.remove_edge(edge[0], edge[1])
    mst.add_edge(edge[0], edge[1], weight=real_weight)
    graph.add_edge(edge[0], edge[1], weight=real_weight)
    return int(mst.size(weight='weight'))


def main():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        edges.append(tuple(map(int, input().split())))
    graph = nx.Graph()
    graph.add_weighted_edges_from(edges)
    for i in range(m):
        wght = find_mst_with_edge(graph, edges[i])
        print(wght)


if __name__ == '__main__':
    main()