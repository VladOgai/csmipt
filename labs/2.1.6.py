import matplotlib.pyplot as plt
import numpy as np
#
#
# plt.title('График 1')
# plt.xlabel('|ΔP|, бар')
# plt.ylabel('-ΔT, К')
#
# xerr = 0.05
#
# x1 = [1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
# y1 = [0.15, 0.54, 0.93, 1.35, 1.79, 2.21]
# y1err = 0.025
#
# x2 = [2.5, 3.0, 3.5, 4.0, 4.5]
# y2 = [0.65, 0.99, 1.42, 1.81, 2.17]
# y2err = 0.024
#
# x3 = x2.copy()
# y3 = [0.09, 0.35, 0.68, 1.01, 1.25]
# y3err = 0.024
#
# x4 = [3.0, 3.5, 4.0, 4.5]
# y4 = [0.23, 0.51, 0.76, 1.00]
# y4err = 0.023
#
# plt.scatter(x1, y1, marker='x')
# plt.scatter(x2, y2, marker='x')
# plt.scatter(x3, y3, marker='x')
# plt.scatter(x4, y4, marker='x')
#
# for xx, y, yerr in [(x1, y1, y1err), (x2, y2, y2err), (x3, y3, y3err), (x4, y4, y4err)]:
#     for i in range(len(xx)):
#         plt.errorbar(xx[i], y[i], xerr=xerr, yerr=yerr, color='black')
#
# x = np.arange(1, 5, 0.01)
# yy1 = 0.8269 * x - 1.112
# yy2 = 0.772 * x - 1.294
# yy3 = 0.596 * x - 1.41
# yy4 = 0.512 * x - 1.295
#
# plt.plot(x, yy1, dashes=[2, 2], label='t = 25°C')
# plt.plot(x, yy2, dashes=[4, 2], label='t = 35°C')
# plt.plot(x, yy3, dashes=[6, 2], label='t = 45°C')
# plt.plot(x, yy4, dashes=[8, 2], label='t = 55°C')
#
# plt.grid(linestyle=':')
# plt.legend()
# plt.show()


plt.title('График 2')
plt.xlabel('1/T, K⁻¹')
plt.ylabel('μ Д-Т, K/бар')

yerr = [0.013, 0.019, 0.015, 0.0099]

x = [0.003047, 0.003143, 0.003252, 0.003354]
y = [0.512, 0.596, 0.772, 0.8269]

plt.scatter(x, y, marker='x')

for i in range(4):
    plt.errorbar(x[i], y[i], yerr=yerr[i], color='black')

xx = np.arange(0.003, 0.0034, 0.00000001)
yy = 1090 * xx - 2.81

plt.plot(xx, yy)

plt.grid(linestyle=':')
plt.show()