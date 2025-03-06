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


def Boruvka(G,edges):
    T = DSU(list(G.keys()))
    N = len(G)
    MST = []

    while N > 1:
        min_w = {i:None for i in G}
        for u,v,w in edges:
            p1 = T.find(u)
            p2 = T.find(v)
            if p1 != p2:
                if not min_w[p1] or min_w[p1][2] > w:
                    min_w[p1] = (u,v,w)
                if not min_w[p2] or min_w[p2][2] > w:
                    min_w[p2] = (u,v,w)
        for edge in min_w:
            if edge:
                u,v,w = edge
                if T.find(u) != T.find(v):
                    T.union(u,v)
                    MST.append((u,v,w))
                    N -= 1
    return MST

print(Boruvka(G,edges))
