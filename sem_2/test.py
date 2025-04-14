N, k = map(int, input().split())
graph = {}
inf = float('inf')

for i in range(N):
    line = input().strip()
    for j in range(N):
        exp = i
        proc = j + N
        if line[j] == '1':
            capacity = inf
        else:
            capacity = k
        if exp not in graph:
            graph[exp] = {}
        if proc not in graph:
            graph[proc] = {}
        graph[exp][proc] = capacity
        graph[proc][exp] = capacity

def dfs(u, visited, match, graph):
    if u in visited:
        return False
    visited.add(u)
    for v in graph.get(u, {}):
        if graph[u][v] > 0:
            if match[v] is None or dfs(match[v], visited, match, graph):
                match[u] = v
                match[v] = u
                return True
    return False

def kuhn(graph, N):
    match = {u: None for u in graph}
    for u in range(N):
        if match[u] is None:
            visited = set()
            dfs(u, visited, match, graph)
    return match

res = 0

while True:
    match = kuhn(graph, N)
    all_paired = all(match.get(u) is not None for u in range(N))
    if not all_paired:
        break
    res += 1
    used_edges = set()
    for u in range(N):
        v = match[u]
        if (u, v) not in used_edges:
            used_edges.add((u, v))
            used_edges.add((v, u))
            if graph[u][v] != inf:
                graph[u][v] -= 1
                graph[v][u] -= 1
                if graph[u][v] <= 0:
                    del graph[u][v]
                    del graph[v][u]

print(res)

