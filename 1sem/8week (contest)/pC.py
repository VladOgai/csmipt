import math


def dobavit_nol(s: str) -> str:
    if s[-2:] == '.0':
        s += '0'
    return s


def road_len(points: list, k: int) -> float:
    res = 0.0
    for i in range(k - 1):
        res += math.sqrt((points[i][0] - points[i + 1][0]) ** 2 +
                         (points[i][1] - points[i + 1][1]) ** 2)
    return res


def find_coords_by_length(points: list, length: float) -> tuple:
    i = 0
    while True:
        part_length = math.sqrt((points[i][0] - points[i + 1][0]) ** 2 +
                                (points[i][1] - points[i + 1][1]) ** 2)
        if part_length >= length:
            break
        length -= part_length
        i += 1
    y0, y1, x0, x1 = points[i][1], points[i + 1][1], points[i][0], points[i + 1][0]
    a = math.sqrt(length ** 2 / (1 + ((y1 - y0) / (x1 - x0)) ** 2))
    if x0 > x0 + a > x1 or x0 < x0 + a < x1:
        x = x0 + a
    else:
        x = x0 - a
    y = math.sqrt(length ** 2 - (x - x0) ** 2)
    if y0 > y + y0 > y1 or y0 < y + y0 < y1:
        y += y0
    else:
        y = y0 - y
    return x, y


nnn = int(input())
for i in range(nnn):
    print(f'Road #{i + 1}:')
    k, t = map(int, input().split())
    points = [0] * k
    tree_coords = [0] * t
    for j in range(k):
        points[j] = tuple(map(float, input().split()))
    rlength = road_len(points, k)
    between_length = rlength / (t - 1)
    tree_coords[0], tree_coords[-1] = points[0], points[-1]
    print(f'{dobavit_nol(str(round(tree_coords[0][0], 2)))} '
          f'{dobavit_nol(str(round(tree_coords[0][1], 2)))}')
    for j in range(1, t - 1):
        tree_coords[j] = find_coords_by_length(points, between_length * j)
        print(f'{dobavit_nol(str(round(tree_coords[j][0], 2)))} '
              f'{dobavit_nol(str(round(tree_coords[j][1], 2)))}')
    print(f'{dobavit_nol(str(round(tree_coords[-1][0], 2)))} '
          f'{dobavit_nol(str(round(tree_coords[-1][1], 2)))}')
