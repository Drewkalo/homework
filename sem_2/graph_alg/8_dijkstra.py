#Дейкстра для поиска наименьшего по цене пути в графе (НЕ РАБОТАЕТ С ОТРИЦАТЕЛЬНЫМИ ВЕСАМИ)
#Жадный алгоритм, каждый раз обновляем расстояние до соседей вершинки
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
    if v2 in G:
        G[v2][v1] = w
    else:
        G[v2] = {v1:w}

def dijkstra(G,start):
    distances = {i:float('infinity') for i in G}
    distances[start] = 0
    h = [(0,start)]
    while h:
        cur_dist, cur_node = heapq.heappop(h)
        if cur_dist > distances[cur_node]:
            continue
        for neighbor in G[cur_node]:
            distance = cur_dist + G[cur_node][neighbor]
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(h,(distance,neighbor))
    return distances

print(dijkstra(G,'A'))
    


