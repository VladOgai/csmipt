import pandas as pd
import numpy as np


def transpose(arr):
    transarr = [[arr[j][i] for j in range(len(arr))] for i in range(len(arr[0]))]
    return transarr


def build_2_tree(mat: list[list[int]], n: int):
    tree = mat.copy()
    tree2 = [[[mat[j][i]] for i in range(len(mat[0]))] for j in range(len(mat))]
    for i in range(n):
        tree[i] = trah_tibidoh_so_strokoy(tree[i])
        tree2[i] = trtr(tree2[i])
    tree = transpose(tree)
    tree2 = transpose(tree2)
    for j in range(len(tree)):
        tree[j] = trah_tibidoh_so_strokoy(tree[j])
        tree2[j] = trtr(tree2[j])
    tree = transpose(tree)
    tree2 = transpose(tree2)
    return tree, tree2


def trtr(arr):
    if len(arr) == 1:
        return arr
    plusarr = []
    if len(arr) % 2 == 0:
        for i in range(0, len(arr), 2):
            plusarr.append([*arr[i], *arr[i + 1]])
    else:
        plusarr.append(arr[0])
        for i in range(1, len(arr), 2):
            plusarr.append([*arr[i], *arr[i + 1]])
    return arr + trtr(plusarr)


def trah_tibidoh_so_strokoy(arr: list[int]):
    if len(arr) == 1:
        return arr
    plusarr = []
    if len(arr) % 2 == 0:
        for i in range(0, len(arr), 2):
            plusarr.append(arr[i] + arr[i + 1])
    else:
        plusarr.append(arr[0])
        for i in range(1, len(arr), 2):
            plusarr.append(arr[i] + arr[i + 1])
    return arr + trah_tibidoh_so_strokoy(plusarr)


def find_result(matrix: list[list[int]], tree: list[list[int]], ref: list[list[list[int]]], x1: int, y1: int, x2: int,
                y2: int) -> int:
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    matrix = np.array(matrix)
    ss = matrix[x1:x2, y1:y2]
    seek = []
    for i in range(len(ss)):
        seek = seek + list(ss[i])
    ind, ind2 = indexxx(ref, seek)
    return tree[ind][ind2]


def indexxx(ar, el):
    ind = 0
    ind2 = 0
    for i in ar:
        try:
            ind2 = i.index(el)
        except ValueError:
            ind2 = -1
        if ind2 != -1:
            break
        ind += 1
    return ind, ind2


N, M, K = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))
sum_tree, reference = build_2_tree(matrix, N)
print(pd.DataFrame(reference))
print(pd.DataFrame(sum_tree))
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())  # почему у нас из условия задачи x по вертикали получается...
    print(find_result(matrix, sum_tree, reference, x1, y1, x2, y2))
