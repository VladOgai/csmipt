import random


def quicksort(lst, l=0, r=None):
    if r is None:
        r = len(lst) - 1
    if l >= r:
        return
    else:
        q = random.choice(lst[l:r + 1])
        i = l
        j = r
        while i <= j:
            while lst[i] < q:
                i += 1
            while lst[j] > q:
                j -= 1
            if i <= j:
                lst[i], lst[j] = lst[j], lst[i]
                i += 1
                j -= 1
                quicksort(lst, l, j)
                quicksort(lst, i, r)


inp = list(map(int, input().split()))
quicksort(inp)
print(*inp)