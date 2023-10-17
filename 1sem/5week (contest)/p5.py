import itertools as it


n, m = map(int, input().split())
par = []
for _ in range(m):
    par.append(set(map(int, input().split())))
soch = set(it.combinations(range(1, n + 1), 3))
bb = soch.copy()
for s in bb:
    ss = set(s)
    sss = [set(p) & ss == set(p) for p in par]
    if any(sss):
        soch.discard(s)
print(len(soch))