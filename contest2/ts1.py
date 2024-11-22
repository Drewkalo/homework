def root(num):
    cont = 0
    if len(str(num)) == 1:
        return num
    while len(str(num)) >= 2:
        for i in str(num):
            cont += int(i)
        num = cont
        cont = 0
    return num
def fasteq(arr: list):
    if len(arr) <= 1:
        return arr
    op = arr[len(arr)//2]
    less = [x for x in arr if x < op]
    eq = [x for x in arr if x == op]
    more = [x for x in arr if x > op]

    return fasteq(less) + eq  + fasteq(more)
def fast_sort(arr: list):
    if len(arr) <= 1:
        return arr
    op = arr[len(arr)//2]
    less = [x for x in arr if root(x) < root(op)]
    eq = [x for x in arr if root(x) == root(op)]
    more = [x for x in arr if root(x) > root(op)]

    return fast_sort(less) + fasteq(eq)  + fast_sort(more)

s = [int(x) for x in input().split()]
print(*fast_sort(s))
    

