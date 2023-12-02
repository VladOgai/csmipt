def maxheapify(lst, i):
    n = len(lst)
    while True:
        l = 2 * i + 1
        r = 2 * i + 2
        max = i
        if l < n and lst[max] < lst[l]:
            max = l
        if r < n and lst[max] < lst[r]:
            max = r
        if max == i:
            break
        lst[max], lst[i] = lst[i], lst[max]
        i = max


def makeheap(lst):
    n = len(lst) // 2 - 1
    for i in range(n, -1, -1):
        maxheapify(lst, i)
    return lst


s = list(map(int, input().split()))
print(*makeheap(s))