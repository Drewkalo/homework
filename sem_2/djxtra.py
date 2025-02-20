import heapq

M = int(input())

G = {}

for i in range(M):
    v1,v2,w = input().split()
    w = float(w)
    if v1 in G:
        G[v1][v2] = w
    else:
        G[v1] = {v2:w}

def dejkstra(G, start):
    dist = {i: float('inf') for i in G}
    par = {i:None for i in G}
    dist[start] = 0
    h = [(0, start)]
    while h:
        cur_dist, cur_node = heapq.heappop(h)
        if cur_dist > dist[cur_node]:
            continue
        for neighbor in G[cur_node]:
            distance = cur_dist + G[cur_node][neighbor]
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                par[neighbor] = cur_node
                heapq.heappush(h, (distance, neighbor))
    return dist
