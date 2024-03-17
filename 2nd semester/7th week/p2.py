# 2) Стоимостью пути можно считать не сумму всех весов входящих в него рёбер, а некие другие функции. Покажите,
# как (и можно ли вообще) модифицировать алгоритм Дейкстры для следующих функций стоимости пути:
# максимальный среди весов используемых рёбер;
# произведение весов рёбер (все веса имеют вес хотя бы 1);
# конкатенация строк, написанных на рёбрах;
# минимальный среди весов используемых рёбер, только теперь стоимость пути нужно максимизировать;
# считаем, что все вершины раскрашены в какие-то цвета, а рёбра имеют неотрицательные длины; нужно в первую очередь
# минимизировать количество смен цвета, во вторую — суммарную рёбер.
def dijkstra(n: int, start: int, weights, graph_array):
    dist = [float('inf') for _ in range(n)]
    dist[start] = 0
    used = []
    queue = [i for i in range(n)]

    def mindist(q, d):
        return min(q, key=lambda x: d[x])

    while queue:
        u = mindist(queue, dist)
        queue.remove(u)
        used.append(u)
        for v in graph_array[u]:
            if dist[v] > dist[u] + weights[u][v]:
                dist[v] = dist[u] + weights[u][v]

    return dist


def dijkstra1(n: int, start: int, weights, graph_array):
    dist = [float('inf') for _ in range(n)]
    dist[start] = 0
    used = []
    queue = list(range(n))

    def mindist(q, d):
        return min(q, key=lambda x: d[x])

    while queue:
        u = mindist(queue, dist)
        queue.remove(u)
        used.append(u)
        for v in graph_array[u]:
            if dist[v] > max(dist[u], weights[u][v]):
                dist[v] = max(dist[u], weights[u][v])

    return dist


def dijkstra2(n: int, start: int, weights, graph_array):
    dist = [float('inf') for _ in range(n)]
    dist[start] = 1
    used = []
    queue = [i for i in range(n)]

    def mindist(q, d):
        return min(q, key=lambda x: d[x])

    while queue:
        u = mindist(queue, dist)
        queue.remove(u)
        used.append(u)
        for v in graph_array[u]:
            if dist[v] > dist[u] * weights[u][v]:
                dist[v] = dist[u] * weights[u][v]

    dist[start] = 0

    return dist


def dijkstra3(n: int, start: int, weights, graph_array):
    new_weights = []
    for lst in weights:
        new_weights.append(list(map(len, lst)))
    dist = ['g' * 10000 for _ in range(n)]
    dist[start] = ''
    used = []
    queue = [i for i in range(n)]

    def mindist(q, d):
        return min(q, key=lambda x: len(d[x]))

    while queue:
        u = mindist(queue, dist)
        queue.remove(u)
        used.append(u)
        for v in graph_array[u]:
            if len(dist[v]) > len(dist[u]) + len(weights[u][v]):
                dist[v] = dist[u] + weights[u][v]

    return dist


def dijkstra4(n: int, start: int, weights, graph_array):
    dist = [0 for _ in range(n)]
    dist[start] = float('inf')
    used = []
    queue = [i for i in range(n)]

    def maxdist(q, d):
        return max(q, key=lambda x: d[x])

    while queue:
        u = maxdist(queue, dist)
        queue.remove(u)
        used.append(u)
        for v in graph_array[u]:
            if dist[v] < min(dist[u], weights[u][v]):
                dist[v] = min(dist[u], weights[u][v])

    dist[0] = 0

    return dist


def dijkstra5(n: int, start: int, weights, colors, graph_array):
    dist = [[float('inf'), float('inf')] for _ in range(n)]
    dist[start] = [0, 0]
    used = []
    queue = [i for i in range(n)]
    ww = []
    for j in weights:
        for i in j:
            if i:
                ww.append(i)
    pluscol = max(ww) + 1

    def mindist(q, d):
        return min(q, key=lambda x: d[x][0])

    while queue:
        u = mindist(queue, dist)
        queue.remove(u)
        used.append(u)
        for v in graph_array[u]:
            if colors[v] == colors[u]:
                if dist[v][0] >= dist[u][0] + weights[u][v] and dist[v][1] >= dist[u][1]:
                    dist[v][0] = dist[u][0] + weights[u][v]
                    dist[v][1] = dist[u][1]
            elif dist[v][1] >= dist[u][1] + pluscol:
                dist[v][1] = dist[u][1] + pluscol
                if sum(dist[v]) > sum(dist[u]) + weights[u][v]:
                    dist[v][0] = dist[u][0] + weights[u][v]

    for v in dist:
        v[1] //= pluscol

    return dist


def main():
    gr = [[1, 3, 4], [0, 2], [1, 4], [0, 4], [0, 2, 3]]
    w = [[0, 1, 0, 4, 10],
         [1, 0, 2, 0, 0],
         [0, 2, 0, 0, 3],
         [4, 0, 0, 0, 5],
         [10, 0, 3, 5, 0]]

    w3 = [['', 'x', '', 'boat', 'abrakadabra'],
         ['x', '', 'hi', '', ''],
         ['', 'hi', '', '', 'row'],
         ['boat', '', '', '', 'booom'],
         ['abrakadabra', '', 'row', 'booom', '']]

    cc = ['black', 'red', 'black', 'red', 'black']
    print(dijkstra1(5, 0, w, gr))  # [0, 1, 2, 4, 3]
    print()
    print(dijkstra2(5, 0, w, gr))  # [0, 1, 2, 4, 6]
    print()
    print(dijkstra3(5, 0, w3, gr))  # ['', 'x', 'xhi', 'boat', 'xhirow']
    print()
    print(dijkstra4(5, 0, w, gr))  # [0, 2, 3, 5, 10]
    print()
    print(dijkstra5(5, 0, w, cc, gr))  # [[0, 0], [1, 1], [3, 2], [4, 1], [10, 0]] второе число - количество смен цвета,
    # сперва минимизировано по нему


if __name__ == '__main__':
    main()