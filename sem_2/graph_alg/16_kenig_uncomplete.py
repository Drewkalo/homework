M = int(input())

G = {}

for i in range(M):
    v1,v2 = input().split()
    if v1 in G:
        G[v1].add(v2)
    else:
        G[v1] = {v2}
    if v2 in G:
        G[v2].add(v1)
    else:
        G[v2] = {v1}


def dfs_kuhn(G,visited,matching,start):
    if start in visited:
        return False
    visited.add(start)
    for i in G[start]:
        if not matching[i] or dfs_kuhn(G,visited,matching,matching[i]):
            matching[i] = start
            matching[start] = i
            return True            
    return False

def Kuhn(G, half):
    matching = {i:None for i in G}
    for i in half:
        visited = set()
        if not matching[i]:
            dfs_kuhn(G,visited,matching,i)
    return matching

matchinh = Kuhn(G, L)