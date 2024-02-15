# Реализуйте структуру данных для эффективного вычисления НОД нескольких подряд идущих элементов массива.
# Входные данные:
# В первой строке вводится одно натуральное число N (1 ≤ N ≤ 100000) — количество чисел в массиве. Во второй
# строке вводятся N чисел от 1 до 100000 — элементы массива. В третьей строке вводится одно натуральное число K
# (1 ≤ K ≤ 30000) — количество запросов на вычисление НОД. В следующих K строках вводится по два
# числа — номера левого и правого элементов отрезка массива (считается, что элементы массива нумеруются с единицы).'
# Выходные данные:
# Для каждого запроса выведите НОД всех чисел соответствующего участка массива. Числа выводите в одну строку через
# пробел.


from math import gcd


def mktree(a: list[int], lng: int) -> list[list[int]]:
    tree = [None] * (4 * lng)
    tree[0] = a
    for i in range(1, 4 * lng):
        if tree[i] is not None:
            continue
        if (i & 1) == 1:
            coretree = tree[(i - 1) // 2]
            if coretree is None or len(coretree) == 1:
                continue
            tree[i] = coretree[:len(coretree) // 2]
        else:
            coretree = tree[(i - 2) // 2]
            if coretree is None or len(coretree) == 1:
                continue
            tree[i] = coretree[len(coretree) // 2:]
    while tree[-1] is None:
        tree.pop()
    return tree


def tree_w_gcd(tree: list[list[int]]) -> list[int]:
    restree = [None] * len(tree)
    for i in range(len(tree) - 1, -1, -1):
        if tree[i] is None:
            continue
        elif len(tree[i]) == 1:
            restree[i] = tree[i][0]
            continue
        a = restree[2 * i + 1]
        b = restree[2 * i + 2]
        if a is None and b is not None:
            restree[i] = b
        elif b is None and a is not None:
            restree[i] = a
        elif a is None and b is None:
            restree[i] = None
        else:
            restree[i] = gcd(a, b)
    return restree


def find_otrezok(tree: list[list[int]], left: int, right: int) -> list[int]:
    ar = tree[0]
    seek = ar[left - 1:right]
    inds = []
    i = 0
    while seek:
        d = tree[i]
        if d is not None and (set(d) & set(seek)) == set(d):
            inds.append(i)
            subseek = []
            for x in seek:
                if x not in d:
                    subseek.append(x)
            seek = subseek
        i += 1
    return inds


def find_gcd(tree: list[list[int]], left: int, right: int) -> int:
    subtree = tree_w_gcd(tree)
    indexes = find_otrezok(tree, left, right)
    gcd_array = [subtree[i] for i in indexes]
    gcd_array = list(set(gcd_array))
    return gcd(*gcd_array)


n = int(input())
massiv = list(map(int, input().split()))
treee = mktree(massiv, n)
k = int(input())
result = []
for _ in range(k):
    l, r = map(int, input().split())
    result.append(find_gcd(treee, l, r))
print(*result)
