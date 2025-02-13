def bin_search_recursive(arr: list, low, high, k):
    if high <= low:
        return 0
    
    mid = (low + high)//2
    if k < arr[mid]:
        return bin_search_recursive(arr, low, mid-1, k)
    elif k == arr[mid]:
        return mid
    else:
        return bin_search_recursive(arr, mid+1, high, k)

my_list = [7,1,6,3,8,9,20,3,5]
print(bin_search_recursive(my_list, 0, len(my_list)-1, 20))