import pandas as pd
import numpy as np


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


def transpose(arr):
    transarr = [[arr[j][i] for j in range(len(arr))] for i in range(len(arr[0]))]
    return transarr


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
    ss = matrix[y1:y2, x1:x2]
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


def update_sumtree(tree: list[list[int]], n: int, x: int, y: int, num: int) -> list[list[int]]:
    tree[y], che_menyalos, prev = update_row(tree[y], n, x, num)
    tree = transpose(tree)
    for s in che_menyalos:
        tree[s], _, _ = update_row(tree[s], n, y, num, prev)
    tree = transpose(tree)
    return tree


def update_row(row: list[int], n: int, x: int, num: int, prev=None):
    if prev is None:
        prev = row[x]
        row[x] = num
    xx = int(x)
    che_menyalos = []
    i = 1
    while len(row) - i != xx:
        row[-i] = row[-i] + num - prev
        che_menyalos.append(len(row) - i)
        if x >= n // 2:
            i = 2 * i
            x -= n // 2
            n //= 2
        else:
            i = 2 * i + 1
            n //= 2
    che_menyalos.append(xx)
    return row, che_menyalos, prev


def update_ref_row(row: list[list[int]], n: int, x: int, num: int, prev=None):
    if prev is None:
        prev = row[x][0]
        row[x] = [num]
    xx = int(x)
    che_menyalos = []
    i = 1
    while len(row) - i != xx:
        j = row[-i].index(prev)
        row[-i].remove(prev)
        row[-i].insert(j, num)
        che_menyalos.append(len(row) - i)
        if x >= n // 2:
            i = 2 * i
            x -= n // 2
            n //= 2
        else:
            i = 2 * i + 1
            n //= 2
    che_menyalos.append(xx)
    return row, che_menyalos, prev


def update_reftree(ref: list[list[list[int]]], n: int, x: int, y: int, num: int) -> list[list[list[int]]]:
    ref[y], che_tut_menyalos, prev = update_ref_row(ref[y], n, x, num)
    ref = transpose(ref)
    for s in che_tut_menyalos:
        ref[s], _, _ = update_ref_row(ref[s], n, y, num, prev)
    ref = transpose(ref)
    return ref


t = int(input())
for _ in range(t):
    n = int(input())
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    sumtree, reftree = build_2_tree(matrix, n)
    inputs = input()
    while inputs != 'END':
        match inputs[:3]:
            case 'SET':
                x, y, num = map(int, inputs[3:].split())
                matrix[y][x] = num
                sumtree = update_sumtree(sumtree, n, x, y, num)
                reftree = update_reftree(reftree, n, x, y, num)
                # print(pd.DataFrame(matrix))
                # print()
                # print(pd.DataFrame(sumtree))
                inputs = input()
            case 'SUM':
                x1, y1, x2, y2 = map(int, inputs[3:].split())
                print(find_result(matrix, sumtree, reftree, x1, y1, x2 + 1, y2 + 1  ))
                inputs = input()
            case _:
                inputs = input()
                continue
    print()
