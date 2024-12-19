def sort(arr: list):
    for i in range(1, len(arr)):
        j = i-1
        key = arr[i]
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
a = [1, 6, 9, 3, 2, 10]
print(*sort(a))
