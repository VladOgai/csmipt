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
            if dist[v] > dist[u] * weights[u][v]:
                dist[v] = dist[u] * weights[u][v]

    return dist


def dijkstra3(n: int, start: int, weights, graph_array):
    new_weights = []
    for lst in weights:
        new_weights.append(list(map(len, lst)))
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


def dijkstra4(n: int, start: int, weights, graph_array):
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
            if dist[v] < min(dist[u], weights[u][v]):
                dist[v] = min(dist[u], weights[u][v])

    return dist


def main():
    gr = [[1, 3, 4], [0, 2], [1, 4], [0, 4], [0, 2]]
    w = [[0, 1, 0, 2, 4],
         [1, 0, 3, 0, 0],
         [0, 3, 0, 0, 1],
         [2, 0, 0, 0, 5],
         [4, 0, 1, 5, 0]]
    print(dijkstra1(5, 0, w, gr))  # [0, 1, 3, 2, 3]


if __name__ == '__main__':
    main()