#Топологическая сортировка

visited = set()
res = []

#это слово в слово dfs, но когда мы доходим до листа, то записываем его в res
def topological(G,visited,start,res):
    visited.add(start)
    for i in G[start]:
        if i not in visited:
            topological(G,visited,i,res)
    res.append(start)

N,M = map(int,input().split())

graph = {i:set() for i in range(1,N+1)}

for i in range(M):
    v1,v2 = map(int,input().split())
    graph[v1].add(v2)

#повторяем topological для каждой вершины, если она не была посещена, чтобы точно пройти все вершинки.
for i in graph:
    if i not in visited:
        topological(graph,visited,i,res)
print(res[::-1])