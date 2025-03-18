M = int(input())

G = {}

edges = []

for i in range(M):
    v1,v2,w = input().split()
    w = float(w)
    edges.append((w,v1,v2))
    if v1 in G:
        G[v1][v2] = w
    else:
        G[v1] = {v2:w}
    if v2 in G:
        G[v2][v1] = w
    else:
        G[v2] = {v1:w}


class DSU:
    def __init__(self,G):
        self.parent = {i:i for i in G}
        self.rank = {i:1 for i in G}
    def find(self,v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]
    def union(self,v1,v2):
        p1 = self.find(v1)
        p2 = self.find(v2)
        if p1 == p2:
            return
        if self.rank[p1] == self.rank[p2]:
            self.rank[p1] += 1
        if self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p2] = p1

def Kruskal(G,edges):
    MST = []
    sorted_edges = sorted(edges)
    dsu = DSU(G)
    for edge in sorted_edges:
        if dsu.find(edge[1]) != dsu.find(edge[2]):
            dsu.union(edge[1],edge[2])
            MST.append([edge[1],edge[2]])
    return MST

print(Kruskal(G,edges))