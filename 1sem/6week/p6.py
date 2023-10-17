from tkinter import *
from tkinter import filedialog
from tkinter import ttk

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def open_csv():
    filetypes = (('.csv table', '*.csv'), ('All files', '*.*'))
    filepath = filedialog.askopenfilename(filetypes=filetypes)
    if filepath[-3:] == 'csv':
        global file
        file = pd.read_csv(filepath)
        mnk.set('Файл загружен')


def save_and_calc():
    filetypes = (('PNG image', '*.png'), ('PDF document', '*.pdf'))
    filepath = filedialog.asksaveasfilename(filetypes=filetypes)
    if filepath:
        xs = list(file['X'])
        ys = list(file['Y'])
        z = np.polyfit(xs, ys, 1)
        x = (min(xs) - 0.5, max(xs) + 1.5)
        p = np.poly1d(z)
        figure = plt.figure()
        axes = figure.add_subplot(1, 1, 1)
        axes.scatter(xs, ys, marker='x', color='r')
        plt.title('y = f(x)')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.plot(x, p(x), label=str(p))
        plt.legend()
        # plt.show()
        figure.savefig(filepath)
        mnk.set(str(p))


file = None

root = Tk()
root.title('p6')
root.columnconfigure(index=0, weight=1)
root.rowconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)

burrito = ttk.Button(text='Открыть файл', command=open_csv)
burrito.grid(column=0, row=0, sticky=NSEW, padx=10)

nachos = ttk.Button(text='Посчитать!', command=save_and_calc)
nachos.grid(column=1, row=0, sticky=NSEW, padx=10)

mnk = StringVar()
ttk.Label(text='Коэффициенты МНК').grid(column=0, row=1, sticky=NSEW)
ttk.Label(textvariable=mnk).grid(column=1, row=1, sticky=NSEW)

root.bind('<Return>', save_and_calc)
root.mainloop()
