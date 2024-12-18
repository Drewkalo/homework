from math import sqrt
#находим первое число, оно гарантированно простое, зануляем все кратные ему, повторяем снова, пока не дойдём до самого числа
a = int(input())
cont = [i for i in range(1+a)]
cont[1] = 0
i = 2
while i < sqrt(a):
    if cont[i] != 0:
        j = i*2
        while j <= a:
            cont[j] = 0
            j = j + i
    i += 1

print(*cont)
