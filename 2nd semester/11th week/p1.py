def is_bipartite(graph_array: list[list[int]]) -> bool:
    colors = [0] * n
    res = True

    def dfs_bebebe(start: int, res) -> bool:
        for v in graph_array[start]:
            if colors[v] == 0:
                colors[v] = 3 - colors[start]
                res = res and dfs_bebebe(v, res)
            elif colors[v] == colors[start]:
                res = res and False
        return res

    for i in range(len(graph_array)):
        if colors[i] == 0:
            colors[i] = 1
            res = res and dfs_bebebe(i, res)

    return res


if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)
    r = is_bipartite(graph)
    if r:
        print('YES')
    else:
        print('NO')
