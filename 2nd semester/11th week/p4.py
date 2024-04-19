import networkx as nx
from collections import defaultdict


if __name__ == '__main__':
    n = int(input())
    name = input()
    g = nx.Graph()
    g.add_node('start')
    g.add_node('end')
    for i in range(1, n + 1):
        g.add_edge('start', i, capacity=1)
        letters = list(input())
        for l in letters:
            g.add_edge(i, l)
            if l in name:
                c = name.count(l)
                g.add_edge(l, 'end', capacity=c)
    v, r = nx.maximum_flow(g, 'start', 'end')
    print(v)
    print(r)
    if v != len(name):
        print('NO')
    else:
        print('YES')
        cc = defaultdict(list)
        res = [None for _ in range(len(name))]
        cubes = set()
        for l in name:
            aoao = list(r[l].keys())
            aoao.remove('end')
            cubes.update(set(aoao))
            curr = 0
            for j in range(name.count(l)):
                ind = name.index(l, curr)
                curr = ind + 1
                if len(aoao) == 1:
                    res[ind] = aoao[0]
                    cubes.remove(aoao[0])
                else:
                    res[ind] = aoao
        # дальше я не придумал как кубики выбрать но там все очевидно
        print(res)