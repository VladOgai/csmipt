from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Приложение на Tkinter')
root.geometry('300x300')
label = Label(text='Hello')
label.pack()
btn = ttk.Button(text='Click!')
btn.pack()

root.mainloop()