def make_graph_dict(pairs: list[tuple[str]]) -> dict[str: str]:
    graph = dict()
    for a, b in pairs:
        graph[a] = b
    return graph


if __name__ == '__main__':
    prs = []
    inp = input()
    while inp != '0':
        prs.append(tuple(inp.split()))
        inp = input()
    gr_dict = make_graph_dict(prs)
    departure = set(gr_dict.keys())
    arrival = set(gr_dict.values())
    i = (departure - arrival).pop()
    res = []
    while i in gr_dict.keys():
        res.append(i)
        i = gr_dict[i]
    res.append(i)
    print(res)