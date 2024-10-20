from tkinter import *
from tkinter import ttk
from tkinter import colorchooser
 
root = Tk()
root.title("clr")
root.geometry("250x200")
  
def select_color():
    result1 = colorchooser.askcolor(initialcolor="grey")
    result = result1[1]
    c1,c2,c3 = result[1:3], result[3:5], result[5:7]
    print(c1,c2,c3)
    c_1 = int(c1,16)
    c_2 = int(c2,16)
    c_3 = int(c3,16)
    print(c_1,c_2,c_3)
    c_11 = 255 - c_1
    c_12 = 255 - c_2
    c_13 = 255 - c_3
    print(c_11,c_12,c_13)
    print(hex(c_11), hex(c_12), hex(c_13))
    new = "#" + hex(c_11)[2:4] + hex(c_12)[2:4] + hex(c_13)[2:4]
    out.config(text=new)
 
open_button = ttk.Button(text="Выбрать цвет", command=select_color)
open_button.pack(anchor=NW, padx=10, pady=10)
tax = ttk.Label(root, text="Комплиментарный цвет:")
tax.pack(anchor=NW, padx=10, pady=20)
out = ttk.Label(root, text="")
out.pack(anchor=NW, padx=10, pady=30)
root.mainloop()