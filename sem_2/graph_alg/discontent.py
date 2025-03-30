n = int(input())

G = {i:{} for i in range(n)}

G['S'] = {}
G['F'] = {}

for i in range(n):
    ai, bi = map(int,input().split())
    G['S'][i] = ai
    G[i]['F'] = bi
    G[i]['S'] = 0
    G['F'][i] = 0

m = int(input())

for i in range(m):
   vi,vj,cij = map(int,input().split())
   G[vi][vj] = cij
   G[vj][vi] = 0

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
    prog = set()
    mat = set()
    visited = set()
    dfs(G,'S','F',visited,float('inf'))
    prog = visited - {'S','F'}
    mat = set(G) - visited - {'S','F'}
    print(G)
    return res,mat,prog

print(ford_fulkerson(G,'S','F'))