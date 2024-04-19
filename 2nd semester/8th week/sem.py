from second_graph_HW import *


def fw(graph):  # граф - матрица
    n = len(graph)
    d = [[float('inf') for _ in range(n)] for _ in range(n)]
    nxt = [[-1 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j]:  # сюда мб матрицу весов
                d[i][j] = graph[i][j]
                nxt[i][j] = j

    for k in range(1, n):
        for i in range(n):
            for j in range(n):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = (d[i][k] + d[k][j])
                    nxt[i][j] = nxt[i][k]

    return d, nxt


def path(i, j, dist, nxt):
    if dist[i][j] == float('inf'):
        print('no path')
    c = i
    p = [c]
    while c != j:
        c = nxt[c - 1][j - 1] + 1
        p.append(c)
    return p


gr = read_graph_as_neigh_matrix_w()
'''
5
1 2 1
2 4 1
4 3 1
2 3 4
1 3 6
'''

'''
5
1 2 1
2 4 1
4 3 1
3 2 -3
1 3 6
'''

'''
12
1 2 -1
2 1 -1
1 3 -1
3 1 -1
1 4 -1
4 1 -1
2 3 -1
3 2 -1
2 4 -1
4 2 -1
3 4 -1
4 3 -1
'''

'''
6
1 2 -1
2 1 -1
1 3 -1
3 1 -1
2 3 -1
3 2 -1
'''
dist, p = fw(gr)
p = path(1, 3, dist, p)
print(p)
print()
for line in dist:
    print(*line)
