from collections import defaultdict


def is_cyclic(graph_array: dict[str: list[str]]) -> bool:
    used = dict.fromkeys(graph_array.keys(), 0)

    res = False

    def dfs(v, x):
        used[v] = 1
        for u in graph_array[v]:
            if u in graph_array.keys():
                if used[u] == 0:
                    x = x or dfs(u, x)
                elif used[u] == 1:
                    x = x or True
                x = x or False
            else:
                x = x or False
                continue
        used[v] = 2
        return x

    for i in graph_array.keys():
        if not used[i]:
            x = res
            res = res or dfs(i, x)

    return res


if __name__ == '__main__':
    n = int(input())
    graph = defaultdict(list)
    for _ in range(n):
        a, b, c = input().split()
        match b:
            case '<':
                graph[c].append(a)
            case '>':
                graph[a].append(c)
    if is_cyclic(graph):
        print('impossible')
    else:
        print('possible')
