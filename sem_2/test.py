n, m = map(int, input().split())

graph = {i: {} for i in range(n + 1)}

for _ in range(m):
    parts = input().split()
    I, r, k, sign = int(parts[0]), int(parts[1]), int(parts[2]), parts[3]
    left = I - 1
    right = r

    if sign == ">=":
        u, v = right, left
        new_weight = -k
        if v in graph[u]:
            if new_weight < graph[u][v]:
                graph[u][v] = new_weight
        else:
            graph[u][v] = new_weight
    else:
        u, v = left, right
        new_weight = k
        if v in graph[u]:
            if new_weight < graph[u][v]:
                graph[u][v] = new_weight
        else:
            graph[u][v] = new_weight

def bellman_ford(graph, start, num_nodes):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0

    for _ in range(num_nodes):
        updated = False
        for u in graph:
            for v in graph[u]:
                if dist[u] != float('inf') and dist[v] > dist[u] + graph[u][v]:
                    dist[v] = dist[u] + graph[u][v]
                    updated = True
        if not updated:
            break

    for u in graph:
        for v in graph[u]:
            if dist[u] != float('inf') and dist[v] > dist[u] + graph[u][v]:
                return "NO"
    return "YES"

print(bellman_ford(graph, 0, n + 1))