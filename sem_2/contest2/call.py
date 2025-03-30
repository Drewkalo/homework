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

n, m, p = map(int, input().split())

unsafe_build = set(map(int, input().split()))
builds = set([i for i in range(1, n + 1)])
safe_build = builds - unsafe_build


unsafe_edges = []
edges = []

graph = {}
flag = True

for _ in range(m):
    v1, v2, cost = map(int, input().split())
    if v1 in unsafe_build or v2 in unsafe_build: 
        unsafe_edges.append((cost, v1, v2))
    else:
        edges.append((cost, v1, v2))
    if v1 in graph:
        graph[v1][v2] = cost
    else:
        graph[v1] = {v2:cost}
    if v2 in graph:
        graph[v2][v1] = cost
    else:
        graph[v2] = {v1:cost}

def Kruskal(G, edges, unsafe_edges):
    MST = []
    sorted_edges = sorted(edges)
    dsu = DSU(G)
    for edge in sorted_edges:
        if dsu.find(edge[1]) != dsu.find(edge[2]) and edge not in unsafe_edges:
            dsu.union(edge[1],edge[2])
            MST.append([edge[1],edge[2]])
    return MST

MST = Kruskal(graph, edges, unsafe_edges)
mst_points = set()
for edge in MST:
    mst_points.add(edge[0])
    mst_points.add(edge[1])

if unsafe_build | mst_points == builds:
    price = 0
    for edge in MST:
        price += graph[edge[0]][edge[1]]

    for point in unsafe_build:
        min_cost = float("inf")
        min_edge = None

        for cost, v1, v2 in unsafe_edges:
            if (v1 in mst_points and v2 == point) or (v2 in mst_points and v1 == point):
                if cost < min_cost:
                    min_cost = cost
                    min_edge = (v1, v2)

        if min_edge is None:
            print("impossible")
            break
        else:
            price += min_cost
    else:
        print(price)
else:
    print("impossible")

