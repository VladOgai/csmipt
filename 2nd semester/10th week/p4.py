import networkx as nx


def main():
    inp = list(map(int, input().split()))
    n = inp[0]
    m = inp[1]
    main_nodes = inp[2:]
    roads = []
    for _ in range(m):
        roads.append(tuple(map(int, input().split())))
    g = nx.Graph()
    g.add_weighted_edges_from(roads)
    res = 0
    iiis = []
    for node in g.nodes:
        if node in main_nodes:
            iiis.append(node)
            continue
        res += min([nx.shortest_path_length(g, node, main_node, weight='weight') for main_node in main_nodes])
    print(res)


if __name__ == '__main__':
    main()