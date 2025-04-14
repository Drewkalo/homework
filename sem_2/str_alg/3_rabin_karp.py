import random

def rabin_karp(s,T):
    res = []
    q = 2**13-1
    x = random.randint(3,q-1)
    ht = [None]*(len(T)+1)
    hs = ord(s[0])
    ht[0] = 0
    for i in range(1,len(s)):
        hs = (x*hs+ord(s[i]))%q
    for i in range(len(T)):
        ht[i+1] = (x*ht[i]+ord(T[i]))%q
    for i in range(len(T)-len(s)+1):
        hlr = (ht[i+len(s)] - pow(x,len(s),q)*ht[i])%q
        if hlr == hs:
            for j in range(len(s)):
                if s[j] != T[i+j]:
                    break
            else:
                res.append(i)
    return res

print(rabin_karp('fbd','djfsjsfbdsbfdsbab'))