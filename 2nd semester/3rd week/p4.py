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


def find_k_stat(arr, k, a, b):
    n = len(arr)
    tree = mktree(arr, n)
    inds = find_otrezok(tree, a, b)
    newarr = []
    for i in inds:
        x = tree[i]
        newarr = newarr + x
    newarr.sort()
    res = newarr[k - 1]
    return res


massiv = [1, 5, 8, 3, 9, 0, 2, 2, 9, 4, 3, 7]
a = 1
b = 5
k = 3
print(find_k_stat(massiv, k, a, b))
