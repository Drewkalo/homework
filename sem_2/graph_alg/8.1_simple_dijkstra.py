M = int(input())

G = {}

for i in range(M):
    v1,v2,w = input().split()
    w = float(w)
    if v1 in G:
        G[v1][v2] = w
    else:
        G[v1] = {v2:w}
    if v2 in G:
        G[v2][v1] = w
    else:
        G[v2] = {v1:w}

# Простой алгоритм Дейкстры без использования кучи      

def dijkstra(G,start):
    distances = {i:float('inf') for i in G}
    distances[start] = 0
    visited = {}
    while len(visited) < len(G):
        cur = min(distances,key=distances.get)
        visited[cur] = distances[cur]
        for node in G[cur]:
            if node not in visited:
                if distances[node] > distances[cur] + G[cur][node]:
                    distances[node] = distances[cur] + G[cur][node]
        distances[cur] = float('inf')
    return visited
print(dijkstra(G,'A'))