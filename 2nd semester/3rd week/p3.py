def count_inversions(arr: list[int]) -> int:
    if len(arr) < 2:
        return 0
    left = arr[:len(arr) // 2]
    right = arr[len(arr) // 2:]
    leftinv = count_inversions(left)
    rightinv = count_inversions(right)
    _, splitinv = merge(left, right)
    res = leftinv + rightinv + splitinv
    return res


def merge(ar1: list[int], ar2: list[int]):
    sortedarr = []
    inv = 0
    while ar1 and ar2:
        l = ar1[0]
        r = ar2[0]
        if l <= r:
            sortedarr.append(l)
            ar1.pop(0)
        else:
            sortedarr.append(r)
            ar2.pop()
            inv += len(ar1)
    sortedarr = sortedarr + ar1 + ar2
    return sortedarr, inv


lst = [3, 2, 1]
print(count_inversions(lst))