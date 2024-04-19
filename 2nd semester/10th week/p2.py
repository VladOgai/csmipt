from time import time_ns


def prim(gr: list[list[int]]) -> list[list[int]]:
    v = len(gr)
    sel = [False] * v
    n_edge = 0
    sel[0] = True
    res = [[0 for _ in range(v)] for _ in range(v)]

    while n_edge < v - 1:
        minimum = float('inf')
        x = 0
        y = 0
        for i in range(v):
            if sel[i]:
                for j in range(v):
                    if not sel[j] and gr[i][j]:
                        if minimum > gr[i][j]:
                            minimum = gr[i][j]
                            x = i
                            y = j
        sel[y] = True
        n_edge += 1
        res[x][y] = res[y][x] = gr[x][y]

    return res


def kruskal(gr: list[list[int]]) -> list[list[int]]:
    def find_parent(a):
        if parents[a] == a:
            return a
        return find_parent(parents[a])

    def apply_union(x, y):
        if rank[x] < rank[y]:
            parents[x] = y
            rank[y] += rank[x]
        else:
            parents[y] = x
            rank[x] += rank[y]

    v = len(gr)
    i, e = 0, 0
    edges = []
    for i in range(v):
        for j in range(i + 1, v):
            if gr[i][j]:
                edges.append([i, j, gr[i][j]])
    edges.sort(key=lambda x: x[2])
    parents = []
    rank = []
    res_gr = [[0 for _ in range(v)] for _ in range(v)]
    for node in range(v):
        parents.append(node)
        rank.append(1)
    while e < v - 1:
        u, v, w = edges[i]
        i += 1
        x = find_parent(u)
        y = find_parent(v)
        if x != y:
            e += 1
            res_gr[u][v] = res_gr[v][u] = w
            apply_union(x, y)
    return res_gr


if __name__ == '__main__':
    print('Первый тест:')
    test_1 = [[0, 5, 0, 0, 22],
              [5, 0, 0, 33, 2],
              [0, 0, 0, 3, 3],
              [0, 33, 3, 0, 0],
              [22, 2, 3, 0, 0]]
    pr1 = []
    kr1 = []
    for _ in range(20):
        start_time = time_ns()
        prim(test_1)
        end_time = time_ns()
        pr1.append(end_time - start_time)
        start_time = time_ns()
        kruskal(test_1)
        end_time = time_ns()
        kr1.append(end_time - start_time)
    krr1 = sum(kr1) / len(kr1)
    prr1 = sum(pr1) / len(pr1)
    print(f'    Среднее время выполнения алгоритма Прима: {prr1} нс\n    Среднее время выполнения алгоритма Краскала:'
          f' {krr1} нс')
    # сделать еще хз несколбко тестов
