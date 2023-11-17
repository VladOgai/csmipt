def max_stir(ch: str, d: int) -> int:
    res_list = []
    for digit in ch:
        while res_list and d > 0 and int(res_list[-1]) < int(digit):
            res_list.pop()
            d -= 1
        res_list.append(digit)
    if d > 0:
        res_list = res_list[:-d]
    return ''.join(res_list)


while True:
    n, d = map(int, input().split())
    if n == 0 and d == 0:
        break
    ch = input()
    print(max_stir(ch, d))