def step(n,k):
    if n == 0 and k == 0:
        return 1
    if n < 0 or k < 0:
        return 0
    count = step(n-2,k-1) + step(n-1, k-2)
    return count
print(step(3,2))

