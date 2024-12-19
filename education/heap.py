#построение за 0(n), остальное за 0(logn), сортировка за 0(n logn), реализуем на массиве, 
#значение в корне больше, чем в детях
def heapify(arr, n, i):
    largest = i # Initialize largest as root
    l = 2 * i + 1   # left = 2*i + 1
    r = 2 * i + 2   # right = 2*i + 2

  # Проверяем существует ли левый дочерний элемент больший, чем корень

    if l < n and arr[largest] < arr[l]:
        largest = l

    # Проверяем существует ли правый дочерний элемент больший, чем корень

    if r < n and arr[largest] < arr[r]:
        largest = r

    # Заменяем корень, если нужно
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i] # свап

        # Применяем heapify к корню.
        heapify(arr, n, largest)

arr = [ 12, 11, 13, 5, 6, 7]
for i in range(len(arr), -1, -1):
        heapify(arr, len(arr), i)
print(arr)