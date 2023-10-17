from tkinter import *
from tkinter import ttk


def calculate(*args):
    cal = str(calc.get())
    res.set(str(eval(cal)))


root = Tk()
root.title('Kalkulator')
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
calc = StringVar()
calc_entry = ttk.Entry(mainframe, width=20, textvariable=calc)
calc_entry.grid(column=2, row=1, sticky=(W, E))
res = StringVar()
ttk.Label(mainframe, textvariable=res).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text='Посчитать', command=calculate).grid(column=3, row=3, sticky=W)
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)
calc_entry.focus()
root.bind('<Return>', calculate)
root.resizable(False, False)
root.mainloop()
