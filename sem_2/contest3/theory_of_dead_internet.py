'''def prefix(s:str):
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

n = int(input())
words = input().split()
# print(words)
res = ''
res += words[0]
# print(res)
for i in range(1,n):
    len_common = prefix(words[i] +'#' + res)[len(res + words[i])]
    res += words[i][len_common:]

print(res)
'''
'''
def naive_prefix_function(s):
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        max_k = 0
        for k in range(1, i + 1):
            # Сравниваем префикс и суффикс
            if s[:k] == s[i - k + 1 : i + 1]:
                max_k = k
        pi[i] = max_k
    return pi
'''
n = int(input())
words = input().split()
res = ''
res += words[0]
for i in range(1, n):
    len_res = len(res)
    word = words[i]
    k = min(len_res, len(word))
    # print('k:',k)
    temp = [0]
    for j in range(k):
        suff = res[-k+j:]
        pref = word[:len(suff)]
        # print('suff:',suff)
        # print('pref:',pref)
        cont = 0
        for _ in range(len(suff)):
            if suff[_] == pref[_]:
                cont += 1
            else:
                cont = 0
                break
        temp.append(cont)

    # print(temp)
    len_common = max(temp)
    res += words[i][len_common:]
    # print('temp_res:', res)
print(res)
