import matplotlib.pyplot as plt
import numpy as np


x = np.array([0.0, 0.25, 1.0, 4.0, 9.0, 16.0, 25.0, 36.0, 49.0])
y = np.array([9.78, 9.77, 9.81, 10.29, 11.01, 12.05, 13.35, 14.8, 16.76])
z = np.polyfit(x, y, 1)
print(z)
p = np.poly1d(z)
# figure = plt.figure()
# axes = figure.add_subplot(1, 1, 1)
plt.plot(x, p(x), color='r', label='y = 0.143x + 9.730')
plt.scatter(x, y, marker='x')
plt.grid()
plt.xlabel('h², см²')
plt.ylabel('I, 10⁻³⋅кг⋅м²')
plt.legend()
plt.show()

