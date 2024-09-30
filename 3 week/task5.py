import numpy as np
def paint(N,M):
    a = np.zeros((N,M))
    k = 1                   #Число в ячейку
    i = 0                   #Строки
    j = 0                   #Столбцы
    while (k < M*N):
        while j+1 < M and a[i][j+1] == 0:
            a[i][j] = k
            k += 1
            j += 1
        while i+1 < N and a[i+1][j] == 0:
            a[i][j] = k
            k += 1
            i += 1
        while j > 0 and a[i][j-1] == 0:
            a[i][j] = k
            k += 1
            j -= 1
        while i > 0 and a[i-1][j] == 0:
            a[i][j] = k
            k += 1
            i -= 1
    a[i][j] = k
    return a

a = int(input("Число строк"))
b = int(input("Число столбцов"))

print(paint(a,b))
