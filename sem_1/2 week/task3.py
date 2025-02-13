st = input()
flag = True
stold = st
ar = []

for c in st:                #Разбиваю строку на символы
    ar.append(c)


for m in range(len(st)):    #'Отзеркаливание' символов
    if ar[m] == "E":
        ar[m] = "3"
    elif ar[m] == '3':
        ar[m] = 'E'
    elif ar[m] == 'J':
        ar[m] = 'L'
    elif ar[m] == 'L':
        ar[m] = 'J'
    elif ar[m] == 'S':
        ar[m] = '2'
    elif ar[m] == '2':
        ar[m] = 'S'
    elif ar[m] == 'Z':
        ar[m] = '5'
    elif ar[m] == '5':
        ar[m] = 'Z'

mirr = ''.join(ar)[::-1]    #Сборка отзеркаленной строки

for c in 'QDRFCGNBKP':      #Проверка на наличие недопустимых символов
    if c in stold:
        flag = False

if flag == False and stold != stold[::-1]:
    print(f'{stold} is not a palindrome.')
elif stold == stold[::-1] and stold == mirr and flag == True:
    print(f'{stold} is a mirrored palindrome.')
elif stold != stold[::-1] and stold == mirr:
    print(f'{stold} is a mirrored string.')
elif (stold == stold[::-1] and stold != mirr) or (stold == stold[::-1] and stold == mirr and flag == False):
    print(f'{stold} is a regular palindrome')