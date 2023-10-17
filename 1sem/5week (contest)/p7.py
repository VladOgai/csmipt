def bob(n: int) -> int:
    global mem1  # я лентяй, поэтому мемоизация оформлена через глобальную переменную
    if n in mem1:
        return mem1[n]
    mem1[n] = bob(n - 2) + bob(n - 1)
    return mem1[n]


def kul(n: int) -> str:
    global mem2
    if n in mem2:
        return mem2[n]
    mem2[n] = kul(n - 2) + kul(n - 1)
    return mem2[n]


def find_num(ll: int) -> int:
    i = 0
    while True:
        if bob(i) > ll:
            break
        else:
            i += 1
    return i


m = int(input())
n_list = []
k_list = []
mem1 = {0: 1, 1: 1}
mem2 = {0: 'a', 1: 'b'}
for _ in range(m):
    n, k = map(int, input().split())
    n_list.append(n)
    k_list.append(k)
stroka = kul(find_num(max(k_list)))
for i in range(m):
    n1, k1 = n_list[i], k_list[i]
    if k1 > 2:
        print(stroka[k1 - 1])
    elif (k1 + n1) % 2:
        print('a')
    else:
        print('b')
