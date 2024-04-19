def main():
    nn = int(input())
    starts = list(map(int, input().split()))
    ends = list(map(int, input().split()))
    vstrechi = []
    for i in range(len(ends)):
        vstrechi.append((starts[i], ends[i], i))

    vstrechi.sort(key=lambda x: x[1])
    i = 0
    res = [vstrechi[i]]
    for j in range(1, nn):
        if vstrechi[j][0] > vstrechi[i][1]:
            res.append(vstrechi[j])
            i = j
    print(len(res))


if __name__ == '__main__':
    main()