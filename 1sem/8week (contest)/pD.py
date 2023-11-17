s = input()
f = True
sk = {'(': ')', '{': '}', '[': ']'}
ls = len(s)
pp = []
if any((ls % 2 == 1, s[0] in sk.values(), s[-1] in sk.keys())):
    f = False

for l in s:
    if l in sk.keys():
        pp.append(l)
    else:
        if l != sk[pp.pop()]:
            f = False

print('Yes' if f else 'No')