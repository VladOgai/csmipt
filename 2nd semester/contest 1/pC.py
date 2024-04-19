if __name__ == '__main__':
    n, m = map(int, input().split())
    if m != n * (n - 1) // 2:
        print('no')
    else:
        graph_matrix = [[0 for _ in range(n)] for _ in range(n)]
        for _ in range(m):
            a, b = map(int, input().split())
            a -= 1
            b -= 1
            graph_matrix[a][a] = 1
            graph_matrix[b][b] = 1
            graph_matrix[a][b] += 1
            graph_matrix[b][a] += 1
        res = all([all([y == 1 for y in x]) for x in graph_matrix])
        if res:
            print('yes')
        else:
            print('no')