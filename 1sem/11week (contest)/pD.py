import random


def quicksort(lst, key=lambda x: x):
    if len(lst) < 2:
        return lst
    else:
        pivot = random.choice(lst)
        left = [x for x in lst if key(x) < key(pivot)]
        right = [x for x in lst if key(x) >= key(pivot)]
        return quicksort(left) + quicksort(right)


def bipbup(otrezki):
    otrezki = quicksort(otrezki, key=lambda x: x[1])
    last_end = float('-inf')
    counter = 0
    for l, r in otrezki:
        if l > last_end:
            counter += 1
            last_end = r
    return counter


_, r = map(int, input().split())
otr = [int(i) for i in input().split()]
otr = [(x - r, x + r) for x in otr]
print(bipbup(otr))