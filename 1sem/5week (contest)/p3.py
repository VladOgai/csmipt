n, m = map(int, input().split())
i, res = 0, 0
while (n != 1 or m != 1) and n % 2 == 1 and m % 2 == 1:  # считаем кол-во возм. "разделений" на 4 поля (их i - 1)
    n = int((n - 1) / 2)
    m = int((m - 1) / 2)
    i += 1
for x in range(i):
    res += 4 ** x
print(res)
