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

def floyd_warshall(G, start):
    d = {i:{j:float("inf") for j in G} for i in G}
    for i in G:
        d[i][i] = 0
    for node1 in G:
        for node2 in G[node1]:
            d[node1][node2] = G[node1][node2]
    for i in G:
        for j in G:
            for k in G:
                d[j][k] = min(d[j][k], d[j][i] + d[i][k])
    return d