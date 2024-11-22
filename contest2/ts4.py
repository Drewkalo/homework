def fast_recombination_word(arr: list):  

    if len(arr) <= 1:
        return arr
    
    op = arr[len(arr)//2]
    less = [x for x in arr if x < op]
    eq = [x for x in arr if x == op]
    more = [x for x in arr if x > op]
    
    return fast_recombination_word(less) + eq + fast_recombination_word(more)


def sort_word(arr: list):              
    word_dict = {}
    for word in arr:
        sorting = "".join(fast_recombination_word(word))
        if sorting not in word_dict:
            word_dict[sorting] = []
        word_dict[sorting].append(word)

    return (list(word_dict.values()))

def sort_alphabet2(arr):                
    if len(arr) <= 1:
        return arr
    op = arr[len(arr)//2]
    less = [x for x in arr if x[1] < op [1]]
    eq = [x for x in arr if x[1] == op [1]]
    more = [x for x in arr if x[1] > op [1]]
    return sort_alphabet2(less) + eq + sort_alphabet2(more)

def sort_alphabet(arr):                 
    if len(arr) <= 1:
        return arr
    op = arr[len(arr)//2]
    less = [x for x in arr if x[0] < op [0]]
    eq = [x for x in arr if x[0] == op [0]]
    more = [x for x in arr if x[0] > op [0]]
    return sort_alphabet(less) + sort_alphabet2(eq) + sort_alphabet(more)

def sort_lists(arr):                   
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if len(arr[j]) < len(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

temporary = [str(x) for x in input().split()]
sorted_list = sort_lists(sort_word(temporary))

ordinarylists = [x for x in sorted_list if len(x) == 1]
morelists = [x for x in sorted_list if len(x) > 1]
for x in morelists:
    print(*sort_alphabet(x), end=" ")
for j in sort_alphabet(ordinarylists):
    print(*j, end=" ")

