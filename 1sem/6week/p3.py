import random as rnd
from tkinter import *
from tkinter import ttk

import pandas as pd


def find_film(*args):
    g = str(genre.get())
    g = g.capitalize()
    if g not in genres_set:
        film.set('There is no such genre in top')
    else:
        flist = film_dict[g]
        film.set(rnd.choice(flist))


films = pd.read_csv('imdb_top_250.csv')
film_genres_list = list(films['Genre'])
film_dict = dict()
complex_genres = []
for film_genre in film_genres_list:
    genres = film_genre.split(' | ')
    if len(genres) > 1:
        for genre in genres:
            film_genres_list.append(genre)
        complex_genres.append(film_genre)
for genre in complex_genres:
    film_genres_list.remove(genre)
genres_set = set(film_genres_list)

for gen in genres_set:
    film_dict[gen] = []
    for num in range(len(films['Title'])):
        if gen in films['Genre'][num]:
            film_dict[gen].append(films['Title'][num])

root = Tk()
mainframe = ttk.Frame(root, padding='3 3 12 12')
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, text='Enter genre:').grid(column=2, row=1)
genre = StringVar()
g_entry = ttk.Entry(mainframe, width=15, textvariable=genre)
g_entry.grid(column=3, row=1)

film = StringVar()
ttk.Label(mainframe, text='Film:').grid(column=2, row=3)
ttk.Label(mainframe, textvariable=film).grid(column=3, row=3)

ttk.Button(mainframe, text='Find smth to watch tonight!', command=find_film).grid(column=2, row=2, columnspan=2)
root.bind('<Return>', find_film)
root.resizable(False, False)
root.mainloop()
