import matplotlib.pyplot as plt
import numpy as np


plt.title('k = f(T)')

x = np.array([296, 313, 323, 333, 343])
y = [np.array([0.02564, 0.02646, 0.02729, 0.02837, 0.02903])]
plt.scatter(x, y[0], marker='x', color='r')
p = []
for i in range(1):
    z = np.polyfit(x, y[i], 10)
    print(i, '  ', z)
    p.append(np.poly1d(z))

plt.plot(x, p[0](x), label='k = f(T)')
plt.grid()
plt.xlabel('T')
plt.ylabel('k')
plt.legend()
plt.show()