import matplotlib.pyplot as plt
import numpy as np


x = np.array(list(range(31)))
ymmhg = [7.7, 7.6, 7.2, 6.5, 5.7, 4.8, 4.0, 3.4, 2.9, 2.7, 2.2, 1.9, 1.5, 1.4, 1.3, 1.3, 1.2, 1.1, 1, 0.98, 0.96, 0.95,
         0.9, 0.87, 0.85, 0.85, 0.84, 0.83, 0.82, 0.81, 0.8]

y = np.array([np.log(i * 1e-4 - 7.4e-5) for i in ymmhg])
print(len(x))
print(len(y))
p = []
z = np.polyfit(x, y, 1)
p.append(np.poly1d(z))
print(p[0])
plt.plot(x, p[0](x))

plt.scatter(x, y)
plt.grid()
plt.xlabel('t, с')
plt.ylabel('ln(P - Pпр)')
plt.legend()
plt.show()
