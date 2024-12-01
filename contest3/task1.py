def k_statistick(arr: list, k: int):
    if len(arr) == 1:
        return arr[0]
    op = arr[len(arr)//2]
    less = [x for x in arr if x < op]
    more = [x for x in arr if x > op]
    eq = [x for x in arr if x == op]

    if k < len(less):
        return k_statistick(less, k)
    elif k < len(less) + len(eq):
        return eq[0]
    else:
        return k_statistick(more, k - len(less) - len(eq))
    
n =[int(c) for c in input().split()]
cont = [int(c) for c in input().split()]
for i in range(n[1]):
    print(k_statistick(cont, i), end=" ")