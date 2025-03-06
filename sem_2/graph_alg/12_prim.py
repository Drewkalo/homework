M = int(input())

G = {}

for i in range(M):
    v1,v2,w = input().split()
    w = float(w)
    if v1 in G:
        G[v1][v2] = w
    else:
        G[v1] = {v2:w}
    if v2 in G:
        G[v2][v1] = w
    else:
        G[v2] = {v1:w}

def Prim(G):
    MST = []
    dist = {i:float('inf') for i in G}
    start = list(G.keys())[0]
    dist[start] = 0
    prev = {i:None for i in G}
    visited = set()
    while len(visited) != len(G):
        v = min(dist,key=dist.get)
        visited.add(v)
        if prev[v] is not None:
            MST.append([prev[v],v])
        for u in G[v]:
            if u not in visited and dist[u]>G[v][u]:
                prev[u] = v
                dist[u] = G[v][u]
        dist[v] = float('inf')
    return MST

print(Prim(G))