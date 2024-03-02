# Попробовал реализовать классом, чтоб все функции в одном месте находились
from collections import defaultdict


class DirectedGraph:
    def __init__(self):
        self.graph_dict = defaultdict(list)

    def create_from_pairs(self, edges):
        for u, v in edges:
            self.graph_dict[u].append(v)
            if v not in self.graph_dict:
                self.graph_dict[v] = []

    def find_cycles(self, start):
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

        return cycles

    def find_full_cycle(self):
        nodes = list(self.graph_dict.keys())
        start = nodes[0]
        cycles = self.find_cycles(start)
        n = len(nodes)
        res = None
        for cycle in cycles:
            if len(cycle) == n + 1:
                res = cycle
                break
        return res


if __name__ == '__main__':
    words = list(input().split())  # ant ostrich deer turkey kangaroo tiger rabbit rat toad yak hyena
    prs = []
    for word1 in words:
        last_letter = word1[-1]
        for word2 in words:
            first_letter = word2[0]
            if word1 != word2 and first_letter == last_letter:
                prs.append((word1, word2))
    graph = DirectedGraph()
    graph.create_from_pairs(prs)
    full_cycle = graph.find_full_cycle()
    print(bool(full_cycle))
    print()
    print(' -> '.join(full_cycle))

