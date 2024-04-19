from munkres import Munkres


if __name__ == '__main__':
    n = int(input())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    m = Munkres()
    indexes = m.compute(matrix)
    s = 0
    for i, j in indexes:
        s += matrix[i][j]
    print(s)