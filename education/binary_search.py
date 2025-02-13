#В общем случае, Бинарный поиск выполняется за log₂n шагов и логарифмическое время O(logn ), 
def binary_search(arr: list, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high)//2
        guess = arr[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1 
    return None

my_lst = [1,3,5,7,9,10]
print(binary_search(my_lst, 9))