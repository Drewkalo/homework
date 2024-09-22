f = open('C:/Users/Эльмира/Documents/GitHub/homework/1 week/input1.txt', 'r')
strnum = f.readline().strip()
op = f.readline().strip()
b = f.readline().strip()
dn = 0
vol = 0
d_l = []
num = [int(i) for i in strnum.split()]

print(num)                      #Проверка

for curr in num:                #Преобразовываем числа в 10ую СС
    dn = 0
    vol = 0
    for j in str(curr)[::-1]:
        dn += int(curr) * (int(b[0]) ** vol)
        vol += 1
    d_l.append(dn)

print(d_l)                      #Проверка

if op[0] == '+':                #Выполняем операцию
    s = sum(d_l)
elif op[0] == '-':
    s = d_l[0] - sum(d_l[1:])
elif op[0] == '*':
    s = 1
    for q in d_l:
        s += q

otv = ''                        #Переводим в ту же СС
while s > 0:
    ld = s % int(b[0])
    otv = str(ld) + otv
    s //= int(b[0])

print(otv)                      #Проверка

f.close()
z = open('C:/Users/Эльмира/Documents/GitHub/homework/1 week/output1.txt', 'w')
z.write(str(s))
z.close()                       #Например, сумму чисел 1 2 3 в четверичной СС он посчитал, получилось 12, true