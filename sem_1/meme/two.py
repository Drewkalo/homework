from tkinter import *
from tkinter import ttk
from tkinter import colorchooser
 
root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")
 
label = ttk.Label(text="Hello World")
label.pack(anchor=NW, padx=10, pady=10)
 
def select_color():
    result = colorchooser.askcolor(initialcolor="black")
    print(result[1])
    label["foreground"] = result[1]
 
open_button = ttk.Button(text="Выбрать цвет", command=select_color)
open_button.pack(anchor=NW, padx=10, pady=10)
 
root.mainloop()