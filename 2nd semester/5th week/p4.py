from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph_dict = defaultdict(list)

    def create_from_pairs(self, edges):
        for u, v in edges:
            self.graph_dict[u].append(v)
            self.graph_dict[v].append(u)

    def find_cycles(self, start=None):
        if start is None:
            start = list(self.graph_dict.keys())
            start = max(start, key=lambda x: len(self.graph_dict[x]))

        cycles = []
        visited = set()

        def dfs(node, path):
            visited.add(node)
            path.append(node)
            for neighbour in self.graph_dict.get(node, []):
                if neighbour == start:
                    cycles.append(path[path.index(start):] + [start])
                elif neighbour not in visited:
                    dfs(neighbour, path)
            path.pop()
            visited.remove(node)

        dfs(start, [])

        return any(map(lambda x: len(x) > 3, cycles))


if __name__ == '__main__':
    n = int(input())
    prs = []
    inp = input()
    while inp != '0':
        prs.append(tuple(map(int, inp.split())))
        inp = input()
    gr = Graph()
    gr.create_from_pairs(prs)
    print(gr.find_cycles())