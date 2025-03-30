n = int(input())

letters =[chr(i) for i in range(65,65+n)]
numbers = range(1,n+1)

G = {}

for i in letters:
    for j in numbers:
        if i in G:
            G[i].add(j)
        else:
            G[i] = {j}
        if j in G:
            G[j].add(i)
        else:
            G[j] = {i}

m = int(input())

for i in range(m):
    square = input()
    l = square[0]
    k = int(square[1])
    G[l].remove(k)
    G[k].remove(l)

def dfs(G,visited,matching,start):
    if start in visited:
        return False
    visited.add(start)
    for i in G[start]:
        if not matching[i] or dfs(G,visited,matching,matching[i]):
            matching[i] = start
            matching[start] = i
            return True            
    return False

def broken_chess(G,n):
    matching = {i:None for i in G}
    lm = 0
    for i in G:
        visited = set()
        if not matching[i]:
            lm += dfs(G,visited,matching,i)
    return n <= lm

print(broken_chess(G,n))