with open('C:/Users/Эльмира/Documents/GitHub/homework/2 week/input1.txt','r') as f_in, open('C:/Users/Эльмира/Documents/GitHub/homework/2 week/output.txt',"w") as f_out:
    for line in f_in:
        output = ""
        previous_char = ""  # Храним предыдущий символ
        for char in line:
            if char in "аеиоуыэюя":
                if previous_char not in "аеиоуыэюя":  # Проверка, был ли предыдущий символ согласным
                    output += char + "с" + previous_char 
                else:
                    output += char
            else:
                output += char
            previous_char = char  # Обновление предыдущего символа
        f_out.write(output)

with open('C:/Users/Эльмира/Documents/GitHub/homework/2 week/input1.txt','r') as a, open('C:/Users/Эльмира/Documents/GitHub/homework/2 week/output.txt',"w") as z:
    b = a.readlines()
    


with open('C:/Users/Эльмира/Documents/GitHub/homework/2 week/output.txt',"w") as z:
    z.write(con)
   
     for j in range(len(_)):
        if _[j] in "уеэоаыяи" and _[j+1] in "уеэоаыяи":
            continue
        if _[j] in 'уеэоаыяи':
            con.append(_[j])
            con.append("с" + _[j])
            continue