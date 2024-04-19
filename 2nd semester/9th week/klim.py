'''
Пусть загадан массив a1, ..., an, а также дано q ограничений к нему. Каждое ограничение имеет вид al + ... + ar <= k или
al + ... + ar >= k. Параметры l, r, k могут быть разными в разных ограничениях. Определите, совместны ли эти
ограничения, то есть существует ли хотя бы один загаданный массив с такими свойствами?
'''


def floyd_warshall(graph: list[list[int]]): # граф как матрица
    n = len(graph)
    d = [[float('inf') for _ in range(n)] for _ in range(n)]
    # nxt = [[-1 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j]:  # сюда мб матрицу весов
                d[i][j] = graph[i][j]
                # nxt[i][j] = j

    for k in range(1, n):
        for i in range(n):
            for j in range(n):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = (d[i][k] + d[k][j])
                    # nxt[i][j] = nxt[i][k]

    return d  # , nxt


if __name__ == '__main__':
    q = int(input())
    edges = []
    nodes = set()
    for _ in range(q):
        r, l, k, znak = input().split()
        r, l, k = map(int, (r, l, k))
        nodes.add(r)
        nodes.add(l - 1)
        match znak:
            case '<=':
                edges.append((r, l - 1, k))
            case '>=':
                edges.append((l - 1, r, -k))
            case _:
                print('Введен неправильный знак, ведите неравенство еще раз')
                break
    bub = max(nodes)
    gr = [[0 for _ in range(bub + 1)] for _ in range(bub + 1)]
    for edge in edges:
        gr[edge[0]][edge[1]] = edge[2]

    distances = floyd_warshall(gr)  # если есть отрицательные циклы (отрицательные числа на главной диагонали матрицы),
    # то система несовместна
    result = True
    for i in range(len(distances)):
        if distances[i][i] < 0:
            result = False
    print(result)