s = str(input())
p = str(input())

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

def part(P, S):
    mesh = z_function(P + "#" + S)
    return (mesh.index(len(P)) - len(P) - 1) 

print(part(p, s))

# можно выводить индексы подстроки в тексте