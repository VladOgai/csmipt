fc = input().strip('#')
xx = '0x' + fc[:2]
yy = '0x' + fc[2:4]
zz = '0x' + fc[4:]
aa = hex(int(255 - float.fromhex(xx))).strip('0x')
bb = hex(int(255 - float.fromhex(yy))).strip('0x')
cc = hex(int(255 - float.fromhex(zz))).strip('0x')
s = '#'
for x in (aa, bb, cc):
    match len(x):
        case 0:
            s += '00'
        case 1:
            s += '0' + x
        case 2:
            s += x
print(s)
