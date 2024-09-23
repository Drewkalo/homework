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
