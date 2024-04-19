def fen_func(x: int, delta: int, f: list[int]) -> list[int]:
    while 0 < x < len(f):
        f[x] = f[x] + delta
        x = x | (x + 1)
    return f


def fen_sum(i: int, f: list[int]) -> int:
    res = 0
    while i >= 0:
        res += f[i]
        i = (i & (i + 1)) - 1
    return res


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        stairs = list(map(int, input().split()))
        f = [0] * (10 ** 5)
        res = 0
        for step in stairs:
            f = fen_func(step, step, f)
            res += fen_sum(step - 1, f)
        print(res)


if __name__ == '__main__':
    main()