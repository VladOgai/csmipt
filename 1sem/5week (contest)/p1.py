banks = list(map(int, input().split()))
if len(banks) < 3:
    print(max(banks))
else:
    banks[2] = banks[0] + banks[2]
    for i in range(3, len(banks)):
        banks[i] = banks[i] + max(banks[i - 2], banks[i - 3])
    print(max(banks))