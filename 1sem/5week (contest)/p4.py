n = int(input())
lst = list(map(int, input().split()))
lst2 = lst.copy()
res = 0
for i in range(n - 2, -1, -1):
    lst2[i] = max(lst[i], lst2[i + 1])
for i in range(n):
    res += lst2[i] - lst[i]
print(res)