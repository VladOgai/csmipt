def make_orient_graph_arr(node_amount: int, pairs: list[tuple[int]]) -> list[list[int]]:
    gr_arr = [[] for _ in range(node_amount)]
    for a, b in pairs:
        gr_arr[a].append(b)
        gr_arr[a].sort()
    return gr_arr


def check_if_reachable(graph: list[list[int]], node_amount: int, start: int,
                       end: int, visited=None, bebebe=True, flag=False) -> bool:
    if bebebe:
        visited = [False] * node_amount
        if start == end:
            return True
        flag = False
    for u in graph[start]:
        if not visited[u]:
            visited[u] = True
            if u == end:
                return True
            flag = check_if_reachable(graph, node_amount, u, end, visited, bebebe=False)
    visited[start] = True
    return flag


if __name__ == '__main__':
    n = int(input())
    prs = []
    inp = input()
    while inp != '0':
        prs.append(tuple(map(int, inp.split())))
        inp = input()
    first, last = map(int, input().split())
    gr = make_orient_graph_arr(n, prs)
    reach = check_if_reachable(gr, n, first, last)
    print(reach)
