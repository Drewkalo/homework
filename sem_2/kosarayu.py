from collections import deque
N,M = map(int,input().split())

graph = {i:set() for i in range(N)}
reversed_graph = {i:set() for i in range(N)}

for i in range(M):
    v1,v2 = map(int,input().split())
    graph[v1].add(v2)
    reversed_graph[v2].add(v1)

visited = []
stack = deque()
res = []

def topological(G,visited,start, stack = None, res):
    visited.append(start)
    for i in G[start]:
        if i not in visited:
            topological(G,visited,i,stack, res)
    if stack:
        stack.push(start)
    if res 


for i in G:
    if i not in visited:
        topological(G,visited,i, stack,res)

result = []

while stack:
    current = stack.pop()
    if current not in visited:
        l = []
        topological(reversed_graph, visited, curent, l = l)
        result.append(l)

print(result)