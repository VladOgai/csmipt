def count_elem_multiplications(matrix: dict, expression: list) -> str or int:
    if len(expression) == 1:
        return 0
    if len(expression) == 2:
        m1 = matrix[expression[0]][0]
        n1 = matrix[expression[0]][1]
        m2 = matrix[expression[1]][0]
        n2 = matrix[expression[1]][1]
        if n1 != m2:
            return 'error'
        return m1 * n1 * n2
    matrix_sizes = [matrix[x] for x in expression]
    for i in range(len(matrix_sizes) - 1):
        if matrix_sizes[i][1] != matrix_sizes[i + 1][0]:
            return 'error'
    list_of_columns = [x[1] for x in matrix_sizes[:-1]]
    mincol = min(list_of_columns)
    res = 0
    for matr in matrix_sizes:
        if all((matr[0] != mincol, matr[1] != mincol)):
            res += matr[0] * matr[1]
    res += matrix_sizes[0][0] * matrix_sizes[-1][1]
    res *= mincol
    return res


N = int(input())
matrix = dict()
for _ in range(N):
    name, m, n = input().split()
    matrix[name] = (int(m), int(n))
while True:
    osch = input()
    if osch == '0':
        break
    exp = list(osch)
    print(count_elem_multiplications(matrix, exp))
