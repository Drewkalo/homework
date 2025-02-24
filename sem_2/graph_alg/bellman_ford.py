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

def bellman_ford(G, start):
    d = {i:float('inf') for i in G}
    parents = {i:None for i in G}                           #запоминаем путь в списке
    d[start] = 0
    for i in range(len(G) - 1):
        for node1 in d:
            for node2 in G[node1]:
                if d[node2] > d[node1] + G[node1][node2]:
                    d[node2] = d[node1] + G[node1][node2]
                    parents[node2] = node1
    return d