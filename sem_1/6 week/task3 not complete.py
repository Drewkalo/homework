import pandas as pd
from tkinter import *
from random import *

films = pd.read_csv('C:/Users/Эльмира/Documents/GitHub/homework/6 week/imdb_top_250.csv')
film_genres_list = list(films['Genre'])

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

root = Tk()
root.title("Приложение на Tkinter")    
root.geometry("200x200")   
 
label = Label(text="Рекомендации") 
label.pack()
ff = [c for c in films["Genre"] if c == 'War']
print(ff)
'''
def rec(*args):
    ff = [c for c in films["Genre"] if c == tax.get()]
    out.config(text=str(ff[randint(0, len(ff))]))
            
tax = StringVar()
tax_entry = Entry(root, textvariable=tax)
tax_entry.pack()
out = Label(root, text="Фильм")
btn = Button(root, text="Тык!", command=rec())
btn.pack()
out.pack()
root.mainloop()
'''