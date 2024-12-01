def summ(arr: list):
    if len(arr) <= 1:
        return arr[0]
    return arr[0] + summ(arr[1:])

my_list = [1,2,3,4,5,6,7,8,9,10]
print(summ(my_list))
