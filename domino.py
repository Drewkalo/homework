#дз сделать функцию для поиска эйлерова цикла
n = int(input())

flag = True

S = set()

visited = []
def dfs(G,visited,start):
    visited.append(start)
    for i in G[start]:
        if i not in visited:
            dfs(G,visited,i)


graph = {i:set() for i in range(n+1)}

for i in range(n):
    v1,v2 = map(int,input().split())
    graph[v1].add(v2)
    graph[v2].add(v1)
print(graph)
for j in graph:
    S.add(j)

for j in S:
    count = 0
    if len(graph[j]) %2 == 0:
        continue
    else:
        count += 1
        if count > 2:
            break

if flag == True:
    dfs(graph, visited, 0)
    if visited != S:
        print("No")
    else:
        print("Yes")
else:
    print("No")

