from math import sqrt
#предпроцессинг за O(n), запрос за O(√n), где n-длина массива, делим наш массив на отрезки с длинной √n, 
#считаем минимум/максимум/сумму на отрезках, при запросе смотрим на диапозон и используем данные.
'''Нам нужно получить ответ на запрос на каком-то отрезке [l, r]. Этот отрезок 
может включать в себя несколько отрезков s. Чтобы найти значения на каждом 
из них - потребуется одна операция(и отрезков не более sqrt(n)). Концы отрезка 
могут лежать в каких-то si. Тогда в этих si надо будет посчитать тривиально - но 
там элементов не более sqrt(n). Получаем сложность не более O(sqrt(n)). 
При изменении какого-то элемента достаточно пересчитать только значение в 
блоке. - O(1) 
'''
def rmq_preprocess(arr):
    n = len(arr)
    b = int(sqrt(n))
    block_mins = []
    for i in range(0, n, b):
        block_mins.append(min(arr[i:i+b]))
    return block_mins, b

def rmq_query(arr, block_mins, b, l, r):
    min_val = float('inf')
    block_l = l // b
    block_r = r // b
    if block_l == block_r:
        min_val = min(arr[l:r+1])
    else:
        min_val = min(min_val, min(arr[l: (block_l+1)*b]))
        for i in range(block_l+1, block_r):
            min_val = min(min_val, block_mins[i])
        min_val = min(min_val, min(arr[block_r*b: r+1]))
    return min_val

#Пример
arr1 = [1, 5, 2, 8, 3, 9, 4, 7, 6, 10]
block_mins, b = rmq_preprocess(arr1)
print(rmq_query(arr1, block_mins, b, 2, 7)) #находим минимум в диапазоне [2,7]

def rsq_preprocess(arr):
    n = len(arr)
    b = int(sqrt(n))
    block_sums = []
    for i in range(0, n, b):
        block_sums.append(sum(arr[i:i+b]))
    return block_sums, b

def rsq_query(arr, block_sums, b, l, r):
    total = 0
    block_l = l // b
    block_r = r // b
    if block_l == block_r:
        total += sum(arr[l:r+1])
    else:
        total += sum(arr[l: (block_l+1)*b])
        for i in range(block_l+1, block_r):
            total += block_sums[i]
        total += sum(arr[block_r*b: r+1])
    return total

#Пример
arr2 = [1, 5, 2, 8, 3, 9, 4, 7, 6, 10]
block_sums, b = rsq_preprocess(arr2)
print(rsq_query(arr2, block_sums, b, 2, 7))