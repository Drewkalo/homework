n,k = map(int,input().split())


G = {i:{} for i in range(4*n)}

G['S'] = {}
G['F'] = {}

for i in range(2*n):
    if i<n:
        G['S'][i] = 100
        G[i]['S'] = 0
        G[i][i+2*n]=k
        G[i+2*n][i]=0
    else:
        G[i]['F'] = 100
        G['F'][i] = 0
        G[i+2*n][i] = k
        G[i][i+2*n] = 0
for i in range(n):
    vvod = input()
    for j in range(len(vvod)):
        if vvod[j]=='1':
            G[i][j+n] = 1
            G[j+n][i] = 0
        else:
            G[i+2*n][j+3*n] = 1
            G[j+3*n][i+2*n] = 0

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
    return res,mat,prog
ford_fulkerson(G,'S','F')
mins=set()
for i in range(n):
    mins.add(100-G['S'][i])
    mins.add(G['F'][i+n])
print(str(min(mins)))
