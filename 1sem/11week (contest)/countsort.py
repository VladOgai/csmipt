def countingsort(a):
    c = [0] * (max(a) + 1)
    for i in a:
        c[i] += 1
    a[:] = []
    for number in range(max(a) + 1):
        a += [number] * c[number]