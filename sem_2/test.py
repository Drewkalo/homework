N, k = map(int, input().split())
graph = {}
res = 0
inf = float("inf")
for i in range(N):
    temp = input()
    for j in range(len(temp), 2*len(temp)):
        if i not in graph:
            if temp[j-len(temp)] == str(0):
                graph[i] = {j:k}
            else:
                graph[i] = {j:inf}
        else:
            if temp[j-len(temp)] == str(0):
                graph[i][j] = k
            else:
                graph[i][j] = inf

        if j not in graph:
            if temp[j-len(temp)] == str(0):
                graph[j] = {i:k}
            else:
                graph[j] = {i:inf}
        else:
            if temp[j-len(temp)] == str(0):
                graph[j][i] = k
            else:
                graph[j][i] = inf

#print(graph)

def dfs(G, visited, matching, start):
    if start in visited:
        return False
    visited.add(start)
    for neighbor in G.get(start, set()):
        if ((matching[neighbor] is None or dfs(G, visited, matching, matching[neighbor])) and G[start][neighbor] > 0 and G[neighbor][start] > 0):
            matching[neighbor] = start
            matching[start] = neighbor
            return True
    return False

def Kuhn(G):
    matching = {v: None for v in G}
    
    for v in range(N):
        if matching[v] is None:
            visited = set()
            dfs(G, visited, matching, v)
    return matching

#match = Kuhn(graph)
#print(match)

#print(graph)

while True:
    match = Kuhn(graph)
    #print(match)
    #print(graph)
    if len([i for i in match.values() if i is not None])//2 == N:
        res += 1
        for vert in match:
            if graph[vert][match[vert]] != inf:
                del graph[vert][match[vert]]
                for neighbor in graph[vert]:
                    graph[vert][neighbor] -= 1
            else:
                del graph[vert][match[vert]]
        #print(graph)
    else:
        break

print(res)

