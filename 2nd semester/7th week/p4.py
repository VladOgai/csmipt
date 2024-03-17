# 2. Задайте граф и для него при помощи методов библиотеки  networkx посчитайте:
# 1) плотность графа и число связных компонент
# 2) словарь предшествующих вершин при поиске в глубину из заданной вершины
# 3) сгенерируйте полносвязный граф из 5 вершин и выведите для него все простые пути из вершины 2 в вершину 4.
import networkx as nx
from pyvis.network import Network


gr = nx.Graph()
gr.add_nodes_from([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
gr.add_edges_from([(0, 1), (0, 2), (0, 5), (1, 3), (1, 5), (1, 6), (2, 4), (2, 5), (3, 4), (5, 6), (6, 4), (7, 4),
                   (7, 6), (7, 2), (8, 3), (9, 0), (10, 1), (10, 3), (11, 12), (11, 14), (12, 13), (13, 14), (14, 12)])

# 1
print(f'Плотность графа: {nx.density(gr)}')
print(f'Число связных компонент: {len(sorted(nx.connected_components(gr)))}')
print()

# 2
start = 0
print(f'Словарь предшествующих вершин при обходе с вершины {start}:')
print(nx.dfs_predecessors(gr, start))
print()

# 3
complete_gr = nx.complete_graph(5)
print('Все простые пути из вершины 2 в вершину 4 для полносвязного графа:')
for path in nx.all_simple_paths(complete_gr, source=2, target=4):
    print(f'    {path}')