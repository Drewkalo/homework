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
        if ((matching[neighbor] is None or dfs(G, visited, matching, matching[neighbor])) and (G[start][neighbor] > 0 and G[neighbor][start] > 0)):
            matching[neighbor] = start
            matching[start] = neighbor
            return True
    return False

def Kuhn(G):
    vertices = set(G.keys())
    for neighbors in G.values():
        vertices.update(neighbors)
    matching = {v: None for v in vertices}
    
    for v in G:
        if matching[v] is None:
            visited = set()
            dfs(G, visited, matching, v)
    return matching

#match = Kuhn(graph)
#print(match)
#print(graph)

while True:
    match = Kuhn(graph)
    all_paired = all(match.get(vert) is not None for vert in range(N))
    if not all_paired:
        break
    res += 1
    used_edges = set()
    for i in range(N):
        pair = match[i]
        if (i, pair) not in used_edges:
            used_edges.add((i, pair))
            used_edges.add((pair, i))
    for node1, node2 in used_edges:
        if graph[node1][node2] != inf:
            graph[node1][node2] = 0
            graph[node2][node1] = 0
            for neighbor in graph[node1]:
                graph[node1][neighbor] -= 1
        else:
            graph[node1][node2] = 0
            graph[node2][node1] = 0

print(res)

