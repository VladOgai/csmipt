import random


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)


def bebebe(weights: list[tuple[int]], lower: int, upper: int, size: int) -> list[int]:
    # wsort = quicksort(weights)
    wsort = weights
    cur_sum = 0
    bad_i = 0
    while bad_i < size:
        cur_sum += wsort[bad_i][1]
        if cur_sum > upper:
            break
        bad_i += 1
    if bad_i == 0:
        return [-1]
    picked = []
    remain = []
    curpicked = 0
    for i in range(bad_i):
        picked.append(wsort[i])
        curpicked += wsort[i][1]
    for i in range(bad_i, size):
        remain.append(wsort[i])
    while curpicked < lower and remain:
        if picked[0][1] >= remain[-1][1]:
            break
        curpicked += remain[-1][1] - picked[0][1]
        picked.pop(0)
        a = remain.pop()
        picked.append(a)
    if curpicked < l:
        return [-1]
    answer = []
    for el in picked:
        answer.append(el[0])
    return answer


random.seed(1)
n, l, u = map(int, input().split())
w = list(map(int, input().split()))
w1 = list(enumerate(w))
ans = []
for _ in range(10000):
    random.shuffle(w1)
    ans.append(bebebe(w1, l, u, n))
minn = list(range(n))
for el in ans:
    if sum([w[i] for i in minn]) > sum([w[i] for i in el]) and el != [-1] and sum(minn) > sum(el):
        minn = el
minn = quicksort(minn)
print(*minn)
# print(*bebebe(w, l, u, n))