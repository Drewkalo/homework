#Сортировка выбором выполняется за O(n^2) времени и шагов (квадратичное время)

def find_smallest(arr: list):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def select_sort(arr: list):
    new_arr = []
    for i in range(len(arr)):
        new_arr.append(arr.pop(find_smallest(arr)))
    return new_arr

my_list = [3, 1, 0, 9, -4, 70, -21, 89, 77, 88, 99, 23, 34, 45, 56]
print(select_sort(my_list))
