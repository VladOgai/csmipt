'''
1) Наибольшее число

Задан массив неотрицательных целых чисел. Расположите их так, чтобы образовалось наибольшее число.

Например, из массива чисел [3, 30, 34, 5, 9] наибольшее можно получить число 9534330.
'''


def cringe_max(ls: list) -> str:
    res = ls[0]
    for i in range(1, len(ls)):
        if len(res) == len(ls[i]):
            res = max(res, ls[i])
        elif len(res) != len(ls[i]):
            a = res * len(ls[i])
            b = ls[i] * len(res)
            res = (res, ls[i])[a < b]
    return res


lst = ['3', '30', '34', '5', '9']
s = ''
for _ in range(len(lst)):
    x = cringe_max(lst)
    s += x
    lst.remove(x)
print(s)