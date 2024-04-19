def main():
    n = int(input())
    m = int(input())
    graph = [[0 for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    D = [None] * n
    count = 0
    for i in range(n):
        if D[i] is None:
            count += 1
            D[i] = 0
            Q = [i]
            Qstart = 0
            while Qstart < len(Q):
                u = Q[Qstart]
                Qstart += 1
                for v in graph[u]:
                    if D[v] is None:
                        D[v] = D[u] + 1
                        Q.append(v)
    print(count)


if __name__ == '__main__':
    main()