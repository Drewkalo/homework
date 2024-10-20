'''def step(fin,  n = {1:1, 2:1}):
    if fin in n:
        return n[fin]
    else:
        n[fin] = step(fin-1,n) + step(fin-2,n)
        return n[fin]
    
print(step(1000))
'''
import tkinter as tk

def calculate():
  try:
    result = str(eval(entry.get()))
    output_label.config(text=result)
  except Exception as e:
    output_label.config(text="Ошибка")

root = tk.Tk()
root.title("Калькулятор")

entry = tk.Entry(root, width=30)
entry.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

calculate_button = tk.Button(root, text="Рассчитать", command=calculate)
calculate_button.grid(row=1, column=0, padx=10, pady=10)

output_label = tk.Label(root, text="")
output_label.grid(row=1, column=1, padx=10, pady=10)

root.mainloop()