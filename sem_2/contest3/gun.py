'''ef z_function(S, bord):
    n = len(S)
    zf = [0] * n
    left, right = 0,0
    for i in range(1, n):
        zf[i] = max(0, min(zf[i-left], right - i))
        while i + zf[i] < n and S[zf[i]] == S[i + zf[i]]:
            zf[i] += 1
        if i + zf[i] > right:
            left, right = i, i + zf[i]
    return max(zf[bord:])'''
def prefix(s:str, bord):
    n = len(s)
    pr = [0] * n

    for i in range(1, n):
        k = pr[i-1]

        while k != 0 and s[k] != s[i]:
            k = pr[k-1]

        if s[k] == s[i]:
            k += 1

        pr[i]=k

    return max(pr[bord:])


n = int(input())
drum_before = input().strip()
drum_after = input().strip()

case_1 = ('1' + drum_after) * 2
case_0 = ('0' + drum_after) * 2

temp_no = prefix(drum_before +'@'+ case_0,n)
temp_yes = prefix(drum_before +'@'+ case_1,n)

if temp_no >= (n-1) and temp_yes >= (n-1):
    print('Random')
elif temp_no >= (n-1):
    print('No')
else:
    print('Yes')