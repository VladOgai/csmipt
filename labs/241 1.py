import matplotlib.pyplot as plt


plt.title('График 1')
plt.xlabel('T, K')
plt.ylabel('P, Па')

x = [293, 295, 297, 299, 301, 303, 305, 307, 309, 311, 313]
y1 = [5976, 6304, 6750, 8073, 8999, 10052, 11087, 12325, 13664, 15152, 16803]
y2 = [5976, 6817, 7353, 8246, 9167, 10172, 11319, 12546, 13875, 15368, 16803]

plt.scatter(x, y1, marker='^', color='red')
plt.plot(x, y1, color='red', label='Нагрев ▲')

plt.scatter(x, y2, marker='v', color='blue')
plt.plot(x, y2, color='blue', label='Охлаждение ▼')

plt.legend()
plt.grid(linestyle=':')
plt.show()