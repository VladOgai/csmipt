def countingsort(a):
    lennn = max(a) + 1
    c = [0] * (lennn)
    for i in a:
        c[i] += 1
    a[:] = []
    for number in range(lennn):
        a += [number] * c[number]
    return a


n, l = map(int, input().split())
cc = list(map(int, input().split()))
countingsort(cc)
cc = cc[::-1]
mas = []
counter = 0
lcounter = 0
for c in cc:
    for c1 in cc:
        if c <= c1:
            counter += 1
        elif c == c1 + 1 and lcounter < l:
            lcounter += 1
        else:
            break
    mas.append(min(counter + lcounter, c))
    counter, lcounter = 0, 0
print(max(mas))