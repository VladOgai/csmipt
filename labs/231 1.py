import matplotlib.pyplot as plt
import numpy as np


x = np.array(list(range(81)))
ymmhg = [0.75, 0.76, 0.77, 0.78, 0.78, 0.78, 0.78, 0.79, 0.79, 0.79, 0.79, 0.8, 0.81, 0.88, 0.91, 1, 1.1, 1.2, 1.3, 1.5,
     1.6, 1.6, 1.7, 1.8, 1.9, 2, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.8, 2.9, 3, 3.1, 3.2, 3.2, 3.3, 3.5, 3.6, 3.7, 3.8, 3.9,
     4, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.9, 5.9, 6, 6.1, 6.2, 6.3,
     6.4, 6.5, 6.6, 6.7, 6.8, 6.9, 7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7]

y = np.array([np.log(i * 1e-4 - 7.4e-5) for i in ymmhg])
print(len(x))
print(len(y))
p = []
z = np.polyfit(x[:20], y[:20], 1)
p.append(np.poly1d(z))
print(p[0])
plt.plot(x, p[0](x))
p = []
z = np.polyfit(x[20:], y[20:], 1)
p.append(np.poly1d(z))
print(p[0])
plt.plot(x, p[0](x))
plt.scatter(x, y)
plt.grid()
plt.xlabel('t, с')
plt.ylabel('ln(P - Pпр)')
plt.legend()
plt.show()
