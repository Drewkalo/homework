n, m = map(int, input().split())

graph = {i:{} for i in range(n + 1)}

for i in range(m):
    v1, v2, w, sign = input().split()
    v1, v2, w = int(v1) - 1, int(v2), int(w)

    if sign == ">=":
        u, v = v1, v2
        w = -w
    else:
        u, v = v2, v1
        w = w

    if v in graph[u]:
        graph[u][v] = min(graph[u][v], w)
    else:
        graph[u][v] = w

def bellman_ford(G, start):
        d = {i: float('inf') for i in G}
        d[start] = 0

        for i in range(len(G)):
            for node1 in G:
                for node2 in G[node1]: 
                    if d[node1] != float("inf") and  d[node2] > d[node1] + G[node1][node2]:
                        d[node2] = d[node1] + G[node1][node2]

        for node1 in G:
            for node2  in G[node1]:
                if d[node1] != float("inf") and d[node2] > d[node1] + G[node1][node2]:
                    return "NO"

        return "YES"

print(bellman_ford(graph, 0))
