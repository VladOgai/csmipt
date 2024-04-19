def find_cycles(graph: list[list[int]]) -> tuple[list[list[int]], bool]:
    color = [0] * len(graph)
    cycles = []

    def dfs(u, color, par, p=0):
        if color[u] == 2:
            return
        if color[u] == 1:
            v = []
            cur = p
            v.append(cur)
            while cur != u:
                cur = par[cur]
                v.append(cur)
            cycles.append(v)
            return
        par[u] = p
        color[u] = 1
        for v in graph[u]:
            if v == par[u]:
                continue
            dfs(v, color, par, u)
        color[u] = 2

    par = [0] * len(graph)
    dfs(1, color, par)

    flag = all(color[1:])

    return cycles, flag


def is_cactus(cycles: list[list[int]]) -> bool:
    res_set = set()
    res = 0
    for cycle in cycles:
        cycle_as_edges = set([tuple(sorted((cycle[i], cycle[i + 1]))) for i in range(len(cycle) - 1)])
        cycle_as_edges.add(tuple(sorted((cycle[0], cycle[-1]))))
        res_set.update(cycle_as_edges)
        res += len(cycle_as_edges)
    if len(res_set) < res:
        return False
    return True


if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        path = list(map(int, input().split()))
        k = path[0]
        path = path[1:]
        for i in range(1, k):
            graph[path[i]].append(path[i - 1])
            graph[path[i - 1]].append(path[i])
    # print(graph)
    gr_cycles, flag = find_cycles(graph)
    # print(gr_cycles)
    if flag and is_cactus(gr_cycles):
        res = 1
        for cycle in gr_cycles:
            res *= len(cycle) + 1
        print(res)
    else:
        print(0)