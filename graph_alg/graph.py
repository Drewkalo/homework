#Считывание графа

N,M = map(int,input().split())

graph = {i:set() for i in range(N)}

for i in range(M):
    v1,v2 = map(int,input().split())
    graph[v1].add(v2)
    graph[v2].add(v1)