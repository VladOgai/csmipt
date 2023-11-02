def proverit_mid(mid, xx, yy, even=True):
    pdict = dict.fromkeys(yy, [])
    for y, x in zip(yy, xx):
        pdict[y].append(x)
    for y in set(yy):
        if yy.count(y) % 2 == 1:
            return False
        for x in pdict[y]:
            if ((x + 2 * mid in pdict[y]) ^ (x - 2 * mid in pdict[y])) or not even and x == int(mid):
                return True
            return False


n = int(input())
points = []
xs = []
ys = []
for _ in range(n):
    point = tuple(map(int, input().split()))
    points.append(point)
    xs.append(point[0])
    ys.append(point[1])
os = True
xmid = sum(xs) / n
points.sort(key=lambda x: x[1])
match n % 2:
    case 1:
        if xmid % 1 != 0 or int(xmid) not in xs:
            os = False
        else:
            os = proverit_mid(xmid, xs, ys, even=False)
    case 0:
        os = proverit_mid(xmid, xs, ys)
print('Yes' if os else 'No')
