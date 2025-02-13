from tkinter import *
#код на основе примера из семинара
root = Tk()     
root.title("Приложение на Tkinter")    
root.geometry("200x200")   
 
label = Label(text="Калькулятор ИМТ") 
label.pack()
def callback(*args):
    try:
        out.config(text=str(float(m.get())/(float(rost.get()))**2))
        if (float(m.get())/(float(rost.get()))**2) >= 40:
            out2.config(text="У вас ожирение 3 степени")
        elif 35 <=(float(m.get())/(float(rost.get()))**2) < 40:
            out2.config(text="У вас ожирение 2 степени")
        elif 30 <=(float(m.get())/(float(rost.get()))**2) < 35:
            out2.config(text="У вас ожирение 1 степени")
        elif 25 <=(float(m.get())/(float(rost.get()))**2) < 30:
            out2.config(text="У вас предожирение")
        elif 18.5 <=(float(m.get())/(float(rost.get()))**2) < 25:
            out2.config(text="ИМТ в норме")
        elif 16 <=(float(m.get())/(float(rost.get()))**2) < 18.5:
            out2.config(text="У вас дефицит массы тела")
        else:
            out2.config(text="У вас выраженный дефицит массы тела")

    except ZeroDivisionError:
        out2.config(text="Error")

rost = StringVar()
rost_entry = Entry(root, textvariable=rost)
rost_entry.pack()

m = StringVar()
m_entry = Entry(root, textvariable=m)
m_entry.pack()

btn = Button(root, text="=", command = callback)
out = Label(root, text = "Введите рост в м. в первое окно, массу в кг. - во второе") 
out2 = Label(root, text = '')
btn.pack(ipadx=50)
out.pack()
out2.pack()
root.mainloop()