def make_graph_arr(node_amount: int, pairs: list[tuple[int]]) -> list[list[int]]:
    gr_arr = [[] for _ in range(node_amount)]
    for a, b in pairs:
        gr_arr[a].append(b)
        gr_arr[a].sort()
        gr_arr[b].append(a)
        gr_arr[b].sort()
    return gr_arr


def dfs(graph: list[list[int]], node_amount: int, start=None, visited=None, prev=None, bebebe=True) -> tuple:
    if bebebe:
        start = 0
        visited = [False] * node_amount
        prev = [None] * node_amount
    for u in graph[start]:
        if not visited[u]:
            prev[u] = start
            visited[u] = True
            dfs(graph, node_amount, u, visited, prev, bebebe=False)
    visited[start] = True
    if bebebe:
        return visited, prev


if __name__ == '__main__':
    n = int(input())
    prs = []
    inp = input()
    while inp != '0':
        prs.append(tuple(map(int, inp.split())))
        inp = input()
    gr = make_graph_arr(n, prs)
    vis, prev = dfs(gr, n)
    # if False in vis:
    #     print('Граф несвязный')
    # else:
    #     print('Граф связный урааа')
    flag = False not in vis
    print(flag)
