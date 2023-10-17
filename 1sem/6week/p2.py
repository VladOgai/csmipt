from tkinter import *
from tkinter import ttk


def calc_bmi(*args):
    bmi1 = float(mass.get()) / (float(height.get()) ** 2)
    bmi.set(str(bmi1))
    if bmi1 <= 16:
        d = 'Выраженный дефицит массы тела'
    elif bmi1 <= 18.5:
        d = 'Недостаточная (дефицит) масса тела'
    elif bmi1 <= 25:
        d = 'Норма'
    elif bmi1 <= 30:
        d = 'Избыточная масса тела (предожирение)'
    elif bmi1 <= 35:
        d = 'Ожирение 1 степени'
    elif bmi1 <= 40:
        d = 'Ожирение 2 степени'
    else:
        d = 'Ожирение 3 степени'
    diagnoz.set(d)


root = Tk()
root.title('BMI calculator')

mainframe = ttk.Frame(root, padding='3 3 12 12')
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mass = StringVar()
mass_entry = ttk.Entry(mainframe, width=7, textvariable=mass)
mass_entry.grid(column=2, row=1, sticky=(W, E))

height = StringVar()
height_entry = ttk.Entry(mainframe, width=7, textvariable=height)
height_entry.grid(column=2, row=2, sticky=(W, E))

bmi = StringVar()
ttk.Label(mainframe, textvariable=bmi).grid(column=2, row=3)

diagnoz = StringVar()
ttk.Label(mainframe, textvariable=diagnoz).grid(column=2, row=4)

ttk.Button(mainframe, text='Посчитать', command=calc_bmi).grid(column=3, row=5, sticky=W)

ttk.Label(mainframe, text='Масса').grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text='Рост').grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, text='ИМТ').grid(column=3, row=3, sticky=W)
ttk.Label(mainframe, text='Интерпретация ИМТ').grid(column=3, row=4, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.bind('<Return>', calc_bmi)
root.resizable(False, False)
root.mainloop()
