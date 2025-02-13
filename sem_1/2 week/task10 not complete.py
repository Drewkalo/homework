with open('C:/Users/Эльмира/Documents/GitHub/homework/2 week/input1.txt','r') as a, open('C:/Users/Эльмира/Documents/GitHub/homework/2 week/output.txt',"w") as z:
    b = a.readlines()
    i = 0
    for j in b:
        if i + 1 > len(j):
        if j[i] in "уеэоаыяи" and _[i+1] in "уеэоаыяи":
            continue
        if _[j] in 'уеэоаыяи':
            con.append(_[j])
            con.append("с" + _[j])
            continue
   



with open('C:/Users/Эльмира/Documents/GitHub/homework/2 week/output.txt',"w") as z:
    z.write(con)
   
     