import matplotlib.pyplot as plt
import numpy as np


x = np.array([1, 2, 3, 4, 5])
x0 = np.array([0, 1, 2, 3, 4, 5])
y1 = np.array([3218.2, 6459, 9686, 12908, 16116.7])
y2 = np.array([4128.3, 8265.3, 12391.3, 16516, 20630.7])
y3 = np.array([4242.7, 8529.7, 12737.3, 16990.7, 21211.7])
y = [y1, y2, y3]
p = []
for i in range(3):
    z = np.polyfit(x, y[i], 1)
    print(i, '  ', z)
    p.append(np.poly1d(z))
plt.plot(x0, p[0](x0), color='r', label='Медь, ×, y = 3224.6x + 3.8')
plt.scatter(x, y[0], marker='x')
plt.plot(x0, p[1](x0), color='b', label='Сталь, +, y = 4125.6x + 9.7')
plt.scatter(x, y[1], marker='P')
plt.plot(x0, p[2](x0), color='g', label='Дюраль, ■, y = 4239.9x + 22.7')
plt.scatter(x, y[2], marker='s')
plt.grid()
plt.xlabel('n, номер гармоники')
plt.ylabel('fₙ, собственные частоты')
plt.legend()
plt.show()
