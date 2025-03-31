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
    price = 0
    sorted_edges = sorted(edges)
    dsu = DSU(G)
    for edge in sorted_edges:
        if dsu.find(edge[1]) != dsu.find(edge[2]):
            dsu.union(edge[1],edge[2])
            price += edge[0]
    return price

t = int(input())
result = []
for _ in range(t):
    n = int(input())
    graph = [int(i) for i in range(n)]
    pillar_cordinates = []
    for i in range(n):
        x, y = map(int, input().split())
        pillar_cordinates.append((x, y))

    cabel = []
    for i in range(n):
        x_out, y_out = pillar_cordinates[i]
        
        for k in range(i+1, n):
            x_in, y_in = pillar_cordinates[k]
            dist = ((x_in - x_out)**2 + (y_in - y_out)**2)**0.5
            cabel.append((dist, i, k))

    result.append("{0:.2f}".format(Kruskal(graph, cabel)))

print(*result, sep="\n")