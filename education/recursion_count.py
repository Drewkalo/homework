def count(arr):
    if len(arr) == 1:
        return 1
    elif len(arr) == 0:
        return 0 
    return 1 + count(arr[1:])

my_list = [1,2,3,4,5,6,7,8,9,10]
print(count(my_list))