dpL = [0, 1, 2, 4]
dpU = [0, 1, 2, 3]
for _ in range(27):
    dpL.append(dpU[-1] + dpL[-1])
    dpU.append(dpL[-2] + dpL[-3])

inp = int(input())
while inp != 0:
    res = 2 ** inp - dpU[inp] - dpL[inp]
    print(res)
    inp = int(input())