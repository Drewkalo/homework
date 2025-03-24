
def prefix(s:str):
    n = len(s)
    pr = [0] * n

    for i in range(1, n):
        k = pr[i-1]

        while k != 0 and s[k] != s[i]:
            k = pr[k-1]

        if s[k] == s[i]:
            k += 1

        pr[i]=k
    return pr

print(prefix("abracadabra"))