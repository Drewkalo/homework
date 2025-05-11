#алгоритм поиска пути между всеми парами вершин в графе (O(V^2))
#строим матрицу смежности d, где d[i][j] расстояние между вершинами i и j.
#Перебором по всем вершинам k пытаемся уменьшить расстояние d[j][k] = min(d[j][k], d[j][i] + d[i][k])

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

def floyd_warshall(G):
    d = {i:{j:float("inf") for j in G} for i in G}
    p = {i: {j: None for j in G} for i in G}

    for i in G:
        d[i][i] = 0
        p[i][i] = i
    for node1 in G:
        for node2 in G[node1]:
            d[node1][node2] = G[node1][node2]
            p[node1][node2] = node1
    for i in G:
        for j in G:
            for k in G:
                d[j][k] = min(d[j][k], d[j][i] + d[i][k])
                p[j][k] = p[i][k]
    return d, p

print(floyd_warshall(G))