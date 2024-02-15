import matplotlib.pyplot as plt
import numpy as np


x = np.array([0.0034, 0.00331, 0.00325, 0.00319, 0.0031])
# x0 = np.array([0, 1, 2, 3, 4, 5])
# y1 = np.array([3218.2, 6459, 9686, 12908, 16116.7])
y2 = np.array([0.07696, -0.51083, -0.8916, -1.38629, -1.96611])
# y3 = np.array([4242.7, 8529.7, 12737.3, 16990.7, 21211.7])
y = [y2]
p = []
for i in range(1):
    z = np.polyfit(x, y[i], 1)
    print(i, '  ', z)
    p.append(np.poly1d(z))
# plt.plot(x0, p[0](x0), color='r', label='Медь, ×, y = 3224.6x + 3.8')
# plt.scatter(x, y[0], marker='x')
plt.plot(x, p[0](x), label='ln(η) = f(1/T)')
plt.scatter(x, y[0], marker='x', color='r')
# plt.plot(x0, p[2](x0), color='g', label='Дюраль, ■, y = 4239.9x + 22.7')
# plt.scatter(x, y[2], marker='s')
plt.grid()
plt.xlabel('1/T')
plt.ylabel('ln(η)')
plt.legend()
plt.show()
