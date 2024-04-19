import matplotlib.pyplot as plt
import numpy as np
import math


plt.title('ln(k) = f(ln(T))')

x = np.array([math.log(i) for i in [296, 313, 323, 333, 343]])
y = [np.array([math.log(i) for i in [0.02564, 0.02646, 0.02729, 0.02837, 0.02903]])]
plt.scatter(x, y[0], marker='x', color='r')
p = []
for i in range(1):
    z = np.polyfit(x, y[i], 1)
    print(i, '  ', z)
    p.append(np.poly1d(z))

plt.plot(x, p[0](x), label='ln(k) = f(ln(T))')
plt.grid()
plt.xlabel('ln(T)')
plt.ylabel('ln(k)')
plt.legend()
plt.show()