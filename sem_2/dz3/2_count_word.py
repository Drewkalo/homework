import random

def rabin_karp(s,T):
    res = 0
    q = 2**13-1
    x = random.randint(3,q-1)
    ht = [None]*(len(T)+1)
    ht[0] = 0
    # создаём все циклические сдвиги
    hashes = {s[i:] + s[:i]:None for i in range(len(s))}
    # вычисляем для них хеши
    for i in hashes:
        hs = ord(i[0])%q
        for j in range(1,len(i)):
            hs = (x*hs+ord(i[j]))%q
        hashes[i] = hs
    for i in range(len(T)):
        ht[i+1] = (x*ht[i]+ord(T[i]))%q

    for i in range(len(T)-len(s)+1):
        hlr = (ht[i+len(s)] - pow(x,len(s),q)*ht[i])%q
        if hlr in hashes.values():
            res += 1
    return res

print(rabin_karp('abc', 'abcabacbacababc'))
