n, b, c = int(input()), int(input()), int(input())
dn = 0
vol = 0
res = ''

for i in str(n)[::-1]:                  #Переводим в 10ую СС
    dn += int(i) * (b ** vol)
    vol += 1

while dn > 0:
    last_d = dn % c                     #Остаток от деления
    res = str(last_d) + res             #res += зеркалит число
    dn //= c

print(res)                              #Например, 123 8 2 выводит 1010011, true
                                        #Например, 123 8 2 выводит 1010011, true