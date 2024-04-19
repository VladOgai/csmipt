import networkx as nx


def main():
    v, e = map(int, input().split())
    gr = nx.Graph()
    gr.add_nodes_from(list(range(v)))
    for i in range(v):
        print(f'Соседние с {i} вершины: ')
        aaa = map(int, input().split())
        for j in aaa:
            gr.add_edge(i, j)

    try:
        flag = nx.find_cycle(gr)
    except nx.exception.NetworkXNoCycle:
        flag = False

    if flag:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()