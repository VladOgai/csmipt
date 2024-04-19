MAX = 100001
F = []
def summa_i(i):
    result = 0
    while(i >= 0):
        result += F[i]
        i = (i & (i + 1)) - 1
    return result

def inc_element(i, d):
    while(0 < i and i < MAX):
        F[i] = F[i] + d
        i = i|(i+1)

def func():
    test = int(input())
    for _ in range(test):
        n = int(input())
        global F
        F = [0 for _ in range(MAX + 1)]
        s = 0
        a = list(map(int,input().split(' ')))
        for i in a:
            inc_element(i, i)
            s += summa_i(i - 1)
        print(s)

func()