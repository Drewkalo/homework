s = str(input())

def z_function(S):
    zf = [0] * len(S)
    left, right = 0,0
    for i in range(1, len(S)):
        zf[i] = max(0, min(zf[i-left], right - i))
        while i + zf[i] < len(S) and S[zf[i]] == S[i + zf[i]]:
            zf[i] += 1
        if i + zf[i] > right:
            left, right = i, i + zf[i]
    return zf
# доработать z[i] + i = |s| and |s| % i == 0

def restock(s):
    zf = z_function(s)
    temp = sorted(list(set(zf)))
    try:
        deg = temp[1]
    except IndexError:
        return s
    if deg == 1:
        return "NO"
    flag = True
    for i in temp[::-1]:
        if i % deg != 0:
            flag = False
            break

    if flag:
        return(s[0:deg])
    else:
        return "NO"
    
print(restock(s))