'''Алгоритм использует принцип «разделяй и властвуй»: задача разбивается на подзадачи меньшего размера, которые решаются по отдельности, после чего их решения комбинируются для получения решения исходной задачи. Конкретно процедуру сортировки слиянием можно описать следующим образом:
Если в рассматриваемом массиве один элемент, то он уже отсортирован — алгоритм завершает работу.
Иначе массив разбивается на две части, которые сортируются рекурсивно.
После сортировки двух частей массива к ним применяется процедура слияния, которая по двум отсортированным частям получает исходный 
отсортированный массив.
T(n) = 2T(n/2) + O(n) = 4T(n/4) + 2O(n) = ... = T(1) + logn * O(n) = O(nlogn)
'''
def merge(left, right):  
    res = []
    left_cnt = right_cnt = 0


    for i in range(len(left) + len(right)):
        if left_cnt < len(left) and right_cnt < len(right):
            if left[left_cnt] <= right[right_cnt]:
                res.append(left[left_cnt])
                left_cnt += 1

            else:
                res.append(right[right_cnt])
                right_cnt += 1

        elif left_cnt == len(left):
            res.append(right[right_cnt])
            right_cnt += 1

        elif right_cnt == len(right):
            res.append(left[left_cnt])
            left_cnt += 1

    return res

def merge_sort(arry):  
    if len(arry) <= 1:
        return arry

    left = merge_sort(arry[:len(arry)//2])
    right = merge_sort(arry[len(arry)//2:])
  
    return merge(left, right)

s = [89,0,0,3,3,56,76,87,90]  
print(merge_sort(s))