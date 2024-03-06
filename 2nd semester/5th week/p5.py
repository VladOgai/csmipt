import numpy as np
from collections import defaultdict


class Graph:
    def __init__(self, vert_num):
        self.vert_num = vert_num
        self.graph_matrix = np.zeros((self.vert_num, self.vert_num), dtype=int)
        self.graph_dict = defaultdict(list)

    def make_from_edges(self, edges):
        for a, b, c in edges:
            self.graph_dict[a].append(b)
            if b not in self.graph_dict:
                self.graph_dict[b] = []
            self.graph_matrix[a][b] = c

    def find_least_path(self, start, end):
        dp = [[] for _ in range(self.vert_num)]
        dp[start] = [0]

        def dfs_dp(startt):
            for u in self.graph_dict[startt]:
                dp[u].append(min(dp[startt]) + self.graph_matrix[startt][u])
                dfs_dp(u)

        dfs_dp(start)
        return min(dp[end])


if __name__ == '__main__':
    eedges = []
    inp = input()
    while inp.count(' ') == 2:
        eedges.append(tuple(map(int, inp.split())))
        inp = input()
    st, en = map(int, inp.split())
    xs, ys, _ = zip(*eedges)
    n = max(xs + ys) + 1
    gr = Graph(n)
    gr.make_from_edges(eedges)
    print(gr.find_least_path(st, en))