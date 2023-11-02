inp = int(input())
stacks = []
while inp != 0:
    stacks.append(inp)
    inp = int(input())
odd = [2 * x + 1 for x in range(max(stacks) + 1)]
j = 0
for i in stacks:
    print(odd[i - 3] + j if i >= 3 else 0)
    j = odd[i - 3]