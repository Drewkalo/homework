M = int(input())

G = {}

for i in range(M):
    v1,v2,w = input().split()
    w = int(w)
    if v1 in G:
        G[v1][v2] = w
    else:
        G[v1] = {v2:w}
    if v2 in G:
        G[v2][v1] = 0
    else:
        G[v2] = {v1:0}

def dfs(G,start,finish,visited,f_min):
    if start == finish:
        return f_min
    visited.add(start)
    for v in G[start]:
        if (v not in visited and G[start][v] > 0):
            flow = dfs(G,v,finish,visited,min(f_min,G[start][v]))
            G[start][v] -= flow
            G[v][start] += flow
            if flow > 0:
                return flow
    return 0
        

def ford_fulkerson(G,start,finish):
    visited = set()
    res = 0
    while (flow:=dfs(G,start,finish,visited,float('inf'))) != 0:
        res += flow
        visited = set()
    return res

print(ford_fulkerson(G,'0','5'))


