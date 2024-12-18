def factor(n):
    ans = []
    d = 2
    while d^2 <= n:
        if n % d == 0:
            ans.append(d)
            n = n//d
        else:
            d += 1
    if n > 1:
        ans.append(n)
    return ans
print(*factor(100))