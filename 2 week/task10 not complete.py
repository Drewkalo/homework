with open('C:/Users/Эльмира/Documents/GitHub/homework/2 week/input1.txt','r') as a, open('C:/Users/Эльмира/Documents/GitHub/homework/2 week/output.txt',"w") as z:
    b = a.readlines()
print(b)
for _ in b:
    con = []
    for j in range(len(_)):
        if _[j] in "уеэоаыяи" and _[j+1] in "уеэоаыяи":
            continue
        if _[j] in 'уеэоаыяи':
            con.append(_[j])
            con.append("с" + _[j])
            continue
    con.append(_[j])
    z.write(''.join(con))
   
