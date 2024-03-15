import matplotlib.pyplot as plt
import numpy as np
import math


plt.title('График 2')
plt.xlabel('1/T, K⁻¹')
plt.ylabel('ln(P)')

x = [1 / i for i in range(293, 314, 2)]
y1 = [math.log(i) for i in [5976, 6304, 6750, 8073, 8999, 10052, 11087, 12325, 13664, 15152, 16803]]
y2 = [math.log(i) for i in [5976, 6817, 7353, 8246, 9167, 10172, 11319, 12546, 13875, 15368, 16803]]

plt.scatter(x, y1, marker='^', color='red')
plt.scatter(x, y2, marker='v', color='blue')

xx = np.array([0.00318, 0.00342])
yy1 = -4940 * xx + 25.51
yy2 = -4747 * xx + 24.89

plt.plot(xx, yy1, label='Нагрев ▲', color='red')
plt.plot(xx, yy2, label='Охлаждение ▼', color='blue')

plt.legend()
plt.grid(linestyle=':')
plt.show()