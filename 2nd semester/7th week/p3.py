# 1. Задайте граф и для него при помощи методов библиотеки  networkx посчитайте:
# 1) число вершин и число ребер
# 2) радиус и диаметр главной (наибольшей по размеру) связной компоненты (Giant Connected Component)
# 3) список длин кратчайших путей от каждой вершины до каждой.
import networkx as nx
from pyvis.network import Network


gr = nx.Graph()
gr.add_nodes_from([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
gr.add_edges_from([(0, 1), (0, 2), (0, 5), (1, 3), (1, 5), (1, 6), (2, 4), (2, 5), (3, 4), (5, 6), (6, 4), (7, 4),
                   (7, 6), (7, 2), (8, 3), (9, 0), (10, 1), (10, 3), (11, 12), (11, 14), (12, 13), (13, 14), (14, 12)])

# 1
print(f'Число вершин графа: {gr.number_of_nodes()}')
print(f'Число ребер графа: {gr.number_of_edges()}')
print()

# 2
grcc = sorted(nx.connected_components(gr), key=len, reverse=True)
gr0 = gr.subgraph(grcc[0])
print(f'Радиус главной связной компоненты: {nx.radius(gr0)}')
print(f'Диаметр главной связной компоненты: {nx.diameter(gr0)}')
print()

# 3
lengths = dict(nx.all_pairs_shortest_path_length(gr))
print('Длины кратчайших путей до:')
for node in lengths.keys():
    print(f'    Вершины {node} от:')
    for bnode in lengths[node].keys():
        print(f'        Вершины {bnode}: {lengths[node][bnode]}')

nt = Network('690px', '1475px')
nt.from_nx(gr)
nt.toggle_physics(True)
nt.show('nex.html', notebook=False)