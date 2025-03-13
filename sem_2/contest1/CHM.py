class DSU:
    def __init__(self, G):
        self.parent = {i:i for i in G}
        self.rank = {i:1 for i in G}
        
    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]
    
    def union(self, v1, v2):
        u1 = self.find(v1)
        u2 = self.find(v2)
        if u1 == u2:
            return
        if self.rank[u1] == self.rank[u2]:
            self.rank[u1] += 1
        if self.rank[u1] < self.rank[u2]:
            self.parent[u1] = u2
        else:
            self.parent[u2] = u1

n, m, k = map(int, input().split())
graph = {i:set() for i in range(1, n+1)}

for i in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].add(v2)
    graph[v2].add(v1)

dsu = DSU(graph)
queue = [input().split() for i in range(k)]
res = []

for temp in queue[::-1]:
    v1 = int(temp[1])
    v2 = int(temp[2])
    if temp[0] == "ask":
        if dsu.find(v1) == dsu.find(v2):
            res.append("YES")
        else:
            res.append("NO")
    else:
        dsu.union(v1, v2)


print(*res[::-1], sep="\n")