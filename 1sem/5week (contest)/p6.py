n, k = map(int, input().split())
a_list = tuple(map(int, input().split()))
sum_list = set()
for i in range(1, 2 ** n + 1):
    j = i ^ k
    if i < j <= 2 ** n:
        sum_list.add(a_list[i] + a_list[j])
print(max(sum_list))