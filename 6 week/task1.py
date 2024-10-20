from tkinter import *
#код на основе примера из семинара
root = Tk()     
root.title("Приложение на Tkinter")    
root.geometry("200x200")   
 
label = Label(text="Калькулятор") 
label.pack()

def callback(*args):
    try:
        out.config(text=str(eval(data.get())))
    except ZeroDivisionError:
        out.config(text="Error")
data = StringVar()
data_entry = Entry(root, textvariable=data)
data_entry.pack()

btn = Button(root, text="=", command = callback)
out = Label(root, text = '') 
out.pack()
btn.pack(ipadx=50)
root.mainloop()