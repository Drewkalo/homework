def fast_recombination_word(arr: list):
    if len(arr) <= 1:
        return arr
    op = arr[len(arr) // 2]
    less = [x for x in arr if x < op]
    eq = [x for x in arr if x == op]
    more = [x for x in arr if x > op]
    return fast_recombination_word(less) + eq + fast_recombination_word(more)


def sort_word(arr: list):
    word_dict = {}
    for word in arr:
        sorting = "".join(sorted(word))
        if sorting not in word_dict:
            word_dict[sorting] = []
        word_dict[sorting].append(word)
    return list(word_dict.values())


def sort_alphabet2(arr):
    if len(arr) <= 1:
        return arr
    op = arr[len(arr) // 2]
    less = [x for x in arr if x[1] < op[1]]
    eq = [x for x in arr if x[1] == op[1]]
    more = [x for x in arr if x[1] > op[1]]
    return sort_alphabet2(less) + eq + sort_alphabet2(more)


def sort_alphabet(arr):
    if len(arr) <= 1:
        return arr
    op = arr[len(arr) // 2]
    less = [x for x in arr if x[0] < op[0]]
    eq = [x for x in arr if x[0] == op[0]]
    more = [x for x in arr if x[0] > op[0]]
    return sort_alphabet(less) + sort_alphabet2(eq) + sort_alphabet(more)


temporary = [str(x) for x in input().split()]
sorted_list = sort_word(temporary)

#Sorting without sort() -  Implementation using insertion sort for demonstration.  For larger datasets, a more efficient algorithm (like merge sort) would be preferable.
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and len(arr[j]) < len(key):  #comparing lengths
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


sorted_list = insertion_sort(sorted_list)


for group in sorted_list:
    print(*sort_alphabet(group), end=" ")

