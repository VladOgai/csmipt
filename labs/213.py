import matplotlib.pyplot as plt
import numpy as np


T = int(input())

x = np.array([1, 2, 3, 4, 5])
match T:
    case 296:
        l = [695.8, 1038.8, 1386, 1729, 2070.6]
    case 303:
        l = [705.6, 1050, 1401.4, 1747.2, 2095.8]
    case 313:
        l = [716.8, 1065.4, 1422.4, 1775.2, 2126.6]
    case 323:
        l = [728, 1082.2, 1444.8, 1803.2, 2163]

y = np.array(l)
p = []
z = np.polyfit(x, y, 1)
p.append(np.poly1d(z))
plt.plot(x, p[0](x), label=f'T = {T} K')
plt.scatter(x, y)
plt.grid()
plt.xlabel('n')
plt.ylabel('2Lf')
plt.legend()
plt.show()

