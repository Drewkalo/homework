import numpy as np

def linsys(n, m, matr):           #Кол-во строк в матрице = n, число столбцов = m, сама матрица
  a = matr[:, :m-1]               # Коэффициенты уравнений, все строчки кроме последнего столбца
  b = matr[:, m-1:]               # Свободные члены, послежний столбец

                                    #Честно подсмотренно на хабре про обработку ошибок, потому что не додумался, как исключить ошибку, если нет решений у СЛАУ 
  try:                              #от:
    x = np.linalg.solve(a, b)
    return x.flatten().tolist()
  except np.linalg.LinAlgError:
    return None                     #до:

                                    #теперь самое сложное - считать данные


n, m = map(int, input().split())
matr = []                         #создаём матрицу СЛАУ

for _ in range(n):                  #считываем введённые значения в матрицу
    r = list(map(float, input().split()))
    matr.append(r)

matr = np.array(matr)           #преобразуем в нампаевский лист, чтобы работала функция
solution = linsys(n, m, matr)     #вызов функции, чтобы найти решения

if solution is not None:            #нет ошибки - выводим решения
    print("Решение:")
    i = 1
    for  x in (solution):   
        print(f"x{i} = {x}")
        i += 1
else:
    print("Система не имеет решения или имеет бесконечно много решений.")