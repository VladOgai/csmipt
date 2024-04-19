import matplotlib.pyplot as plt
import numpy as np


plt.title('R = f(T)')

x = np.array([296, 313, 323, 333, 343])
y = [np.array([19.511, 20.715, 21.417, 22.129, 22.839])]

p = []
for i in range(1):
    z = np.polyfit(x, y[i], 1)
    print(i, '  ', z)
    p.append(np.poly1d(z))

plt.plot(x, p[0](x), label='R = f(T)')
plt.scatter(x, y[0], marker='x', color='r')
plt.grid()
plt.xlabel('T')
plt.ylabel('R')
plt.legend()
plt.show()