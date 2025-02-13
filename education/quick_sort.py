
def sort(n):
    if len(n) <= 0:
        return n
    pivot = len(n)//2
    great = [c for c in n if c > n[pivot]]
    eq = [c for c in n if c == n[pivot]]
    less = [c for c in n if c < n[pivot]]
    return sort(less) + eq + sort(great)
a = [1,4,5,7,1,9,10,23]
print(sort(a))