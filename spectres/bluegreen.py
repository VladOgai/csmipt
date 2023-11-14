import pandas as pd
import matplotlib.pyplot as plt

dd = pd.read_csv('0211bluegreen.csv', delimiter=';')
x = dd['X'].tolist()
x = [float(i.replace(',', '.')) for i in x]
y = dd['Y'].tolist()
y = [float(i.replace(',', '.')) for i in y]
plt.plot(x, y)
plt.show()
