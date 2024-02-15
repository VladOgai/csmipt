# Реализуйте структуру данных для эффективного вычисления максимумов подряд идущих элементов массива.
# Входные данные:
# В первой строке вводится одно натуральное число N (1 ≤ N ≤ 100000) — количество чисел в массиве.
# Во второй строке вводятся N чисел от 1 до 100000 — элементы массива. В третьей строке вводится одно натуральное
# число K (1 ≤ K ≤ 30000) — количество запросов на вычисление максимума.
# В следующих K строках вводится по два числа — номера левого и правого элементов отрезка массива (считается,
# что элементы массива нумеруются с единицы).
# Выходные данные:
# Для каждого запроса выведите значение максимального элемента на указанном отрезке массива. Числа выводите в одну
# строку через пробел.

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


def tree_w_max(tree: list[list[int]]) -> list[int]:
    restree = [None] * len(tree)
    for i in range(len(tree) - 1, -1, -1):
        if tree[i] is None:
            restree[i] = float('-inf')
            continue
        if len(tree[i]) == 1:
            restree[i] = tree[i][0]
            continue
        a = restree[2 * i + 1]
        b = restree[2 * i + 2]
        if a >= b:
            restree[i] = a
        else:
            restree[i] = b
    return restree


def find_otrezok(tree: list[list[int]], left: int, right: int) -> list[int]:
    ar = tree[0]
    seek = ar[left:right + 1]
    inds = []
    i = 1
    while seek:
        d = tree[i]
        if d is not None and (set(d) & set(seek)) == set(d):
            inds.append(i)
            subseek = []
            for x in seek:
                if x not in tree[i]:
                    subseek.append(x)
            seek = subseek
        i += 1
    return inds


def find_max(tree: list[list[int]], lng: int, left: int, right: int) -> int:
    subtree = tree_w_max(tree)
    indexes = find_otrezok(tree, left, right)
    maxes = [subtree[i] for i in indexes]
    maxes = set(maxes)
    return max(maxes)


n = int(input())
massiv = list(map(int, input().split()))
tree = mktree(massiv, n)
k = int(input())
result = []
for _ in range(k):
    left, right = map(int, input().split())
    result.append(find_max(tree, n, left - 1, right - 1))
print(*result)