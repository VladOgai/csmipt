def bellmanford(graph: list[list[int]], start_node:int) -> tuple:
    vnum = len(graph)
    aaa = [[float('inf') for _ in range(vnum)] for _ in range(vnum)]
    ppp = [[None for _ in range(vnum)] for _ in range(vnum)]
    aaa[0][start_node] = 0
    edges = []
    for i in range(vnum):
        for j in range(vnum):
            if graph[i][j]:
                edges.append([i, j, graph[i][j]])
    for i in range(vnum - 1):
        for edge in edges:
            u, v, w = edge
            if aaa[i][v] > aaa[i - 1][u] + w:
                aaa[i][v] = aaa[i - 1][u] + w
                ppp[i][v] = u
    return aaa, ppp


def find_path_from_bellman_ford(ppp: list[list[any]], end_node: int,  num_of_edges: int) -> list[int]:
    p = []
    while num_of_edges > 0:
        p[num_of_edges] = end_node
        end_node = ppp[num_of_edges][end_node]
        num_of_edges -= 1
    return p
