N, k = map(int, input().split())
graph = {}
inf = float("inf")
infinity_edge = set()
for i in range(N):
    temp = input()
    for j in range(len(temp), 2*len(temp)):
        if i not in graph:
            if temp[j-len(temp)] == str(0):
                graph[i] = {j:k}
            else:
                infinity_edge.add((i, j))
                graph[i] = {j:k+1}
        else:
            if temp[j-len(temp)] == str(0):
                graph[i][j] = k
            else:
                infinity_edge.add((i, j))
                graph[i][j] = k+1

        if j not in graph:
            graph[j] = {i:0}
        else:
            graph[j][i] = 0

graph[-1] = {}
graph[2*N] = {}
for i in range(N):
    graph[-1][i] = 1
    graph[i][-1] = 0
for i in range(len(temp), 2*len(temp)):
    graph[2*N][i] = 0
    graph[i][2*N] = 1

'''copy_graph = {}
for node in graph:
    copy_graph[node] = {}
    for neighbor, weight in graph[node].items():
        copy_graph[node][neighbor] = weight'''

#print(graph)
#print(graph.keys())

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

cnt = 0
while (flow:=ford_fulkerson(graph, -1, 2*N)) == N:
    cnt += 1
    for i in range(N):
        graph[-1][i] = 1
        graph[i][-1] = 0
    for i in range(len(temp), 2*len(temp)):
        graph[2*N][i] = 0
        graph[i][2*N] = 1

    #print(graph)
    if k != 0 and cnt < N:
        u, v = infinity_edge.pop()
        graph[u][v] = 0
    #print(graph)

print(cnt)