def gcd(x, y):
    if not x % y:
        return y
    return gcd(y, x % y)


a, b = map(int, input().split())
dd = a / gcd(a, b) * b
res = dd - a - b
if res < 0:
    res += dd
print(int(res))