class Node:
    def __init__(self,val = None):
        self.val = val
        self.left = None
        self.right = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
    def add(self,val):
        node = Node(val)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.right = node
            self.tail = node
    def remove(self):
        if not self.head:
            print('Empty')
            return None
        res = self.head.val
        self.head = self.head.right
        return res


M = int(input())

G = {}

for i in range(M):
    v1,v2,w = input().split()
    w = int(w)
    if v1 in G:
        G[v1][v2] = w
    else:
        G[v1] = {v2:w}
    if v2 in G:
        G[v2][v1] = 0
    else:
        G[v2] = {v1:0}


def dfs(G,start,finish,visited,f_min,dist,ptr):
    if start == finish:
        return f_min
    visited.add(start)
    for v in G[start]:
        if v not in ptr[start]:
            if (v not in visited and G[start][v] > 0 and (dist[v] == (dist[start]+1))):
                flow = dfs(G,v,finish,visited,min(f_min,G[start][v]),dist,ptr)
                G[start][v] -= flow
                G[v][start] += flow
                if flow > 0:
                    return flow
                else:
                    ptr[start].add(v)
    return 0

def bfs(G,queue,start,dist):
    queue.add(start)
    dist[start] = 0
    while queue.head:
        current = queue.remove()
        for i in G[current]:
            if dist[i] == None and G[current][i] > 0:
                queue.add(i)
                dist[i] = dist[current] + 1
    return dist['F'] != None


def dinic(G):
    res = 0
    dist = {i:None for i in G}
    queue = Deque()
    while bfs(G,queue,'S',dist):
        visited = set()
        ptr = {i:set() for i in G}
        while (flow:=dfs(G,'S','F',visited,float('inf'),dist,ptr)) != 0:
            res += flow
            visited = set()
        dist = {i:None for i in G}
        queue = Deque()
    return res
    
print(dinic(G))