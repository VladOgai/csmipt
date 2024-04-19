def main():
    v, e = map(int, input().split())
    graph = [[] for _ in range(v)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    D = [None] * v
    D[0] = 0
    Q = [0]
    Qstart = 0
    while Qstart < len(Q):
        u = Q[Qstart]
        Qstart += 1
        for v in graph[u]:
            if D[v] is None:
                D[v] = D[u] + 1
                Q.append(v)
    for el in D:
        print(el)


if __name__ == '__main__':
    main()